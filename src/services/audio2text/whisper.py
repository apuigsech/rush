import whisper
from ..base import ServiceBase

class ServiceWhisper(ServiceBase):
    def __init__(self, config=None):
        super().__init__(config)

    def call(self, audio_file):
        wp = whisper.load_model(self.config['model'])
        return wp.transcribe(audio_file)['text']
