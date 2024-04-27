import os
import json
from . import log

default_data = '''{\n
    "host": "0.0.0.0",\n
    "port": 8080,\n
    "name": "GeekBlog"\n
}'''

def get_config(path):
    json_file_path = path+'/'+'settings.json'
    if not os.path.exists(json_file_path):
        with open(json_file_path, 'w') as json_file:
            json.dump(default_data, json_file)
    else:
        with open(json_file_path, 'r') as json_file:
            try:
                data = json.load(json_file)
            except json.decoder.JSONDecodeError as e:
                log.error(f"JSON解析错误: {str(e)}")
                data = default_data
                
            if 'name' not in data:
                log.warning("配置文件中缺少'name'字段，使用默认值。")
                data['name'] = default_data['name']

            if 'port' not in data:
                log.warning("配置文件中缺少'port'字段，使用默认值。")
                data['port'] = default_data['port']

            if 'host' not in data:
                log.warning("配置文件中缺少'host'字段，使用默认值。")
                data['host'] = default_data['host']

def get_config_port(path):
    json_file_path = path+'/'+'settings.json'
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        return data.get('port', 0)

def get_config_host(path):
    json_file_path = path+'/'+'settings.json'
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        return data.get('host', 0)

def get_config_name(path):
    json_file_path = path+'/'+'settings.json'
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        return data.get('name', 0)