class TransformsRegistry:
    transforms = {}
    def register(self, transform_name, transform_type, transform_class):
        self.transforms[(transform_name, transform_type)] = transform_class
    
    def get(self, transform_name, transform_type):
        return self.transforms.get((transform_name, transform_type), None)

    def list_names(self):
        return list(set(key[0] for key in self.transforms.keys()))


transforms_registry = TransformsRegistry()

def Transform(transform_name, transform_type, transform_config):
    transform_class = transforms_registry.get(transform_name, transform_type)
    if transform_class is None:
        raise ValueError(f"Transform '{transform_name}:{transform_type}' not found")
    return transform_class(transform_config)

def Transforms():
    return transforms_registry.list_names()

from .curate import *
from .summarise import *
from .translate import *

