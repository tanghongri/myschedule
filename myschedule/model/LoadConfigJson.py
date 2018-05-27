import json
import logging
import os
from string import Template
'''
加载config.jso配置文件

'''
logger = logging.getLogger(__file__)


def LoadJsonFile(filepath, sysconfig):
    if not os.path.exists(filepath):
        logger.error('config.json not exist: '+filepath)
        return
    if not isinstance(sysconfig, dict):
        logger.error('arg sysconfig must be dict')
        return
    try:
        with open(filepath, 'r') as jsonfile:
            configjosn = json.load(jsonfile)
            if not isinstance(sysconfig, dict):
                logger.error('dict: '+configjosn)
                return
            for module in configjosn:
                if not isinstance(configjosn[module], dict):
                    logger.error('dict: '+configjosn[module])
                    return
                for key, value in configjosn[module].items():
                    sysconfig[module+'_' +
                              key] = Template(value).safe_substitute(sysconfig)

    except:
        logger.exception('LoadJsonFile')


if __name__ == '__main__':
    filepath = r'F:\myschedule\config.json'
    sysconfig = {'TEMP_DIR': 'F:\myschedule\temp'}
    LoadJsonFile(filepath, sysconfig)
    print(sysconfig)
