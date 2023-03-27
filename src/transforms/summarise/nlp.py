from ..base import TransformBase

PROMPT_SUMMARISE_DEFAULT = '''
Summarise the following text.
Write only the new text.
'''

PROMPT_SUMMARISE_TWITTER = '''
I will provide you with a text, and I want you to summarize it following the rules I list below:
- The summary should be concise and capture the main points and arguments of the text.
- The summary should be in the form of tweets composing a Twitter thread.
- Enumerate all tweets using a numeric list.
- There will be between 5 and 10 tweets.
- The first, and only the first, tweet must contain relevant hashtags.
- Replace all well-known names with their Twitter id.
- The summary should be in the same language as the original text.
'''

PROMPT_STYLES = {
    'default': PROMPT_SUMMARISE_DEFAULT,
    'twitter': PROMPT_SUMMARISE_TWITTER,
}

class TransformSummariseNLP(TransformBase):
    def __init__(self, config=None):
        super().__init__(config)
        self.prompt = PROMPT_STYLES[config.get('style', 'default')]
        
    def apply(self, text):
        return self.config['services']['nlp'].call(self.prompt, text, text_chunks=2000)