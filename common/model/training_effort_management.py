from keras.callbacks import Callback

from common.misc.RollingBuffer import *

VAL_LOSS = 'val_loss'

def loss_mgr():
    _lastrun_logs = None
    _lastrun_direction = None
    def fn_direction(logs):
        nonlocal _lastrun_logs, _lastrun_direction
        if _lastrun_logs == None:
            direction = 0
        else:
            if _lastrun_logs[VAL_LOSS] == logs[VAL_LOSS]:
                direction = 0
            if _lastrun_logs[VAL_LOSS] > logs[VAL_LOSS]:
                direction = -1
            if _lastrun_logs[VAL_LOSS] < logs[VAL_LOSS]:
                direction = 1

        change_direction = True
        if direction is not None and _lastrun_direction is not None:
            if direction == _lastrun_direction:
                change_direction = False
        _lastrun_logs = logs
        _lastrun_direction = direction
        return direction, change_direction
    return fn_direction


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
        self._recent_epochs = RollingBuffer(recent_epochs_buffer_size)
        self.fn_direction = loss_mgr()


    def on_epoch_begin(self, epoch, logs):
        self._epoch = epoch

    def on_epoch_end(self, epoch, logs):
        info = (self._train_iteration, self._epoch, self._batch, logs)
        self._recent_epochs.add(info)
        direction, changed_direction = self.fn_direction(logs)
        val_loss = logs[VAL_LOSS]
        print('val_loss => {}::    DIRECTION => {} and CHANGED_DIRECTION => {}'.format(val_loss, direction, changed_direction))

    def on_batch_begin(self, batch, logs):
        self._batch = batch

    def on_batch_end(self, batch, logs):
        pass

    def on_train_begin(self, logs):
        self._train_iteration += 1

    def on_train_end(self, logs):

        x = self._recent_epochs.get_last_n(12)

        x = None

