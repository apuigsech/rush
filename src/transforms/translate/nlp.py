from ..base import TransformBase

PROMPT_TRANSLATE_DEFAULT = '''
I want you to act as a translator.
Translate the following text into {dst}.
Keep decorators such as markdown or HTML tags.
Write only the translated version of the text, nothing else.

'''


class TransformTranslateNLP(TransformBase):
    def __init__(self, config=None):
        super().__init__(config)
        self.prompt = PROMPT_TRANSLATE_DEFAULT.format(
            org = config['org'],
            dst = config['dst'],
        )
        
    def apply(self, text):
        return self.config['services']['nlp'].call(self.prompt, text, text_chunks=1500)