import os


from common.model.model_storage import load_model, save_model

DATA_PATH = "data/"
DATA_MODEL = DATA_PATH + "model"
DATA_MODEL1 = DATA_PATH + "model1"
JSON_FILE = DATA_PATH + 'model.json'
JSON_FILE1 = DATA_PATH + 'model1.json'
H5_FILE = DATA_PATH + 'model.h5'
H5_FILE1 = DATA_PATH + 'model1.h5'

def test_load_and_test_model():
    if os.path.exists(JSON_FILE1):
        os.remove(JSON_FILE1)
    if os.path.exists(H5_FILE1):
        os.remove(H5_FILE1)

    model_path = os.path.abspath(DATA_MODEL)
    model = load_model(model_path)

    model_path1 = os.path.abspath(DATA_MODEL1)
    save_model(model_path1, model)

    assert os.path.getsize(JSON_FILE) == os.path.getsize(JSON_FILE1)
    assert os.path.getsize(H5_FILE) == os.path.getsize(H5_FILE1)
