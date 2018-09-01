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