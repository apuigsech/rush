
PROMPT_CURATE_DEFAULT = '''
I will provide you with a text, and I want you to correct it following the rules I list bellow:
- This request and the text may be on different language. Your response should be on the same languaje than the text.
'''

PROMPT_TRANSLATE_DEFAULT = '''
Tanstalet the following text form {org} to {dst}. Write only the new text.
'''

PROMPT_SUMMARIZE_DEFAULT = '''
Summarise the following text.
Write only the new text.
'''

PROMPT_SUMMARIZE_TWITTER = '''
I will provide you with a text, and I want you to summarize it following the rules I list below:
- The summary should be concise and capture the main points and arguments of the text.
- The summary should be in the form of tweets composing a Twitter thread.
- Enumerate all tweets using a numeric list.
- There will be between 5 and 10 tweets.
- The first, and only the first, tweet must contain relevant hashtags.
- Replace all well-known names with their Twitter id.
- The summary should be in the same language as the original text.
'''

RESOLV = {
    'curate': {
        'default': PROMPT_CURATE_DEFAULT
    },
    'traslate': {
        'default': PROMPT_TRANSLATE_DEFAULT
    },
    'summarize': {
        'default': PROMPT_SUMMARIZE_DEFAULT,
        'twitter': PROMPT_SUMMARIZE_TWITTER
    }
}
