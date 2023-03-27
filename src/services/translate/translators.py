from ..base import ServiceBase

import translators as ts
from nltk.tokenize import sent_tokenize

class ServiceTranslators(ServiceBase):
    gpt = None

    def __init__(self, config=None):
        super().__init__(config)

    def call(self, text="",org='auto', dst='auto', html=False, text_chunks=None):
        response_chunks = []
        for text_chunk in split_text(text, text_chunks):
            print("-")
            if html:
                resp = ts.translate_html(text_chunk, translator=self.config['provider'], from_language=org, to_language=dst,  if_ignore_empty_query=True)
            else:
                resp = ts.translate_text(text_chunk, translator=self.config['provider'], from_language=org, to_language=dst)
            response_chunks.append(resp)
        return ' '.join(response_chunks)


def split_text(text, chunk_size):
    if text is None:
        return ['']
    if chunk_size is None:
        return [text]

    sentences = sent_tokenize(text)

    chunks = []
    current_chunk = ''
    for sentence in sentences:
        if len(current_chunk + sentence) > chunk_size:
            chunks.append(current_chunk.strip())
            current_chunk = ''
        current_chunk += sentence + ' '
    if len(current_chunk) > 0:
        chunks.append(current_chunk.strip())

    return chunks
