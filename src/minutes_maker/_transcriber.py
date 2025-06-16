import logging
from dataclasses import dataclass
from typing import Literal
import assemblyai as aai
import datetime
from pydub import AudioSegment
import os
from dotenv import load_dotenv


@dataclass(frozen=True)
class TranscribeData:
    timeline: str
    transcript: str
    chatbot_timeline: str

load_dotenv()

aai.settings.api_key = os.getenv('ASSEMBLYAI_API_KEY')

def ms_to_srt_time(ms: int) -> str:
    """
    Convert milliseconds to SRT-style timestamp: HH:MM:SS,mmm
    """
    td = datetime.timedelta(milliseconds=ms)
    total_seconds = td.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def transcribe_with_srt(audio_path: str):
    """
    Transcribe audio with AssemblyAI, then write SRT with sentence timestamps.
    """
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_path)
    timelines = []
    transcripts = []
    chatbot_timelines = []

    if transcript.status == aai.TranscriptStatus.error:
        raise RuntimeError(f"Transcription failed: {transcript.error}")

    sentences = transcript.get_sentences()

    for idx, sent in enumerate(sentences, start=1):
        start_ts = ms_to_srt_time(sent.start)
        end_ts = ms_to_srt_time(sent.end)
        timelines.append(f"{start_ts} --> {end_ts}  **{sent.text.strip()}**")
        transcripts.append(sent.text.strip())
        chatbot_timelines.append(f"{start_ts}-->{end_ts}*{sent.text.strip()}*")
         
    return timelines, transcripts, chatbot_timelines



class Transcriber:
    def __init__(
        self,
        device: Literal["cpu", "cuda"] = "cuda",
        *,
        cpu_threads: int = 7,
        num_workers: int = 1,
    ) -> None:
        """ 
        Initialize the transcriber.

        Parameters
        ----------
        device : str, optional
            The device to use for inference, by default 'cuda'.
        cpu_threads : int, optional
            The number of CPU threads to use for inference,
            by default 0 (auto).
        num_workers : int, optional
            The number of workers to use for inference,
            by default 1 (non-parallel).
        """


    def convert_and_transcribe(
        self,
        audio_or_video_file_path: str,
        *,
        prompt: str = "",
        beam_size: int = 5,
    ) -> TranscribeData:
        """
        Transcribe an audio or video file.

        Parameters
        ----------
        audio_or_video_file_path : str
            The path to the video or audio file.
        prompt : str, optional
            The initial prompt to make the model easier to understand
            the context, by default "".
        beam_size : int, optional
            The beam size to use for beam search, by default 5.

        Returns
        -------
        TranscribeData
            The transcribed text and the timeline of the audio file.
        """
        # Extract or convert audio from input file if it is a .mp3 file
        audio_file_path = self.__convert_to_audio(audio_or_video_file_path)

        # Transcribe the audio file
        return self.__transcribe(
            audio_file_path=audio_file_path, prompt=prompt, beam_size=beam_size
        )

    def __transcribe(
        self,
        audio_file_path: str,
        *,
        prompt: str = "",
        beam_size: int = 5,
    ) -> TranscribeData:
        """
        Transcribe an audio file.

        Parameters
        ----------
        audio_file_path : str
            The path to the audio file.
        prompt : str, optional
            The initial prompt to make the model easier to understand
            the context, by default "".

        Returns
        -------
        TranscribeData
            The transcribed text and the timeline of the audio file.
        """

        transcripts: list[str] = []
        timelines: list[str] = []
        chatbot_timelines: list[str] = []
        


        timelines, transcripts, chatbot_timelines = transcribe_with_srt(audio_file_path)
        text = "\n\n".join(timelines)
        audio_file_path_text_file = audio_file_path.split('/')[0] +'.txt'
        with open(audio_file_path_text_file, "w", encoding="utf-8") as f:
            f.write(text) 
        print(f'saved to {audio_file_path_text_file}')
        

        return TranscribeData(
            timeline="\n\n".join(timelines), transcript="\n".join(transcripts), chatbot_timeline= "--".join(chatbot_timelines)
        )
        

    def __convert_to_audio(self, audio_or_video_file_path: str) -> str:
        """
        Extract audio from a video file and save it as an mp3 file.

        Parameters
        ----------
        audio_or_video_file_path : str
            The path to the video or audio file.

        Returns
        -------
        str
            The path to the output mp3 file.
        """
        audio = AudioSegment.from_file(audio_or_video_file_path)
        audio_file_path = audio_or_video_file_path.rsplit(".", 1)[0] + ".mp3"
        audio.export(audio_file_path, format="mp3")

        return audio_file_path
