from .nlp import *
from bs4 import BeautifulSoup as soup
import markdownify


class TransformBase:
	def __init__(self, config=None):
		self.config = config
		pass


class TransformCurateNLP(TransformBase):
    def __init__(self, config=None):
        super().__init__(config)
        #self.prompt = 'Correct the synatx and semantics of the folling text. Keep the new text as similar as possible than the original one. Write only the new text.'
        self.prompt = PROMPT_CURATE_DEFAULT
        
    def apply(self, text):
        return self.config['services']['nlp'].call(self.prompt, text, text_chunks=2000)


class TransformTranslateNLP(TransformBase):
    def __init__(self, config=None):
        super().__init__(config)
        self.prompt = PROMPT_TRANSLATE_DEFAULT.format(
            org = config['org'],
            dst = config['dst'],
        )

    def apply(self, text):
        return self.config['services']['nlp'].call(self.prompt, text, text_chunks=2000)    


class TransformTranslate(TransformBase):
    def __init__(self, config=None):
        super().__init__(config)
        self.prompt = PROMPT_TRANSLATE_DEFAULT.format(
            org = config['org'],
            dst = config['dst'],   
        )

    def apply(self, text):
        return self.config['services']['translate'].call(self.prompt, text, text_chunks=2000)


class TransformSummarizeNLP(TransformBase):
    def __init__(self, config=None):
        super().__init__(config)
        self.prompt = PROMPT_SUMMARIZE_TWITTER

    def apply(self, text):
        return self.config['services']['nlp'].call(self.prompt, text)


class TransformHTMLClean(TransformBase):
    def __init__(self, config=None):
        super().__init__(config)

    def apply(self, text):
        html = soup(text, 'html.parser')
        for tag in self.config['tags']:
            for item in html.find_all(tag):
                item.replaceWith(item.text)
        return(str(html)) 


class TransformHTML2Markdown(TransformBase):
    def __init__(self, config=None):
        super().__init__(config)

    def apply(self, text):
        return markdownify.markdownify(text, heading_style="ATX_CLOSED")



RESOLV = {
    'curate': {
        'nlp': TransformCurateNLP
    },
    'translate': {
        'translate': TransformTranslate,
        'nlp': TransformTranslateNLP
    },
    'summarize': {
        'nlp': TransformSummarizeNLP
    },
    'htmlclean': TransformHTMLClean,
    'html2markdown': TransformHTML2Markdown
}

def Transform(name, config=None):
    if 'type' in config:
        type = config['type']
        return RESOLV[name][type](config)
    else:
        return RESOLV[name](config)
