from ..registry import transforms_registry 
from .nlp import TransformSummariseNLP

transforms_registry.register('summarise', 'nlp', TransformSummariseNLP)