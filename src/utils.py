import re
from configobj import ConfigObj, Section

from services import Service

def config_overlay(config, keys, value):
    keys = keys.split('.')
    last_key = keys.pop()

    sub_config = config
    for key in keys:
        if key not in sub_config:
            break
        sub_config = sub_config[key]

    sub_config[last_key] = value

    return config


def config_resolv(config):
    config['input'] = config_resolv_services(config['inputs'], config['services'])
    config['transforms'] = config_resolv_services(config['transforms'], config['services'])
    return config


def config_resolv_services(config, services_config={}):
    for key in config:
        if type(config[key]) == Section:
            config_resolv_services(config[key], services_config)
        else:
            if key == 'services':
                pattern = r',\s*(?![^()]*\))'
                print(key, config[key])
                services_list = re.split(pattern, config[key])
                config['services'] = {}
                for service in services_list:
                    (service_type, service_name, local_service_config) = config_service_parse(service)  
                    service_config = services_config[service_type][service_name]
                    for key, value in local_service_config.items():
                        service_config[key] = value
                    config['services'][service_type] = Service(service_type, service_name, service_config)
    return config


def config_service_parse(service):
    pattern = r'^(\w+)\.(\w+)(?:\((.*)\))?$'
    match = re.match(pattern, service)
    if match:
        service_type, service_name, service_config_str = match.groups()
        service_config = {}
        if service_config_str:
            for c in service_config_str.split(','):
                c = c.strip()
                if '=' in c:
                    key, value = c.split('=', 1)
                    service_config[key.strip()] = value.strip()
                else:
                    service_config[p] = 'true'
        return service_type, service_name, service_config
    else:
        return None