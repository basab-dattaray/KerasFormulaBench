from common.misc.fileops import *
import  importlib

from plugins.constants import *

PLUGIN_KEY = "plugin_key"

def plugin_mgr():

    _plug_name = None

    GENERATOR_IF = 'generator_if'
    _plugin_module_GENERATOR_IF = None

    MODEL_IF = 'model_if'
    _plugin_module_MODEL_IF = None

    def init():
        nonlocal _plugin_module_GENERATOR_IF
        nonlocal _plugin_module_MODEL_IF
        nonlocal _plug_name
        dict = get_dict_from_json_file('apps' + '/CONFIG.JSON')
        _plug_name = dict[PLUGIN_KEY]
        _plugin_module_GENERATOR_IF = get_plug_module(_plug_name, GENERATOR_IF)
        _plugin_module_MODEL_IF = get_plug_module(_plug_name, MODEL_IF)

    def fn_get_plugin_info():
        nonlocal _plugin_module_GENERATOR_IF
        nonlocal _plugin_module_MODEL_IF
        nonlocal _plug_name
        return (_plug_name, _plugin_module_GENERATOR_IF, _plugin_module_MODEL_IF)

    # def set_plugname(plug_name):
    #     file_path = "common/CONFIG.JSON"
    #     abs_path = get_abs_path(file_path)
    #     dict = {}
    #     with open(abs_path, 'r') as f:
    #         dict = json.load(f)
    #
    #     with open(abs_path, 'w') as f:
    #         try:
    #             dict[PLUGIN_KEY] = plug_name
    #             json.dump(dict, f)
    #             _plug_name = plug_name
    #         except Exception as e:
    #             print(e)

    def get_plug_module(plug_name, module_name):

        PLUGIN_NAME = PLUGINS + '.' + plug_name + '.' + module_name
        plugin = importlib.import_module(PLUGIN_NAME, '.')
        return plugin

    init()

    return  fn_get_plugin_info







