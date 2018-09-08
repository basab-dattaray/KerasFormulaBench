def model_mgr(plugin_module, plugin_name):
    fn_setup_model = None # IN: inputs, labels SIDE_EFFECT: save model
    fn_compile_model = None
    fn_predict = None # IN: in_str; OUT: out_str

    def init():
        nonlocal fn_setup_model,  fn_compile_model, fn_predict
        fn_setup_model,  fn_compile_model, fn_predict = \
            plugin_module.model(plugin_name)

    init()

    return (fn_setup_model, fn_compile_model, fn_predict)

