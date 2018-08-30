def model_mgr(plugin_module, num_of_iterations, save_after_n_iterations, num_of_iteration_degradations_for_overfitting):
    fn_setup_model = None # IN: inputs, labels SIDE_EFFECT: save model
    fn_train_model = None # IN: num_of_iterations, Num_of_epochs, num_of_batches, directives_dict; OUT: info_dict;  SIDE_EFFECT: save and load model
    fn_train_on = None # IN: num_of_iterations. directives_dict; OUT: info_dict; SIDE_EFFECT: save and load model
    fn_stop_training = None #
    fn_compile_model = None
    fn_predict = None # IN: in_str; OUT: out_str

    def init():
        nonlocal fn_setup_model, fn_train_model, fn_train_on, fn_stop_training, fn_compile_model, fn_predict
        fn_setup_model, fn_train_model, fn_train_on, fn_stop_training, fn_compile_model, fn_predict = plugin_module.model(num_of_iterations, save_after_n_iterations, num_of_iteration_degradations_for_overfitting)

    init()

    return (fn_setup_model, fn_train_model, fn_train_on, fn_stop_training, fn_compile_model, fn_predict)

