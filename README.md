# Rush

Rush is a Python information processing tool. It takes TEXT information from different sources, including video transcription, and transforms into new information in different ways, such as summarizing the content, translating the text to different languages, or even composing a Twitter thread.

In an increasingly content-saturated world, it's essential to focus our efforts on consuming content that adds value. Selecting the right content can be a daunting task, but Rush streamlines the process and makes it more efficient than ever before. With Rush, you can spend less time sifting through irrelevant content and more time engaging with the content that matters to you.


## Installation

To use Rush, you need to have Python 3 installed on your system. You also need to install the required Python packages, which are listed in the `requirements.txt` file. You can install these packages by running the following command:

pip install -r requirements.txt
pip install git+https://github.com/mmabrouk/chatgpt-wrapper


## Usage

python src/main.py -i 'https://www.youtube.com/watch?v=7AZi3twcYdI' --co transforms.summarize.style twitter -t curate -t summarize