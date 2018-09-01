from keras.callbacks import Callback

from common.misc.RollingBuffer import *

from common.model.loss_mgt import *


class TrainingContinuationCallback(Callback):


    def __init__(self, fn_stop_training, monitor='loss', value=0.01, verbose=0, recent_epochs_buffer_size = 10):
        super(Callback, self).__init__()
        self._monitor = monitor
        self._value = value
        self._verbose = verbose
        self._fn_stop_training = fn_stop_training
        self._train_iteration = 0
        self._batch = -1
        self._epoch = -1
        self._recent_epochs_to_track = RollingBuffer(recent_epochs_buffer_size)
        self.fn_direction = loss_mgr()


    def on_epoch_begin(self, epoch, logs):
        self._epoch = epoch

    def on_epoch_end(self, epoch, logs):
        val_loss_direction, changed_val_loss_direction = self.fn_direction(logs)
        val_loss = logs[VAL_LOSS]
        print('val_loss => {}::    DIRECTION => {} and CHANGED_DIRECTION => {}'.format(val_loss, val_loss_direction, changed_val_loss_direction))

        info = (self._train_iteration, self._epoch, self._batch, logs)

        if val_loss_direction > 0 and changed_val_loss_direction == True:
            self._recent_epochs_to_track.reset()
        if val_loss_direction > 0:
            self._recent_epochs_to_track.add(info)
            if self._recent_epochs_to_track.count() > 1:
                print('epochs tracked = {}'.format(self._recent_epochs_to_track.count()))


    def on_batch_begin(self, batch, logs):
        self._batch = batch

    def on_batch_end(self, batch, logs):
        pass

    def on_train_begin(self, logs):
        self._train_iteration += 1

    def on_train_end(self, logs):

        x = self._recent_epochs_to_track.get_last_n(12)

        x = None

