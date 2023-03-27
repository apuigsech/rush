from ..registry import service_registry 
from .translators import ServiceTranslators

service_registry.register('translate', 'translators', ServiceTranslators)