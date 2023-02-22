import tempfile
import requests

from bs4 import BeautifulSoup as soup

from pytube import YouTube
import whisper

class InputBase:
	def __init__(self, config=None):
		self.config = config
		pass

class InputYoutube(InputBase):
	def __init__(self, config=None):
		super().__init__(config)

	def get_text(self, input_url):
		yt = YouTube(input_url)
		audio = yt.streams.filter(only_audio=True).order_by('abr').last()
		
		audio_file = tempfile.NamedTemporaryFile(prefix='audio_').name
		audio.download(filename=audio_file) 

		return self.config['services']['audio2text'].call(audio_file)


class InputHTML(InputBase):
	def __init__(self, config=None):
		super().__init__(config)
	
	def get_text(self, input_url):
		if 'cookies' not in self.config:
			self.config['cookies'] = None

		r = requests.get(input_url, cookies=self.config['cookies'])
		html = soup(r.content, 'html.parser').select(self.config['query'])[0]
		text = str(html)
		
		return(text)


RESOLV = {
	'youtube': InputYoutube,
	'html': InputHTML
}

def Input(config=None):
    type = config['type']
    return RESOLV[type](config)