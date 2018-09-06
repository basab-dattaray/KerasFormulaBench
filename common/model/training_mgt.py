from common.misc.fileops import *
from common.model.training_effort_management import *
from common.generator.data_bender import *

def training_mgr(fn_compile_model, plugin_name, inputs, labels, save_after_n_iterations):

    _model = None
    _stop_running = None
    _x_train = None
    _y_train = None
    _x_val = None
    _y_val = None

    _x_train, _x_val, _y_train, _y_val = data_breaker(inputs, labels)
    _abs_model_path = get_abs_path('plugins/' + plugin_name + '/model_data/model')
    _stop_running = False


    def _fn_stop_training():
        nonlocal _stop_running
        _stop_running = True


    def fn_train_model(total_num_of_iterations, current_iteration, batch_size, num_of_epochs):
        # nonlocal _batch_size, _num_of_epochs
        # nonlocal _model, _abs_model_path
        nonlocal _stop_running
        nonlocal  _x_train, _y_train,  _x_val, _y_val

        # _batch_size = batch_size
        # _num_of_epochs = num_of_epochs

        early_stopping_call_back = TrainingContinuationCallback(_fn_stop_training, _model, plugin_name)

        # print("RANGE:", range(current_iteration, total_num_of_iterations + 1))

        return train_on(_stop_running, _x_train, _x_val, _y_train, _y_val, batch_size, current_iteration, early_stopping_call_back,
                        num_of_epochs, total_num_of_iterations)

    def train_on(_stop_running, _x_train, _x_val, _y_train, _y_val, batch_size, current_iteration, early_stopping_call_back,
                 num_of_epochs, total_num_of_iterations):
        # nonlocal _stop_running
        for iteration in range(current_iteration, total_num_of_iterations + 1):

            if (_stop_running):
                _stop_running = False
                break
                # pass
            print()
            print('-' * 50)
            print('Iteration', iteration)
            _model.fit(_x_train, _y_train,
                       batch_size=batch_size,
                       epochs=num_of_epochs,
                       validation_data=(_x_val, _y_val),
                       callbacks=[early_stopping_call_back],
                       verbose=2)
            if iteration > 0 and iteration % save_after_n_iterations == 0:
                save_model(_abs_model_path, _model)
                print('saved model after {} iterations'.format(iteration))
        save_model(_abs_model_path, _model)
        print('saved model, normal termination')
        return iteration
    return fn_train_model