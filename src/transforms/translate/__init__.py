from ..registry import transforms_registry 
from .nlp import TransformTranslateNLP
from .translate import TransformTranslate

transforms_registry.register('translate', 'nlp', TransformTranslateNLP)
transforms_registry.register('translate', 'translate', TransformTranslate)