import logging
import subprocess
from typing import Literal, Union

from dotenv import load_dotenv

from ._prompts import (
       EnglishLecturePrompts,
    EnglishMeetingPrompts,
    JapaneseLecturePrompts,
    JapaneseMeetingPrompts,
    SpanishLecturePrompts,
    SpanishMeetingPrompts,
    UrduLecturePrompts,
    HindiLecturePrompts,
    ArabicLecturePrompts,
    FrenchLecturePrompts,
    GermanLecturePrompts,
    KoreanLecturePrompts,
    BengaliLecturePrompts,
    ChineseLecturePrompts,
    ItalianLecturePrompts,
    RussianLecturePrompts,
    TurkishLecturePrompts,
    PortugueseLecturePrompts,
    UrduMeetingPrompts,
    HindiMeetingPrompts,
    ArabicMeetingPrompts,
    FrenchMeetingPrompts,
    GermanMeetingPrompts,
    KoreanMeetingPrompts,
    BengaliMeetingPrompts,
    ChineseMeetingPrompts,
    ItalianMeetingPrompts,
    RussianMeetingPrompts,
    TurkishMeetingPrompts,
    PortugueseMeetingPrompts,
)
from ._summarizer import Summarizer
from ._transcriber import Transcriber

load_dotenv()

logging.basicConfig(level=logging.INFO)


