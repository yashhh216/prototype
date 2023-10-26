import requests

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/Yko7PKHZNXotIFUBG7I9/stream"

headers = {
"Accept": "audio/mpeg",
"Content-Type": "application/json",
"xi-api-key": "8826b2137958be68b307bfcc8cbb5e16"
}

data = {
"text": 'Hello there ms dhoni is the goat of all time',
"model_id": "eleven_monolingual_v1",
"voice_settings": {
    "stability": 0.6,
    "similarity_boost": 0.5
}
}

response = requests.post(url, json=data, headers=headers, stream=True)

with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
