from ..registry import service_registry 
from .chatgpt import ServiceChatGTP

service_registry.register('nlp', 'chatgpt', ServiceChatGTP)