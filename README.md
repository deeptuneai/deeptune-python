# Deeptune Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)
[![pypi](https://img.shields.io/pypi/v/deeptune)](https://pypi.python.org/pypi/deeptune)

The Deeptune Python library provides convenient access to the Deeptune API from Python.

## Installation

```sh
pip install deeptune
```

## Usage

Instantiate and use the client with the following:

```python
from deeptune import play
from deeptune.client import DeeptuneApi

client = DeeptuneApi(
    api_key="YOUR_API_KEY",
)

audio = client.text_to_speech.generate(
    text="Wow, Deeptune's text to speech API is amazing!",
    voice="d770a0d0-d7b0-4e52-962f-1a41d252a5f6",
)
play(audio)
```

## Using Prompt Audio

If you prefer to manage voices on your own, you can use your own audio file as a reference for the voice clone.

### Using a URL prompt

```python
from deeptune import play
from deeptune.client import DeeptuneApi

client = DeeptuneApi(
    api_key="YOUR_API_KEY",
)

audio = client.text_to_speech.generate_from_prompt(
    text="Wow, Deeptune's text to speech API is amazing!",
    prompt_audio="https://deeptune-demo.s3.amazonaws.com/Michael.wav",
)
play(audio)
```

### Using a file prompt

```python
import base64
from deeptune import play
from deeptune.client import DeeptuneApi

client = DeeptuneApi(
    api_key="YOUR_API_KEY",
)

# Open the file and read its contents as bytes
with open("Michael.wav", "rb") as audio_file:
    audio_bytes = audio_file.read()

# Encode the bytes to base64
audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")
audio = client.text_to_speech.generate_from_prompt(
    text="Wow, Deeptune's text to speech API is amazing!",
    prompt_audio=f"data:audio/wav;base64,{audio_base64}",
)
play(audio)
```

## Saving the output

### Saving manually

The `generate` and `generate_from_prompt` endpoints return an iterator of bytes. Make sure to get all of the bytes before writing as demonstrated below.

```python
audio = client.text_to_speech.generate(
    text="Wow, Deeptune's text to speech API is amazing!",
    voice="d770a0d0-d7b0-4e52-962f-1a41d252a5f6",
)
audio_bytes = b"".join(audio)

# Now, you can save however you'd like
with open("output.mp3", "wb") as audio_file:
    audio_file.write(audio_bytes)
```

### Using built in utils

The also has inbuilt `play`, `save`, and `stream` utility methods. Under the hood, these methods use ffmpeg and mpv to play audio streams.

```python
from deeptune import play, save, stream

# plays audio using ffmpeg
play(audio)
# streams audio using mpv
stream(audio)
# saves audio to file
save(audio, "my-file.mp3")
```

## Voices

You can also store and manage voices inside of Deeptune.

```python
# Get all available voices
voices = client.voices.list()
print(voices)

# Get a specific voices
voice = client.voices.get(voice_id="d770a0d0-d7b0-4e52-962f-1a41d252a5f6")
print(voice)

# Create a new cloned voice
voice = client.voices.create(name="Cool Name", file=url_to_file(url))
print(voice)

# Update an existing voice
voice = client.voices.update(
    voice.id,
    name="Updated Name",
    file=,
)

# Delete an existing voice
client.voices.delete(voice.id)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
from deeptune.client import AsyncDeeptuneApi

client = AsyncDeeptuneApi(
    api_key="YOUR_API_KEY",
)
await client.text_to_speech.generate_from_prompt(
    text="string",
    voice="string",
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
