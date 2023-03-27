from ..registry import service_registry 
from .whisper import ServiceWhisper

service_registry.register('audio2text', 'whisper', ServiceWhisper)