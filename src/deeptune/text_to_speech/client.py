# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TextToSpeechClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def generate(
        self,
        *,
        text: str,
        voice: str,
        language_code: typing.Optional[str] = OMIT,
        seed: typing.Optional[int] = OMIT,
        output_format: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        The official Python API for Deeptune. Deeptune brings the most human-like text to speech and voice cloning technology to your project in only a few lines of code.

        Parameters
        ----------
        text : str
            The text to be converted to speech.

        voice : str
            Voice ID to be used, you can use the API or https://app.deeptune.com to browse voices and clone your own.

        language_code : typing.Optional[str]
            Language code used to specify language/accent for the model, see supported languages. If not specified, language is auto-detected.

        seed : typing.Optional[int]
            Assuming all other properties didn't change, a fixed seed should always generate the exact same audio file.

        output_format : typing.Optional[str]
            Output audio format. Must be one of the following:
            * `mp3_44100_192` - MP3 with 44.1kHz sample rate at 192kbps
            * `mp3_44100_128` - MP3 with 44.1kHz sample rate at 128kbps
            * `mp3_44100_96` - MP3 with 44.1kHz sample rate at 96kbps
            * `mp3_44100_64` - MP3 with 44.1kHz sample rate at 64kbps
            * `mp3_44100_32` - MP3 with 44.1kHz sample rate at 32kbps
            * `mp3_22050_32` - MP3 with 22.05kHz sample rate at 32kbps
            * `wav_44100` - WAV with 44.1kHz sample rate
            * `wav_24000` - WAV with 24kHz sample rate
            * `wav_22050` - WAV with 22.05kHz sample rate
            * `wav_16000` - WAV with 16kHz sample rate


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[bytes]
            Successful response

        Examples
        --------
        from deeptune.client import Deeptune

        client = Deeptune(
            api_key="YOUR_API_KEY",
        )
        client.text_to_speech.generate(
            text="string",
            voice="string",
            language_code="string",
            seed=1,
            output_format="string",
        )
        """
        with self._client_wrapper.httpx_client.stream(
            "v1/text-to-speech",
            method="POST",
            json={
                "text": text,
                "voice": voice,
                "language_code": language_code,
                "seed": seed,
                "output_format": output_format,
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:
            try:
                if 200 <= _response.status_code < 300:
                    for _chunk in _response.iter_bytes():
                        yield _chunk
                    return
                _response.read()
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)

    def generate_from_prompt(
        self,
        *,
        text: str,
        prompt_audio: str,
        language_code: typing.Optional[str] = OMIT,
        seed: typing.Optional[int] = OMIT,
        output_format: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        If you prefer to manage voices on your own, you can use your own audio file as a reference for the voice clone.

        Parameters
        ----------
        text : str
            The text to be converted to speech.

        prompt_audio : str
            The audio of the voice prompt to clone. This can be the url of a publicly accessible audio file or base64 encoded byte string.

            The audio file should have a duration ranging from 3 to 30 seconds (quality does not improve with more than 30 seconds of reference audio). It can be in any audio format, as long as it is less than 50 MB.


        language_code : typing.Optional[str]
            Language code used to specify language/accent for the model, see supported languages. If not specified, language is auto-detected.

        seed : typing.Optional[int]
            Assuming all other properties didn't change, a fixed seed should always generate the exact same audio file.

        output_format : typing.Optional[str]
            Output audio format. Must be one of the following:
            * `mp3_44100_192` - MP3 with 44.1kHz sample rate at 192kbps
            * `mp3_44100_128` - MP3 with 44.1kHz sample rate at 128kbps
            * `mp3_44100_96` - MP3 with 44.1kHz sample rate at 96kbps
            * `mp3_44100_64` - MP3 with 44.1kHz sample rate at 64kbps
            * `mp3_44100_32` - MP3 with 44.1kHz sample rate at 32kbps
            * `mp3_22050_32` - MP3 with 22.05kHz sample rate at 32kbps
            * `wav_44100` - WAV with 44.1kHz sample rate
            * `wav_24000` - WAV with 24kHz sample rate
            * `wav_22050` - WAV with 22.05kHz sample rate
            * `wav_16000` - WAV with 16kHz sample rate


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[bytes]
            Successful response

        Examples
        --------
        from deeptune.client import Deeptune

        client = Deeptune(
            api_key="YOUR_API_KEY",
        )
        client.text_to_speech.generate_from_prompt(
            text="string",
            prompt_audio="string",
            language_code="string",
            seed=1,
            output_format="string",
        )
        """
        with self._client_wrapper.httpx_client.stream(
            "v1/text-to-speech/from-prompt",
            method="POST",
            json={
                "text": text,
                "prompt_audio": prompt_audio,
                "language_code": language_code,
                "seed": seed,
                "output_format": output_format,
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:
            try:
                if 200 <= _response.status_code < 300:
                    for _chunk in _response.iter_bytes():
                        yield _chunk
                    return
                _response.read()
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTextToSpeechClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def generate(
        self,
        *,
        text: str,
        voice: str,
        language_code: typing.Optional[str] = OMIT,
        seed: typing.Optional[int] = OMIT,
        output_format: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        The official Python API for Deeptune. Deeptune brings the most human-like text to speech and voice cloning technology to your project in only a few lines of code.

        Parameters
        ----------
        text : str
            The text to be converted to speech.

        voice : str
            Voice ID to be used, you can use the API or https://app.deeptune.com to browse voices and clone your own.

        language_code : typing.Optional[str]
            Language code used to specify language/accent for the model, see supported languages. If not specified, language is auto-detected.

        seed : typing.Optional[int]
            Assuming all other properties didn't change, a fixed seed should always generate the exact same audio file.

        output_format : typing.Optional[str]
            Output audio format. Must be one of the following:
            * `mp3_44100_192` - MP3 with 44.1kHz sample rate at 192kbps
            * `mp3_44100_128` - MP3 with 44.1kHz sample rate at 128kbps
            * `mp3_44100_96` - MP3 with 44.1kHz sample rate at 96kbps
            * `mp3_44100_64` - MP3 with 44.1kHz sample rate at 64kbps
            * `mp3_44100_32` - MP3 with 44.1kHz sample rate at 32kbps
            * `mp3_22050_32` - MP3 with 22.05kHz sample rate at 32kbps
            * `wav_44100` - WAV with 44.1kHz sample rate
            * `wav_24000` - WAV with 24kHz sample rate
            * `wav_22050` - WAV with 22.05kHz sample rate
            * `wav_16000` - WAV with 16kHz sample rate


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[bytes]
            Successful response

        Examples
        --------
        from deeptune.client import AsyncDeeptune

        client = AsyncDeeptune(
            api_key="YOUR_API_KEY",
        )
        await client.text_to_speech.generate(
            text="string",
            voice="string",
            language_code="string",
            seed=1,
            output_format="string",
        )
        """
        async with self._client_wrapper.httpx_client.stream(
            "v1/text-to-speech",
            method="POST",
            json={
                "text": text,
                "voice": voice,
                "language_code": language_code,
                "seed": seed,
                "output_format": output_format,
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:
            try:
                if 200 <= _response.status_code < 300:
                    async for _chunk in _response.aiter_bytes():
                        yield _chunk
                    return
                await _response.aread()
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)

    async def generate_from_prompt(
        self,
        *,
        text: str,
        prompt_audio: str,
        language_code: typing.Optional[str] = OMIT,
        seed: typing.Optional[int] = OMIT,
        output_format: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        If you prefer to manage voices on your own, you can use your own audio file as a reference for the voice clone.

        Parameters
        ----------
        text : str
            The text to be converted to speech.

        prompt_audio : str
            The audio of the voice prompt to clone. This can be the url of a publicly accessible audio file or base64 encoded byte string.

            The audio file should have a duration ranging from 3 to 30 seconds (quality does not improve with more than 30 seconds of reference audio). It can be in any audio format, as long as it is less than 50 MB.


        language_code : typing.Optional[str]
            Language code used to specify language/accent for the model, see supported languages. If not specified, language is auto-detected.

        seed : typing.Optional[int]
            Assuming all other properties didn't change, a fixed seed should always generate the exact same audio file.

        output_format : typing.Optional[str]
            Output audio format. Must be one of the following:
            * `mp3_44100_192` - MP3 with 44.1kHz sample rate at 192kbps
            * `mp3_44100_128` - MP3 with 44.1kHz sample rate at 128kbps
            * `mp3_44100_96` - MP3 with 44.1kHz sample rate at 96kbps
            * `mp3_44100_64` - MP3 with 44.1kHz sample rate at 64kbps
            * `mp3_44100_32` - MP3 with 44.1kHz sample rate at 32kbps
            * `mp3_22050_32` - MP3 with 22.05kHz sample rate at 32kbps
            * `wav_44100` - WAV with 44.1kHz sample rate
            * `wav_24000` - WAV with 24kHz sample rate
            * `wav_22050` - WAV with 22.05kHz sample rate
            * `wav_16000` - WAV with 16kHz sample rate


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[bytes]
            Successful response

        Examples
        --------
        from deeptune.client import AsyncDeeptune

        client = AsyncDeeptune(
            api_key="YOUR_API_KEY",
        )
        await client.text_to_speech.generate_from_prompt(
            text="string",
            prompt_audio="string",
            language_code="string",
            seed=1,
            output_format="string",
        )
        """
        async with self._client_wrapper.httpx_client.stream(
            "v1/text-to-speech/from-prompt",
            method="POST",
            json={
                "text": text,
                "prompt_audio": prompt_audio,
                "language_code": language_code,
                "seed": seed,
                "output_format": output_format,
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:
            try:
                if 200 <= _response.status_code < 300:
                    async for _chunk in _response.aiter_bytes():
                        yield _chunk
                    return
                await _response.aread()
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)
