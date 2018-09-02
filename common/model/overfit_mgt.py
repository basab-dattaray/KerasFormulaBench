from common.model.MODEL_MGT_PARAMS import *
from common.model.loss_mgt import *
from common.misc.RollingBuffer import *
from common.misc.fileops import *
from common.model.model_storage import *

def overfit_mgr(fn_stop_training, model, plugin_name):
    _loss_info = loss_mgr()
    _recent_epochs_to_track = RollingBuffer(RECENT_EPOCHS_BUFFER)
    fn_loss_direction = loss_mgr()

    def save_model_in_archive():
        nonlocal  plugin_name
        dt_now = get_filename_based_on_time()
        model_file_path = get_abs_path('plugins/' + plugin_name + '/model_data/archive/' + dt_now)
        save_model(model_file_path, model)


    def fn_is_overfitting(info):
        iter_num, epoch_num, batch_num, logs = info
        val_loss_direction, changed_val_loss_direction = fn_loss_direction(logs)
        val_loss = logs[VAL_LOSS]
        print('val_loss => {}::    DIRECTION => {} and CHANGED_DIRECTION => {}'.format(val_loss, val_loss_direction, changed_val_loss_direction))

        if val_loss_direction > 0 and changed_val_loss_direction == True:
            _recent_epochs_to_track.reset()
        if val_loss_direction > 0:
            _recent_epochs_to_track.add(info)
            save_model_in_archive()

            if _recent_epochs_to_track.count() > MAX_CONSECUTIVE_LOSS_DEGRATION_COUNT:
                return True

        return False

    # if os.path.exists("demofile.txt"):
    #     os.remove("demofile.txt")



    def fn_stop_and_clean():
        fn_stop_training()
        p = get_abs_path('common/model/archive')


    return (fn_is_overfitting, fn_stop_and_clean)
