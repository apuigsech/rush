from ..base import TransformBase

PROMPT_CURATE_DEFAULT = 'Correct the synatx and semantics of the folling text. Keep the new text as similar as possible than the original one. Write only the new text.'

class TransformCurateNLP(TransformBase):
    def __init__(self, config=None):
        super().__init__(config)
        self.prompt = PROMPT_CURATE_DEFAULT
        
    def apply(self, text):
        return self.config['services']['nlp'].call(self.prompt, text, text_chunks=2000)