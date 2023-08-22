# getYaml
import yaml
import os
from utils.handle_path import GetPath
def get_yaml_data(yml):
    with open(yml,encoding='utf-8') as f:
        data = yaml.safe_load(f.read())
    return data

if __name__ == '__main__':
    data = get_yaml_data(GetPath.data_path/'data_login.yaml')
    print(data)