class MinutesMaker:
    def __init__(
        self,
        model: str = "gpt-3.5-turbo",
        *,
        cpu_threads: int = 0,
        num_workers: int = 1,
    ) -> None:
        """
        Initialize the MinutesMaker class with a Summarizer and
        a Transcriber.

        Parameters
        ----------
        model : str, optional
            The OpenAI model to be used for summarization,
            by default "gpt-3.5-turbo".
        cpu_threads : int, optional
            The number of CPU threads to use for inference,
            by default 0 (auto).
        num_workers : int, optional
            The number of workers to use for inference,
            by default 1 (non-parallel).
        """
        self.__summarizer = Summarizer(model=model)
        self.__transcriber = Transcriber(
            device="cuda" if self.__check_cuda() else "cpu",
            cpu_threads=cpu_threads,
            num_workers=num_workers,
        )

        # Somehow cannot extend the Enum class,
        # we cannot make base class for prompts.
        self.__prompts: Union[
             EnglishLecturePrompts,
    EnglishMeetingPrompts,
    JapaneseLecturePrompts,
    JapaneseMeetingPrompts,
    SpanishLecturePrompts,
    SpanishMeetingPrompts,
    UrduLecturePrompts,
    HindiLecturePrompts,
    ArabicLecturePrompts,
    FrenchLecturePrompts,
    GermanLecturePrompts,
    KoreanLecturePrompts,
    BengaliLecturePrompts,
    ChineseLecturePrompts,
    ItalianLecturePrompts,
    RussianLecturePrompts,
    TurkishLecturePrompts,
    PortugueseLecturePrompts,
    UrduMeetingPrompts,
    HindiMeetingPrompts,
    ArabicMeetingPrompts,
    FrenchMeetingPrompts,
    GermanMeetingPrompts,
    KoreanMeetingPrompts,
    BengaliMeetingPrompts,
    ChineseMeetingPrompts,
    ItalianMeetingPrompts,
    RussianMeetingPrompts,
    TurkishMeetingPrompts,
    PortugueseMeetingPrompts,
        ] = None

    def __call__(
        self,
        audio_or_video_file_path: str,
        language: Literal["ja", "en", "es", "fr", "de", "zh", "hi", "ar", "ru", "pt", "ko", "it", "tr", "bn", "ur"] = "en",
        category: Literal["meeting", "lecture"] = "meeting",
        content: str = "",
        *,
        beam_size: int = 5,
    ) -> tuple[str, str]:
        """
        Transcribe and summarize an audio or video file.

        Parameters
        ----------
        audio_or_video_file_path : str
            The path to the audio or video file to be summarized.
        language : Literal["ja", "en"], optional
            The language of the text to be summarized,
            by default "ja".
        category : Literal["meeting", "lecture"], optional
            The type of the audio to be summarized,
            by default "meeting"
        content : str, optional
            The content of the audio or video file to be summarized.
            e.g. 商品開発, engineering, etc.
            by default "".
        beam_size : int, optional
            The beam size to use for inference,
            by default 5.

        Returns
        -------
        tuple[str, str]
            The transcribed timeline and its summary.
        """
        if language == "ja":
            if category == "meeting":
                self.__prompts = JapaneseMeetingPrompts
            elif category == "lecture":
                self.__prompts = JapaneseLecturePrompts
            else:
                raise ValueError(
                    f"category must be either 'meeting' or 'lecture', but got {category}."
                )
        elif language == "en":
            if category == "meeting":
                self.__prompts = EnglishMeetingPrompts
            elif category == "lecture":
                self.__prompts = EnglishLecturePrompts
            else:
                raise ValueError(
                    f"category must be either 'meeting' or 'lecture', but got {category}."
                )
                
        elif language == "es":
            if category == "meeting":
                self.__prompts = SpanishMeetingPrompts
            elif category == "lecture":
                self.__prompts = SpanishLecturePrompts
            else:
                raise ValueError(f"category must be either 'meeting' or 'lecture', but got {category}.")
        elif language == "fr":
            if category == "meeting":
                self.__prompts = FrenchMeetingPrompts
            elif category == "lecture":
                self.__prompts = FrenchLecturePrompts
            else:
                raise ValueError(f"category must be either 'meeting' or 'lecture', but got {category}.")
        elif language == "de":
            if category == "meeting":
                self.__prompts = GermanMeetingPrompts
            elif category == "lecture":
                self.__prompts = GermanLecturePrompts
            else:
                raise ValueError(f"category must be either 'meeting' or 'lecture', but got {category}.")
        elif language == "zh":
            if category == "meeting":
                self.__prompts = ChineseMeetingPrompts
            elif category == "lecture":
                self.__prompts = ChineseLecturePrompts
            else:
                raise ValueError(f"category must be either 'meeting' or 'lecture', but got {category}.")
        elif language == "hi":
            if category == "meeting":
                self.__prompts = HindiMeetingPrompts
            elif category == "lecture":
                self.__prompts = HindiLecturePrompts
            else:
                raise ValueError(f"category must be either 'meeting' or 'lecture', but got {category}.")
        elif language == "ar":
            if category == "meeting":
                self.__prompts = ArabicMeetingPrompts
            elif category == "lecture":
                self.__prompts = ArabicLecturePrompts
            else:
                raise ValueError(f"category must be either 'meeting' or 'lecture', but got {category}.")
        elif language == "ru":
            if category == "meeting":
                self.__prompts = RussianMeetingPrompts
            elif category == "lecture":
                self.__prompts = RussianLecturePrompts
            else:
                raise ValueError(f"category must be either 'meeting' or 'lecture', but got {category}.")
        elif language == "pt":
            if category == "meeting":
                self.__prompts = PortugueseMeetingPrompts
            elif category == "lecture":
                self.__prompts = PortugueseLecturePrompts
            else:
                raise ValueError(f"category must be either 'meeting' or 'lecture', but got {category}.")
        elif language == "ko":
            if category == "meeting":
                self.__prompts = KoreanMeetingPrompts
            elif category == "lecture":
                self.__prompts = KoreanLecturePrompts
            else:
                raise ValueError(f"category must be either 'meeting' or 'lecture', but got {category}.")
        elif language == "it":
            if category == "meeting":
                self.__prompts = ItalianMeetingPrompts
            elif category == "lecture":
                self.__prompts = ItalianLecturePrompts
            else:
                raise ValueError(f"category must be either 'meeting' or 'lecture', but got {category}.")
        elif language == "tr":
            if category == "meeting":
                self.__prompts = TurkishMeetingPrompts
            elif category == "lecture":
                self.__prompts = TurkishLecturePrompts
            else:
                raise ValueError(f"category must be either 'meeting' or 'lecture', but got {category}.")
        elif language == "bn":
            if category == "meeting":
                self.__prompts = BengaliMeetingPrompts
            elif category == "lecture":
                self.__prompts = BengaliLecturePrompts
            else:
                raise ValueError(f"category must be either 'meeting' or 'lecture', but got {category}.")
        elif language == "ur":
            if category == "meeting":
                self.__prompts = UrduMeetingPrompts
            elif category == "lecture":
                self.__prompts = UrduLecturePrompts
            else:
                raise ValueError(f"category must be either 'meeting' or 'lecture', but got {category}.")
        else:
            raise ValueError(f"Unsupported language: {language}")
     

        results = self.__transcriber.convert_and_transcribe(
            audio_or_video_file_path,
            prompt=self.__prompts.TRANSCRIBE_FORMAT.value.format(content=content),
            beam_size=beam_size,
        ) 
        return results.timeline, self.__summarizer.summarize(
            results.transcript, prompts=self.__prompts
        ), results.chatbot_timeline
        

    def __check_cuda(self) -> bool:
        """
        Check if CUDA is available.
        This method evaluates the output of `nvidia-smi` command.
        If the output contains "NVIDIA-SMI", return True.

        Returns
        -------
        bool
            Whether CUDA is available or not.
        """
        try:
            output = subprocess.check_output("nvidia-smi", shell=True)
            if "NVIDIA-SMI" in output.decode("utf-8"):
                return True
            else:
                return False
        except Exception:
            return False
