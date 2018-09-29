from common.render.color_ref import *
from common.model.training_callback_mgt import *
from common.generator.data_bender import *

def training_mgr(plugin_name, save_after_n_iterations):

    _stop_running = None


    _abs_model_path = get_abs_path('plugins/' + plugin_name + '/model_data/model')
    _stop_running = False
    _x_train = None
    _x_val = None
    _y_train = None
    _y_val = None

    def _fn_stop_training():
        nonlocal _stop_running
        _stop_running = True


    def fn_train_model(model, inputs, labels, total_num_of_iterations, current_iteration, batch_size, num_of_epochs):
        nonlocal _stop_running
        nonlocal _x_train, _x_val, _y_train, _y_val

        early_stopping_call_back = EarlyStopCallback(_fn_stop_training, model, plugin_name)

        _x_train, _x_val, _y_train, _y_val = data_breaker(inputs, labels)
        # print("RANGE:", range(current_iteration, total_num_of_iterations + 1))

        return train_on(model, batch_size, current_iteration, early_stopping_call_back,
                        num_of_epochs, total_num_of_iterations)

    def train_on(model, batch_size, current_iteration, early_stopping_call_back,
                 num_of_epochs, total_num_of_iterations):
        nonlocal _stop_running
        nonlocal _x_train, _x_val, _y_train, _y_val
        iteration = None
        for iteration in range(current_iteration, total_num_of_iterations + 1):

            if (_stop_running):
                break
                # pass
            print()
            print('-' * 50)
            print('Iteration', iteration)
            model.fit(_x_train, _y_train,
                      batch_size=batch_size,
                      epochs=num_of_epochs,
                      validation_data=(_x_val, _y_val),
                      callbacks=[early_stopping_call_back],
                      verbose=2)
            if iteration > 0 and iteration % save_after_n_iterations == 0:
                save_model(_abs_model_path, model)
                print(colors.blue + 'saved model after {} iterations'.format(iteration) + colors.close, end=' ')

        save_model(_abs_model_path, model)
        if _stop_running == False:
            print(colors.blue + 'saved model, training complete' + colors.close, end=' ')
        else:
            print(colors.blue + 'saved model, regressing due to over fitting so start training afresh' + colors.close, end=' ')
            _stop_running = False


        return iteration
    return fn_train_model