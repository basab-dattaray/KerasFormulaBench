from common.model.MODEL_MGT_PARAMS import *
from common.model.loss_mgt import *

def overfit_mgr():
    _loss_info = loss_mgr()

    def fn_is_overfitting(info):
        return True

    return fn_is_overfitting
