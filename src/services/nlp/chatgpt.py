from chatgpt_wrapper import ChatGPT
from ..base import ServiceBase

from nltk.tokenize import sent_tokenize

class ServiceChatGTP(ServiceBase):
    gpt = None

    def __init__(self, config=None):
        super().__init__(config)
        if ServiceChatGTP.gpt == None:
            ServiceChatGTP.gpt = ChatGPT()

    def _request(self, prompt):
        return ServiceChatGTP.gpt.ask(prompt)

    def call(self, prompt, text="", text_chunks=None):
        response_chunks = []
        for text_chunk in split_text(text, text_chunks):
            resp = self._request(f'{prompt}\n{text_chunk}')[1]
            resp=text_chunk + "\n\n\n-----\n\n\n" + resp + "\n\n\n============\n\n\n"
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