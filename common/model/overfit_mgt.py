from common.model.MODEL_MGT_PARAMS import *
from common.model.loss_mgt import *
from common.misc.RollingBuffer import *
from common.misc.fileops import *
from common.model.model_storage import *
from common.render.print_colors import *

def overfit_mgr(fn_stop_training, model, plugin_name):
    _loss_info = loss_mgr()
    _recent_epochs_to_track = RollingBuffer(RECENT_EPOCHS_BUFFER)
    fn_loss_direction = loss_mgr()
    _archive_dir_path = get_abs_path('plugins/' + plugin_name + '/model_data/archive/')
    remove_directory_tree(_archive_dir_path)
    print ('cleaned archive if that was needed')

    def save_model_in_archive():
        nonlocal  plugin_name, _archive_dir_path
        dt_now = get_filename_based_on_time()
        model_file_path = _archive_dir_path + dt_now
        save_model(model_file_path, model)
        print ('save model {} in archive'.format(dt_now))
        return model_file_path

    def cleanup_model_overspill(info):
        _, _, _, _, old_model_path = info
        remove_file(old_model_path + '.h5')
        remove_file(old_model_path + '.json')

    def fn_check_overfitting(iter_num, epoch_num, batch_num, logs):
        nonlocal  _recent_epochs_to_track
        val_loss_direction, changed_val_loss_direction = fn_loss_direction(logs)
        val_loss = logs[VAL_LOSS]

        if val_loss_direction <= 0:
            print(colors.ok + '>>> PROGRESS >>>' + colors.close, end=' ')
        else:
            print(colors.fail + '<<< REGRESS <<<' + colors.close, end=' ')

        print('val_loss => {}::    DIRECTION => {} and CHANGED_DIRECTION => {}'.format(val_loss, val_loss_direction, changed_val_loss_direction))

        if val_loss_direction > 0 and changed_val_loss_direction == True:
            _recent_epochs_to_track.reset()
            remove_directory_tree(_archive_dir_path) # cleanup archive

        if val_loss_direction > 0:
            new_model_filepath = save_model_in_archive()
            info = (iter_num, epoch_num, batch_num, logs, new_model_filepath)
            _recent_epochs_to_track.add(info, cleanup_model_overspill)
            info_count = _recent_epochs_to_track.count()
            if info_count > MAX_CONSECUTIVE_LOSS_DEGRATION_COUNT:
                    fn_stop_and_clean()

    def find_model_filepath_for_lowest_val_loss():
        nonlocal  _recent_epochs_to_track
        lowest_val_loss = 1.0
        for epoch_end_info in _recent_epochs_to_track.get_last_n(RECENT_EPOCHS_BUFFER):
            _, _, _, logs, model_filepath = epoch_end_info
            val_loss = logs[VAL_LOSS]
            if val_loss < lowest_val_loss:
                lowest_val_loss = val_loss
                return model_filepath
        return None

    def fn_stop_and_clean():
        nonlocal _archive_dir_path

        model_filepath = find_model_filepath_for_lowest_val_loss()
        if model_filepath is None:
            return None

        fn_stop_training()
        move_model_files_from_archive_to_model_data(_archive_dir_path, model_filepath)
        print('over_fitting: save earlier model')


    def move_model_files_from_archive_to_model_data(_archive_dir_path, model_filepath):
        # src_file_path = _archive_dir_path + model_filepath
        model_dir_path = get_abs_path('plugins/' + plugin_name + '/model_data/')
        move_and_override_file(model_filepath + '.h5', model_dir_path, 'model.h5')
        move_and_override_file(model_filepath + '.json', model_dir_path, 'model.json')

    return (fn_check_overfitting)
