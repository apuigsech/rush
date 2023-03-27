import tempfile
import requests
import re

from bs4 import BeautifulSoup as soup
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

class InputBase:
	def __init__(self, config=None, required_services=[]):
		for service in required_services:
			if service not in config['services']:
				raise ValueError(f"Missing service: {service}")
		self.config = config


class InputYoutube(InputBase):
	def __init__(self, config=None):
		if ['transcript' in config and config['transcript'] == True]:
			super().__init__(config, [])
		else:
			super().__init__(config, ['audio2text'])

	def get_text_transcript(self, input_url):
		pattern = r'(?<=v=)[\w-]+'
		print(input_url)
		match = re.search(pattern, input_url)
		if match:
			video_id = match.group()
			text = ''
			for t in YouTubeTranscriptApi.get_transcript(video_id):
				text = f'{text} {t["text"]}'
			return text
		else:
			return None
		
	def get_text(self, input_url):
		if ['transcript' in self.config and self.config['transcript'] == True]:
			return self.get_text_transcript(input_url)

		audio_file = tempfile.NamedTemporaryFile(prefix='audio_').name

		audio = YouTube(input_url).streams \
				.filter(only_audio=True) \
				.order_by('abr').last() \
				.download(filename=audio_file)
				
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


RESOLV_INPUT = {
	'youtube': InputYoutube,
	'html': InputHTML
}

def Input(input_url, config):
    for i in config['inputs']:
        if i in input_url:
            input_config = config['inputs'][i]

    return(RESOLV_INPUT[input_config['type']](input_config))
