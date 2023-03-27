from ..registry import transforms_registry 
from .htmlclean import TransformHTMLClean

transforms_registry.register('htmlclean', '', TransformHTMLClean)