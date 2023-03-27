import translators as ts

from ..base import TransformBase

class TransformTranslate(TransformBase):
    def __init__(self, config=None):
        super().__init__(config)
        
    def apply(self, text):
        return self.config['services']['translate'].call(text, org=self.config['org'], dst=self.config['dst'], html=True, text_chunks=None)