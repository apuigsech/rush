from service import Service

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


def input_config(input_url, config):
    for i in config['inputs']:
        if i in input_url:
            local_config = config['inputs'][i]

    local_config = load_services(local_config, config)

    return local_config

def transform_config(name, config):
    local_config = config['transforms'][name]
    local_config = load_services(local_config, config)
    return local_config


def load_services(local_config, config):
    services = {}

    if 'services' not in local_config:
        return local_config

    if isinstance(local_config['services'], str):
        local_config['services'] = [local_config['services']]

    for service in local_config['services']:
        service_type, service_name = service.split('.')
        services[service_type] = Service(service_type, service_name, config['services'][service_type][service_name])
    
    local_config['services'] = services

    return local_config
