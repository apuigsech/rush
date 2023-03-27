
class ServicesRegistry:
    services = {}
    def register(self, service_type, service_name, service_class):
        self.services[(service_type, service_name)] = service_class
    
    def get(self, service_type, service_name):
        return self.services.get((service_type, service_name), None)

service_registry = ServicesRegistry()

def Service(service_type, service_name, service_config):
    service_class = service_registry.get(service_type, service_name)
    if service_class is None:
        raise ValueError(f"Service '{service_type}:{service_name}' not found")
    return service_class(service_config)

from .audio2text import *
from .nlp import *
from .translate import *