from keras.callbacks import Callback
#
# from common.misc.RollingBuffer import *

from common.model.overfit_mgt import *


class TrainingContinuationCallback(Callback):


    def __init__(self, fn_stop_training, model, plugin_name):
        super(Callback, self).__init__()

        self._train_iteration = 0
        self._batch = -1
        self._epoch = -1
        self.fn_check_overfitting = overfit_mgr(fn_stop_training, model, plugin_name)


    def on_epoch_begin(self, epoch, logs):
        self._epoch = epoch

    def on_epoch_end(self, epoch, logs):
        self.fn_check_overfitting(self._train_iteration, self._epoch, self._batch, logs)



    def on_batch_begin(self, batch, logs):
        self._batch = batch

    def on_batch_end(self, batch, logs):
        pass

    def on_train_begin(self, logs):
        self._train_iteration += 1

    def on_train_end(self, logs):
        pass

        # x = self._recent_epochs_to_track.get_last_n(12)
        #
        # x = None

