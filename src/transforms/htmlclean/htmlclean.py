from ..base import TransformBase

class TransformHTMLClean(TransformBase):
    def __init__(self, config=None):
        super().__init__(config)
        self.prompt = PROMPT_CURATE_DEFAULT
        
    def apply(self, text):
        return self.config['services']['nlp'].call(self.prompt, text, text_chunks=2000)