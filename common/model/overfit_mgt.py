from common.model.MODEL_MGT_PARAMS import *
from common.model.loss_mgt import *
from common.misc.RollingBuffer import *

def overfit_mgr():
    _loss_info = loss_mgr()
    _recent_epochs_to_track = RollingBuffer(RECENT_EPOCHS_BUFFER)
    fn_loss_direction = loss_mgr()

    def fn_is_overfitting(info):
        iter_num, epoch_num, batch_num, logs = info
        val_loss_direction, changed_val_loss_direction = fn_loss_direction(logs)
        val_loss = logs[VAL_LOSS]
        print('val_loss => {}::    DIRECTION => {} and CHANGED_DIRECTION => {}'.format(val_loss, val_loss_direction, changed_val_loss_direction))

        if val_loss_direction > 0 and changed_val_loss_direction == True:
            _recent_epochs_to_track.reset()
        if val_loss_direction > 0:
            _recent_epochs_to_track.add(info)
            if _recent_epochs_to_track.count() > MAX_CONSECUTIVE_LOSS_DEGRATION_COUNT:
                return True
        return False

    return fn_is_overfitting
