import whisper
import openai
from chatgpt_wrapper import ChatGPT
from google.cloud import translate


from nltk.tokenize import sent_tokenize

class ServiceBase:
	def __init__(self, config=None):
		self.config = config
		pass

class ServiceWhisper(ServiceBase):
    def __init__(self, config=None):
        super().__init__(config)
    
    def call(self, audio_file):
        wp = whisper.load_model(self.config['model'])
        return wp.transcribe(audio_file)['text']

class ServiceChatGTP(ServiceBase):
    gpt = None

    def __init__(self, config=None):
        super().__init__(config)
        if ServiceChatGTP.gpt == None:
            ServiceChatGTP.gpt = ChatGPT()

    def _request(self, prompt):
        return ServiceChatGTP.gpt.ask(prompt)

    def call(self, prompt, text=None, text_chunks=None):
        response_chunks = []
        for text_chunk in split_text(text, text_chunks):
            resp = self._request(f'{prompt}\n{text_chunk}')
            response_chunks.append(resp)
        return ' '.join(response_chunks)


class ServiceTranslateGCP(ServiceBase):
    def __init__(self, config=None):
        super().__init__(config)
        self.client = translate.TranslationServiceClient()
        self.project_id = config['project-id']
        self.location = config['location']
        self.parent = f"projects/{self.project_id}/locations/{self.location}"

    def detect_language(self, text, mime_type="text/plain"):
        response = self.client.detect_language(
            content=text,
            parent=self.parent,
            mime_type=mime_type,
        )

        if response.languages[0].language_code == "und":
            response.languages[0].language_code = None

        return response.languages[0].language_code    

    def call(self, text, org=None, dst=None, text_chunks=None):
        if org is None:
            org = self.detect_language(text, mime_type)
        if org is None:
            return text

        response_chunks = []
        for text_chunk in split_text(text, text_chunks):
            print(len(text_chunk))
            response = self.client.translate_text(
                request={
                    "parent": self.parent,
                    "contents": [text_chunk],
                    "mime_type": "text/html",
                    "source_language_code": org,
                    "target_language_code": dst,
                })
            response_chunks.append(response.translations[0].translated_text)
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


RESOLV = {
    'audio2text': {
        'whisper': ServiceWhisper
    },
    'nlp': {
        'chatgpt': ServiceChatGTP
        # 'gpt': ServiceGTP,
        # 'textblow': ServiceTextBlow
    },
    'translate': {
        'gcp': ServiceTranslateGCP
    }
}

def Service(type, name, config=None):
    return RESOLV[type][name](config)