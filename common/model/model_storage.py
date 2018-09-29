from keras.models import model_from_json
from os.path import exists
from framework.mediation_mgt import *

# from plugins.expr_calc.model_if import compile_model

def is_model_usable(path):
    if not exists(path + '.json'):
        return False
    if not exists(path + '.h5'):
        return False
    # bare_path = path.rspit('model', 2)[0]
    return True

def save_model(path, model):
    # serialize model to JSON

    base_folder = path.rsplit('/', 1)[0]
    path = get_abs_path(path)
    base_folder = get_abs_path(base_folder)
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)

    model_json = model.to_json()
    with open(path + ".json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights(path + ".h5")
    # print("Saved model to disk")


def load_model(path):
    # load json and create model
    json_file = open(path + '.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(path + ".h5")

    return loaded_model
    # print("Loaded model from disk")

def load_compiled_model():
    plugin_name, fn_get_data, fn_generate_data_given_input_strings, fn_setup_model, fn_compile_model, fn_predict \
        = mediation_mgr()
    abs_model_path = get_abs_path('plugins/' + plugin_name + '/model_data/model')
    model = load_model(abs_model_path)
    fn_compile_model(model)
    return model
