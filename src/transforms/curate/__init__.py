from ..registry import transforms_registry 
from .nlp import TransformCurateNLP

transforms_registry.register('curate', 'nlp', TransformCurateNLP)