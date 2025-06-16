import inspect
from enum import Enum


class JapaneseMeetingPrompts(Enum):
    """
    Enum for storing prompts for meeting minutes in Japanese.

    Attributes
    ----------
    TRANSCRIBE_FORMAT : str
        The format string for the prompt for transcribing the audio.
        Used in `src/minutes_maker/_transcriber.py`.

    SUMMARIZE_SYSTEM_PROMPT : str
        The system message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SUMMARY : str
        The user message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SHORTENING : str
        The user message for shortening the transcript.
        Used in `src/minutes_maker/_summarizer.py`.
    """

    TRANSCRIBE_FORMAT: str = "{content}に関する、ミーティングの書き起こし。"
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        以下のテキストは、ある日本語の会議の内容を文字起こししたものです。
        文字起こしは機械学習モデルによって行われており、その精度は100%ではありません。
        また、文字起こしの結果には、会議の参加者の発言以外にも、雑音や会議の進行に関する記述が含まれている可能性があります。
        それを踏まえた上で、以下の文字起こしを読み、ユーザーの質問に答えてください。

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        会議の文字起こしの内容から、以下の3点について日本語でまとめてください。
        なお、markdown形式で、重要な点を太字にしたり、タイトル部分を大きくしたりなど、読みやすいように工夫して記述してください。

        ## 1. 会議のサマリ
        ## 2. 会議の決定事項
        ## 3. 会議の結論から考えられるToDoもしくはNext Action
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        この文字起こしは長すぎるため、要点を確実に押さえながら要約してください。
        なお、この文字起こしはより長い文字起こし文の一部切り出したものである可能性があることに注意してください。
        """
    )


class EnglishMeetingPrompts(Enum):
    """
    Enum for storing prompts for meeting minutes in English.

    Attributes
    ----------
    TRANSCRIBE_FORMAT : str
        The format string for the prompt for transcribing the audio.
        Used in `src/minutes_maker/_transcriber.py`.

    SUMMARIZE_SYSTEM_PROMPT : str
        The system message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SUMMARY : str
        The user message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SHORTENING : str
        The user message for shortening the transcript.
        Used in `src/minutes_maker/_summarizer.py`.
    """

    TRANSCRIBE_FORMAT: str = "Transcription of the meeting regarding {content}."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        The following text is a transcription of a meeting in English.
        The transcription is done by a machine learning model, and its accuracy is not 100%.
        Also, the transcription results may include not only the participants' remarks, but also background noise and descriptions of the meeting's progress.
        Bearing this in mind, please read the transcription below and answer the user's question.

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        From the content of the meeting transcription, please summarize the following three points in English.
        Please note, describe it in markdown format, emphasizing important points in bold, making the title parts bigger, and so on, for easier reading.

        ## 1. Meeting Summary
        ## 2. Decisions Made in the Meeting
        ## 3. ToDos or Next Actions from Meeting Conclusions
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        This transcription is too long, please summarize it while ensuring the key points are captured.
        Please note that this transcription may be a part cut out from a longer transcription.
        """
    )
    
    
class SpanishMeetingPrompts(Enum):
    """
    Enum for storing prompts for meeting minutes in Spanish.

    Attributes
    ----------
    TRANSCRIBE_FORMAT : str
        The format string for the prompt for transcribing the audio.
        Used in `src/minutes_maker/_transcriber.py`.

    SUMMARIZE_SYSTEM_PROMPT : str
        The system message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SUMMARY : str
        The user message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SHORTENING : str
        The user message for shortening the transcript.
        Used in `src/minutes_maker/_summarizer.py`.
    """

    TRANSCRIBE_FORMAT: str = "Transcripción de la reunión sobre {content}."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        Por favor, explique cada punto en 4-5 frases para mayor detalle.
        El siguiente texto es una transcripción de una reunión en español.
        La transcripción fue realizada por un modelo de aprendizaje automático y su precisión no es del 100%.
        También puede incluir ruidos de fondo o descripciones del desarrollo de la reunión además de las declaraciones de los participantes.
        Teniendo esto en cuenta, por favor lea la transcripción y responda a la pregunta del usuario.

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        A partir del contenido de la transcripción de la reunión, por favor resuma los siguientes tres puntos en español.
        Escriba en formato markdown, resaltando los puntos importantes en **negrita**, y utilizando encabezados grandes para mayor claridad.

        ## 1. Resumen de la reunión
        ## 2. Decisiones tomadas en la reunión
        ## 3. Tareas o próximas acciones derivadas de las conclusiones
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        Esta transcripción es demasiado larga, por favor resúmala asegurando que se capturen los puntos clave.
        Tenga en cuenta que esta transcripción puede ser parte de una transcripción más larga.
        """
    )


class FrenchMeetingPrompts(Enum):
    
    """
    Enum for storing prompts for meeting minutes in French.

    Attributes
    ----------
    TRANSCRIBE_FORMAT : str
        The format string for the prompt for transcribing the audio.
        Used in `src/minutes_maker/_transcriber.py`.

    SUMMARIZE_SYSTEM_PROMPT : str
        The system message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SUMMARY : str
        The user message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SHORTENING : str
        The user message for shortening the transcript.
        Used in `src/minutes_maker/_summarizer.py`.
    """
    
    
    TRANSCRIBE_FORMAT: str = "Transcription de la réunion concernant {content}."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc("""
        Veuillez expliquer chaque point en 4-5 phrases pour plus de détails.
        Le texte suivant est une transcription d'une réunion en français.
        La transcription a été réalisée par un modèle d'apprentissage automatique, et sa précision n'est pas de 100%.
        Elle peut contenir des bruits de fond ou des descriptions du déroulement de la réunion en plus des déclarations des participants.
        Veuillez lire la transcription ci-dessous et répondre à la question de l'utilisateur.

        '''
        {transcript}
        '''
    """)
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc("""
        À partir du contenu de la transcription de la réunion, veuillez résumer les trois points suivants en français.
        Utilisez le format markdown, en mettant les points importants en **gras** et en utilisant des titres pour plus de clarté.

        ## 1. Résumé de la réunion
        ## 2. Décisions prises lors de la réunion
        ## 3. Tâches ou prochaines actions issues des conclusions
    """)
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc("""
        Cette transcription est trop longue, veuillez la résumer en veillant à conserver les points clés.
        Notez que cette transcription peut faire partie d'une transcription plus longue.
    """)

class GermanMeetingPrompts(Enum):
    
    """
    Enum for storing prompts for meeting minutes in German.

    Attributes
    ----------
    TRANSCRIBE_FORMAT : str
        The format string for the prompt for transcribing the audio.
        Used in `src/minutes_maker/_transcriber.py`.

    SUMMARIZE_SYSTEM_PROMPT : str
        The system message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SUMMARY : str
        The user message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SHORTENING : str
        The user message for shortening the transcript.
        Used in `src/minutes_maker/_summarizer.py`.
    """
    
    
    TRANSCRIBE_FORMAT: str = "Transkription des Meetings zu {content}."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc("""
        Bitte erklären Sie jeden Punkt in 4-5 Sätzen für mehr Details.                                    
        Der folgende Text ist ein Transkript eines Meetings auf Deutsch.
        Das Transkript wurde von einem maschinellen Lernmodell erstellt und ist nicht zu 100% genau.
        Es kann Hintergrundgeräusche oder Beschreibungen des Sitzungsverlaufs enthalten.
        Bitte lesen Sie das Transkript unten und beantworten Sie die Frage des Benutzers.

        '''
        {transcript}
        '''
    """)
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc("""
        Bitte fassen Sie basierend auf dem Inhalt des Transkripts die folgenden drei Punkte auf Deutsch zusammen.
        Verwenden Sie Markdown-Format, heben Sie wichtige Punkte fett hervor und gestalten Sie die Überschriften klar.

        ## 1. Zusammenfassung des Meetings
        ## 2. Im Meeting getroffene Entscheidungen
        ## 3. Aufgaben oder nächste Schritte aus den Ergebnissen
    """)
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc("""
        Dieses Transkript ist zu lang, bitte fassen Sie es zusammen und achten Sie darauf, die Schlüsselpunkte zu erfassen.
        Beachten Sie, dass dieses Transkript ein Ausschnitt eines längeren Transkripts sein kann.
    """)

class ChineseMeetingPrompts(Enum):
    
    """
    Enum for storing prompts for meeting minutes in Chinese.

    Attributes
    ----------
    TRANSCRIBE_FORMAT : str
        The format string for the prompt for transcribing the audio.
        Used in `src/minutes_maker/_transcriber.py`.

    SUMMARIZE_SYSTEM_PROMPT : str
        The system message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SUMMARY : str
        The user message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SHORTENING : str
        The user message for shortening the transcript.
        Used in `src/minutes_maker/_summarizer.py`.
    """
    
    
    TRANSCRIBE_FORMAT: str = "关于{content}的会议记录。"
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc("""
        请将每一点用4-5句话详细说明，以便内容更丰富。                                          
        以下是一次中文会议的转录内容。
        转录由机器学习模型完成，其准确性不是100%。
        转录内容可能包含背景噪音或会议流程的描述。
        请阅读下方转录内容，并回答用户的问题。

        '''
        {transcript}
        '''
    """)
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc("""
        请根据会议记录内容，总结以下三点。
        使用markdown格式，重点内容请加粗，标题清晰。

        ## 1. 会议总结
        ## 2. 会议决定事项
        ## 3. 后续任务或行动计划
    """)
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc("""
        本次转录内容过长，请在确保关键信息完整的前提下进行摘要。
        注意，这段内容可能是更长会议记录的一部分。
    """)

class HindiMeetingPrompts(Enum):
    """
    Enum for storing prompts for meeting minutes in Hindi (simplified language).
    """

    TRANSCRIBE_FORMAT: str = "{content} से जुड़ी मीटिंग की ट्रांसक्रिप्शन।"
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc("""
        कृपया हर बिंदु को 4-5 वाक्यों में विस्तार से समझाएँ ताकि उत्तर पूरा हो।                                        
        नीचे दिया गया टेक्स्ट एक हिंदी मीटिंग की ट्रांसक्रिप्शन है।
        यह ट्रांसक्रिप्शन एक मशीन लर्निंग मॉडल ने बनाई है, इसलिए इसमें थोड़ी गलती हो सकती है।
        इसमें शोर या मीटिंग की जानकारी भी हो सकती है।
        कृपया ट्रांसक्रिप्शन पढ़ें और यूज़र के सवाल का जवाब दें।

        '''
        {transcript}
        '''
    """)
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc("""
        मीटिंग की ट्रांसक्रिप्शन से नीचे दिए गए तीन पॉइंट्स का हिंदी में आसान और छोटा सारांश बनाइए।
        प्लीज़ markdown फॉर्मेट में लिखें, जरूरी बातों को **बोल्ड** करें और टाइटल्स साफ दिखाएँ।

        ## 1. मीटिंग का सारांश
        ## 2. मीटिंग में क्या-क्या फैसले हुए
        ## 3. मीटिंग के बाद कौन-से काम या अगले स्टेप्स तय हुए
    """)
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc("""
        यह ट्रांसक्रिप्शन बहुत लंबी है, तो कृपया सिर्फ मुख्य बातों को ध्यान में रखते हुए इसे छोटा करें।
        ध्यान रहे, यह किसी लंबी ट्रांसक्रिप्शन का हिस्सा भी हो सकता है।
    """)



class ArabicMeetingPrompts(Enum):
    
    """
    Enum for storing prompts for meeting minutes in Arabic.

    Attributes
    ----------
    TRANSCRIBE_FORMAT : str
        The format string for the prompt for transcribing the audio.
        Used in `src/minutes_maker/_transcriber.py`.

    SUMMARIZE_SYSTEM_PROMPT : str
        The system message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SUMMARY : str
        The user message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SHORTENING : str
        The user message for shortening the transcript.
        Used in `src/minutes_maker/_summarizer.py`.
    """
    
    
    TRANSCRIBE_FORMAT: str = "نسخة من الاجتماع حول {content}."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc("""
        يرجى شرح كل نقطة في 4-5 جمل لمزيد من التفاصيل.                                     
        النص التالي هو نسخة من اجتماع باللغة العربية.
        تم إجراء النسخ بواسطة نموذج تعلم آلي، ودقته ليست 100٪.
        قد يحتوي النص على ضوضاء خلفية أو أوصاف لسير الاجتماع.
        يرجى قراءة النسخة أدناه والإجابة على سؤال المستخدم.

        '''
        {transcript}
        '''
    """)
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc("""
        من محتوى النسخة، يرجى تلخيص النقاط الثلاث التالية باللغة العربية.
        استخدم تنسيق markdown، وقم بتوضيح العناوين وتحديد النقاط المهمة بخط عريض.

        ## 1. ملخص الاجتماع
        ## 2. القرارات المتخذة في الاجتماع
        ## 3. المهام أو الإجراءات التالية بناءً على نتائج الاجتماع
    """)
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc("""
        هذه النسخة طويلة جدًا، يرجى تلخيصها مع الحفاظ على النقاط الأساسية.
        لاحظ أن هذه النسخة قد تكون جزءًا من نسخة أطول.
    """)

class RussianMeetingPrompts(Enum):
    
    """
    Enum for storing prompts for meeting minutes in Russian.

    Attributes
    ----------
    TRANSCRIBE_FORMAT : str
        The format string for the prompt for transcribing the audio.
        Used in `src/minutes_maker/_transcriber.py`.

    SUMMARIZE_SYSTEM_PROMPT : str
        The system message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SUMMARY : str
        The user message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SHORTENING : str
        The user message for shortening the transcript.
        Used in `src/minutes_maker/_summarizer.py`.
    """
    
    
    TRANSCRIBE_FORMAT: str = "Транскрипция встречи по теме {content}."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc("""
        Пожалуйста, объясните каждый пункт в 4-5 предложениях для большей детализации.                                     
        Следующий текст — это транскрипция встречи на русском языке.
        Транскрипция выполнена моделью машинного обучения и может быть неточной.
        Она может содержать фоновый шум или описание хода встречи.
        Пожалуйста, прочтите транскрипцию и ответьте на вопрос пользователя.

        '''
        {transcript}
        '''
    """)
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc("""
        Исходя из транскрипции встречи, кратко изложите следующие три пункта на русском языке.
        Используйте формат markdown, выделяйте важные моменты жирным шрифтом и структурируйте заголовки.

        ## 1. Краткое содержание встречи
        ## 2. Принятые решения
        ## 3. Дальнейшие действия или задачи
    """)
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc("""
        Эта транскрипция слишком длинная, пожалуйста, сократите её, сохранив ключевые моменты.
        Учтите, что это может быть фрагмент более длинной транскрипции.
    """)

class PortugueseMeetingPrompts(Enum):
    
    """
    Enum for storing prompts for meeting minutes in Portuguese.

    Attributes
    ----------
    TRANSCRIBE_FORMAT : str
        The format string for the prompt for transcribing the audio.
        Used in `src/minutes_maker/_transcriber.py`.

    SUMMARIZE_SYSTEM_PROMPT : str
        The system message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SUMMARY : str
        The user message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SHORTENING : str
        The user message for shortening the transcript.
        Used in `src/minutes_maker/_summarizer.py`.
    """
    
    
    TRANSCRIBE_FORMAT: str = "Transcrição da reunião sobre {content}."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc("""
        Por favor, explique cada ponto em 4-5 frases para mais detalhes.                               
        O texto a seguir é uma transcrição de uma reunião em português.
        A transcrição foi feita por um modelo de aprendizado de máquina e pode não ser 100% precisa.
        Pode conter ruídos de fundo ou descrições do andamento da reunião.
        Leia a transcrição abaixo e responda à pergunta do usuário.

        '''
        {transcript}
        '''
    """)
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc("""
        Com base no conteúdo da transcrição da reunião, resuma os três pontos a seguir em português.
        Use o formato markdown, destaque os pontos importantes em **negrito** e utilize títulos claros.

        ## 1. Resumo da reunião
        ## 2. Decisões tomadas na reunião
        ## 3. Tarefas ou próximas ações derivadas das conclusões
    """)
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc("""
        Esta transcrição é muito longa, por favor resuma garantindo que os pontos-chave sejam mantidos.
        Note que esta transcrição pode ser parte de uma transcrição maior.
    """)

class KoreanMeetingPrompts(Enum):
    
    """
    Enum for storing prompts for meeting minutes in Korean.

    Attributes
    ----------
    TRANSCRIBE_FORMAT : str
        The format string for the prompt for transcribing the audio.
        Used in `src/minutes_maker/_transcriber.py`.

    SUMMARIZE_SYSTEM_PROMPT : str
        The system message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SUMMARY : str
        The user message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SHORTENING : str
        The user message for shortening the transcript.
        Used in `src/minutes_maker/_summarizer.py`.
    """
    
    
    TRANSCRIBE_FORMAT: str = "{content}에 대한 회의 기록."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc("""
        각 항목을 4-5문장으로 자세하게 설명해 주세요.                                       
        다음 텍스트는 한국어 회의의 전사입니다.
        전사는 머신러닝 모델에 의해 생성되었으며 정확도가 100%는 아닙니다.
        배경 소음이나 회의 진행에 대한 설명이 포함될 수 있습니다.
        아래 전사 내용을 읽고 사용자 질문에 답해주세요.

        '''
        {transcript}
        '''
    """)
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc("""
        회의 전사 내용을 바탕으로 다음 세 가지 항목을 한국어로 요약해주세요.
        markdown 형식을 사용하고, 중요한 내용을 **굵게** 표시하고, 제목을 명확히 작성해주세요.

        ## 1. 회의 요약
        ## 2. 회의에서 결정된 사항
        ## 3. 결론으로부터 파생된 작업 또는 다음 조치
    """)
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc("""
        이 전사는 너무 깁니다. 핵심 내용을 유지하면서 요약해주세요.
        이 전사는 더 긴 전사의 일부일 수 있습니다.
    """)


class ItalianMeetingPrompts(Enum):
    
    """
    Enum for storing prompts for meeting minutes in Italian.

    Attributes
    ----------
    TRANSCRIBE_FORMAT : str
        The format string for the prompt for transcribing the audio.
        Used in `src/minutes_maker/_transcriber.py`.

    SUMMARIZE_SYSTEM_PROMPT : str
        The system message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SUMMARY : str
        The user message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SHORTENING : str
        The user message for shortening the transcript.
        Used in `src/minutes_maker/_summarizer.py`.
    """
    
    TRANSCRIBE_FORMAT: str = "Trascrizione della riunione riguardante {content}."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc("""
        Si prega di spiegare ogni punto in 4-5 frasi per maggiore dettaglio.                                     
        Il seguente testo è una trascrizione di una riunione in italiano.
        La trascrizione è stata eseguita da un modello di apprendimento automatico e potrebbe non essere accurata al 100%.
        Potrebbero essere presenti rumori di fondo o descrizioni dello svolgimento della riunione.
        Leggi la trascrizione qui sotto e rispondi alla domanda dell'utente.

        '''
        {transcript}
        '''
    """)
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc("""
        Sulla base della trascrizione della riunione, riassumi i seguenti tre punti in italiano.
        Utilizza il formato markdown, evidenzia i punti importanti in **grassetto** e rendi i titoli chiari.

        ## 1. Riassunto della riunione
        ## 2. Decisioni prese nella riunione
        ## 3. Attività o prossime azioni derivanti dalle conclusioni
    """)
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc("""
        Questa trascrizione è troppo lunga, per favore riassumila mantenendo i punti chiave.
        Nota che potrebbe trattarsi di una parte di una trascrizione più lunga.
    """)

class TurkishMeetingPrompts(Enum):
    
    """
    Enum for storing prompts for meeting minutes in Turkish.

    Attributes
    ----------
    TRANSCRIBE_FORMAT : str
        The format string for the prompt for transcribing the audio.
        Used in `src/minutes_maker/_transcriber.py`.

    SUMMARIZE_SYSTEM_PROMPT : str
        The system message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SUMMARY : str
        The user message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SHORTENING : str
        The user message for shortening the transcript.
        Used in `src/minutes_maker/_summarizer.py`.
    """
    
    
    
    TRANSCRIBE_FORMAT: str = "{content} ile ilgili toplantının dökümü."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc("""
        Lütfen her maddeyi 4-5 cümleyle detaylıca açıklayın.                                      
        Aşağıdaki metin Türkçe bir toplantının dökümüdür.
        Döküm, bir makine öğrenimi modeli tarafından yapılmıştır ve %100 doğru olmayabilir.
        Katılımcıların sözlerinin yanı sıra arka plan gürültüsü veya toplantının gidişatına dair açıklamalar içerebilir.
        Lütfen aşağıdaki dökümü okuyun ve kullanıcının sorusunu yanıtlayın.

        '''
        {transcript}
        '''
    """)
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc("""
        Toplantı dökümünün içeriğine dayanarak lütfen aşağıdaki üç noktayı Türkçe olarak özetleyin.
        Markdown formatını kullanın, önemli noktaları **kalın** yazın ve başlıkları açıkça belirtin.

        ## 1. Toplantı Özeti
        ## 2. Toplantıda Alınan Kararlar
        ## 3. Toplantı Sonuçlarından Çıkarılabilecek Görevler veya Sonraki Adımlar
    """)
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc("""
        Bu döküm çok uzun, lütfen ana noktaları koruyarak özetleyin.
        Bu döküm daha uzun bir metnin parçası olabilir.
    """)

class BengaliMeetingPrompts(Enum):
    
    
    """
    Enum for storing prompts for meeting minutes in Bengali.

    Attributes
    ----------
    TRANSCRIBE_FORMAT : str
        The format string for the prompt for transcribing the audio.
        Used in `src/minutes_maker/_transcriber.py`.

    SUMMARIZE_SYSTEM_PROMPT : str
        The system message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SUMMARY : str
        The user message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SHORTENING : str
        The user message for shortening the transcript.
        Used in `src/minutes_maker/_summarizer.py`.
    """
    
    
    TRANSCRIBE_FORMAT: str = "{content} সম্পর্কিত মিটিং-এর ট্রান্সক্রিপশন।"
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc("""
        অনুগ্রহ করে প্রতিটি বিষয়ে 4-5টি বাক্যে বিস্তারিতভাবে ব্যাখ্যা করুন।                                                                         
        নিম্নলিখিত পাঠ্যটি একটি বাংলা মিটিং-এর ট্রান্সক্রিপশন।
        এটি একটি মেশিন লার্নিং মডেল দ্বারা তৈরি, এবং এর নির্ভুলতা ১০০% নয়।
        এতে ব্যাকগ্রাউন্ড শব্দ বা মিটিং-এর অগ্রগতির বর্ণনা থাকতে পারে।
        অনুগ্রহ করে ট্রান্সক্রিপশনটি পড়ুন এবং ব্যবহারকারীর প্রশ্নের উত্তর দিন।

        '''
        {transcript}
        '''
    """)
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc("""
        ট্রান্সক্রিপশন এর বিষয়বস্তুর উপর ভিত্তি করে নিচের তিনটি বিষয় বাংলা ভাষায় সংক্ষেপে উপস্থাপন করুন।
        markdown ফরম্যাট ব্যবহার করুন, গুরুত্বপূর্ণ বিষয়গুলো **bold** করুন এবং শিরোনামগুলো স্পষ্ট করুন।

        ## 1. মিটিং সারাংশ
        ## 2. মিটিং-এ গৃহীত সিদ্ধান্ত
        ## 3. মিটিং-এর উপসংহার থেকে সম্ভাব্য কাজ বা পরবর্তী পদক্ষেপ
    """)
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc("""
        এই ট্রান্সক্রিপশনটি অনেক বড়, অনুগ্রহ করে মূল বিষয়বস্তু বজায় রেখে এটি সংক্ষিপ্ত করুন।
        মনে রাখবেন এটি একটি বড় ট্রান্সক্রিপশনের অংশ হতে পারে।
    """)

class UrduMeetingPrompts(Enum):
    
    """
    Enum for storing prompts for meeting minutes in Urdu.

    Attributes
    ----------
    TRANSCRIBE_FORMAT : str
        The format string for the prompt for transcribing the audio.
        Used in `src/minutes_maker/_transcriber.py`.

    SUMMARIZE_SYSTEM_PROMPT : str
        The system message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SUMMARY : str
        The user message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SHORTENING : str
        The user message for shortening the transcript.
        Used in `src/minutes_maker/_summarizer.py`.
    """
    
    
    TRANSCRIBE_FORMAT: str = "{content} سے متعلق میٹنگ کا ٹرانسکرپشن۔"
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc("""
        براہ کرم ہر نکتہ کو4-5جملوں میں وضاحت سے بیان کریں۔
        ذیل کا متن ایک اردو میٹنگ کی ٹرانسکرپشن ہے۔
        یہ ٹرانسکرپشن ایک مشین لرننگ ماڈل نے تیار کی ہے اور یہ مکمل طور پر درست نہیں ہو سکتی۔
        اس میں پس منظر کی آوازیں یا میٹنگ کی پیش رفت کی تفصیلات ہو سکتی ہیں۔
        براہ کرم نیچے دی گئی ٹرانسکرپشن کو پڑھیں اور صارف کے سوال کا جواب دیں۔

        '''
        {transcript}
        '''
    """)
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc("""
        میٹنگ کی ٹرانسکرپشن کے مواد کی بنیاد پر، براہ کرم اردو میں درج ذیل تین نکات کا خلاصہ فراہم کریں۔
        markdown فارمیٹ استعمال کریں، اہم نکات کو **بولڈ** کریں اور عنوانات کو واضح رکھیں۔

        ## 1. میٹنگ کا خلاصہ
        ## 2. میٹنگ میں کیے گئے فیصلے
        ## 3. میٹنگ کے نتائج سے اخذ کردہ کام یا اگلے اقدامات
    """)
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc("""
        یہ ٹرانسکرپشن بہت طویل ہے، براہ کرم اسے اہم نکات کے ساتھ مختصر کریں۔
        نوٹ کریں کہ یہ کسی بڑی ٹرانسکرپشن کا حصہ ہو سکتی ہے۔
    """)
 
    



class JapaneseLecturePrompts(Enum):
    """
    Enum for storing prompts for lecture transcripts and summaries in Japanese.

    Attributes
    ----------
    TRANSCRIBE_FORMAT : str
        The format string for the prompt for transcribing the audio.
        Used in `src/minutes_maker/_transcriber.py`.

    SUMMARIZE_SYSTEM_PROMPT : str
        The system message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SUMMARY : str
        The user message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SHORTENING : str
        The user message for shortening the transcript.
        Used in `src/minutes_maker/_summarizer.py`.
    """

    TRANSCRIBE_FORMAT: str = "{content}に関する、レクチャーの書き起こし。"
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        以下のテキストは、ある日本語のレクチャーの内容を文字起こししたものです。
        文字起こしは機械学習モデルによって行われており、その精度は100%ではありません。
        また、文字起こしの結果には、レクチャーの参加者の発言以外にも、雑音やレクチャーの進行に関する記述が含まれている可能性があります。
        それを踏まえた上で、以下の文字起こしを読み、ユーザーの質問に答えてください。

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        レクチャーの文字起こしの内容から、以下の3点について日本語でまとめてください。
        なお、markdown形式で、重要な点を太字にしたり、タイトル部分を大きくしたりなど、読みやすいように工夫して記述してください。

        ## 1. レクチャーのサマリ
        ## 2. レクチャーで説明された主要なポイント
        ## 3. レクチャーの結論
        ## 4. その他、レクチャーの内容に関するメモ
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        この文字起こしは長すぎるため、要点を確実に押さえながら要約してください。
        なお、この文字起こしはより長い文字起こし文の一部切り出したものである可能性があることに注意してください。
        """
    )


class EnglishLecturePrompts(Enum):
    """
    Enum for storing prompts for lecture transcripts and summaries in English.

    Attributes
    ----------
    TRANSCRIBE_FORMAT : str
        The format string for the prompt for transcribing the audio.
        Used in `src/minutes_maker/_transcriber.py`.

    SUMMARIZE_SYSTEM_PROMPT : str
        The system message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SUMMARY : str
        The user message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SHORTENING : str
        The user message for shortening the transcript.
        Used in `src/minutes_maker/_summarizer.py`.
    """

    TRANSCRIBE_FORMAT: str = "Transcription of the lecture regarding {content}."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        The following text is a transcription of a lecture in English.
        The transcription is done by a machine learning model, and its accuracy is not 100%.
        Also, the transcription results may include not only the speakers' remarks, but also background noise and descriptions of the lecture's progress.
        Bearing this in mind, please read the transcription below and answer the user's question.

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        From the content of the lecture transcription, please summarize the following three points in English.
        Please note, describe it in markdown format, emphasizing important points in bold, making the title parts bigger, and so on, for easier reading.

        ## 1. Lecture Summary
        ## 2. Key Points Explained in the Lecture
        ## 3. Lecture Conclusions
        ## 4. Other Notes on the Lecture Content
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        This transcription is too long, please summarize it while ensuring the key points are captured.
        Please note that this transcription may be a part cut out from a longer transcription.
        """
    )


class SpanishLecturePrompts(Enum):
    TRANSCRIBE_FORMAT: str = "Transcripción de la clase sobre {content}."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        Por favor, explique cada punto en 4-5 frases para mayor detalle.
        El siguiente texto es una transcripción de una clase en español.
        La transcripción ha sido realizada por un modelo de aprendizaje automático y puede no ser 100% precisa.
        También puede contener ruidos de fondo o descripciones del desarrollo de la clase.
        Teniendo esto en cuenta, lea la transcripción a continuación y responda a la pregunta del usuario.

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        A partir del contenido de la transcripción de la clase, resuma los siguientes puntos en español.
        Use formato markdown, resalte los puntos importantes en **negrita** y haga que los títulos sean más visibles para facilitar la lectura.

        ## 1. Resumen de la clase
        ## 2. Puntos clave explicados en la clase
        ## 3. Conclusiones de la clase
        ## 4. Otras notas sobre el contenido de la clase
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        Esta transcripción es demasiado larga, por favor resuma asegurando que se mantengan los puntos clave.
        Tenga en cuenta que esta transcripción puede ser parte de una transcripción más larga.
        """
    )



class FrenchLecturePrompts(Enum):
    TRANSCRIBE_FORMAT: str = "Transcription du cours sur {content}."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        Veuillez expliquer chaque point en 4-5 phrases pour plus de détails.
        Le texte suivant est une transcription d'un cours en français.
        La transcription a été réalisée par un modèle d'apprentissage automatique et peut ne pas être précise à 100%.
        Elle peut contenir des bruits de fond ou des descriptions du déroulement du cours.
        Veuillez lire la transcription ci-dessous et répondre à la question de l'utilisateur.

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        À partir du contenu de la transcription du cours, veuillez résumer les points suivants en français.
        Utilisez le format markdown, mettez en **gras** les points importants et utilisez des titres clairs pour une lecture facile.

        ## 1. Résumé du cours
        ## 2. Points clés expliqués pendant le cours
        ## 3. Conclusions du cours
        ## 4. Autres notes sur le contenu du cours
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        Cette transcription est trop longue, veuillez la résumer en veillant à conserver les points clés.
        Notez que cette transcription peut faire partie d'une transcription plus longue.
        """
    )


class GermanLecturePrompts(Enum):
    TRANSCRIBE_FORMAT: str = "Transkription der Vorlesung zu {content}."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        Bitte erklären Sie jeden Punkt in 4-5 Sätzen für mehr Details.
        Der folgende Text ist eine Transkription einer Vorlesung auf Deutsch.
        Die Transkription wurde von einem maschinellen Lernmodell erstellt und ist möglicherweise nicht zu 100% genau.
        Sie kann Hintergrundgeräusche oder Beschreibungen des Ablaufs der Vorlesung enthalten.
        Bitte lesen Sie die Transkription und beantworten Sie die Frage des Nutzers.

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        Fassen Sie basierend auf dem Inhalt der Vorlesungstranskription die folgenden Punkte auf Deutsch zusammen.
        Verwenden Sie Markdown-Format, heben Sie wichtige Punkte **fett** hervor und gestalten Sie die Überschriften klar.

        ## 1. Zusammenfassung der Vorlesung
        ## 2. In der Vorlesung erklärte Hauptpunkte
        ## 3. Schlussfolgerungen der Vorlesung
        ## 4. Weitere Notizen zum Inhalt der Vorlesung
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        Diese Transkription ist zu lang, bitte fassen Sie sie zusammen und achten Sie darauf, die Schlüsselpunkte zu erfassen.
        Beachten Sie, dass diese Transkription Teil einer längeren Transkription sein kann.
        """
    )



class ChineseLecturePrompts(Enum):
    TRANSCRIBE_FORMAT: str = "关于{content}的讲座记录。"
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        请将每一点用4-5句话详细说明，以便内容更丰富。
        以下文本为一场中文讲座的转录内容。
        转录由机器学习模型生成，准确性并非100%。
        结果中可能包含背景噪音或讲座进程的描述。
        请阅读下方转录内容，并回答用户的问题。

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        请根据讲座的转录内容，用中文总结以下几点。请使用 markdown 格式，重要内容加粗，标题醒目，便于阅读。

        ## 1. 讲座摘要
        ## 2. 讲座中讲解的关键点
        ## 3. 讲座结论
        ## 4. 其他讲座内容相关备注
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        本次转录内容过长，请确保保留要点并进行摘要。
        注意，这段内容可能是更长转录内容的一部分。
        """
    )


class HindiLecturePrompts(Enum):
    TRANSCRIBE_FORMAT: str = "{content} से जुड़ा लेक्चर ट्रांसक्रिप्शन।"
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        कृपया हर बिंदु को 4-5 वाक्यों में विस्तार से समझाएँ ताकि उत्तर पूरा हो।
        नीचे दिया गया टेक्स्ट एक हिंदी लेक्चर की ट्रांसक्रिप्शन है।
        यह ट्रांसक्रिप्शन मशीन लर्निंग मॉडल से बनी है, इसलिए इसमें थोड़ी गलती हो सकती है।
        इसमें शोर या लेक्चर से जुड़ी दूसरी बातें भी हो सकती हैं।
        कृपया ट्रांसक्रिप्शन पढ़ें और यूज़र के सवाल का जवाब दें।

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        लेक्चर की ट्रांसक्रिप्शन के आधार पर, नीचे दिए गए पॉइंट्स को आसान हिंदी में संक्षेप में लिखिए।
        कृपया markdown फॉर्मेट में लिखें, ज़रूरी बातों को **बोल्ड** करें और टाइटल्स साफ दिखाएँ।

        ## 1. लेक्चर का सारांश
        ## 2. लेक्चर में बताए गए मुख्य पॉइंट्स
        ## 3. लेक्चर का नतीजा
        ## 4. लेक्चर के बारे में दूसरी बातें/नोट्स
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        यह ट्रांसक्रिप्शन बहुत लंबी है, कृपया सिर्फ मुख्य बातों को ध्यान में रखते हुए इसे छोटा करें।
        ध्यान दें, यह किसी बड़ी ट्रांसक्रिप्शन का हिस्सा भी हो सकता है।
        """
    )



class ArabicLecturePrompts(Enum):
    TRANSCRIBE_FORMAT: str = "نسخة من المحاضرة حول {content}."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        يرجى شرح كل نقطة في4-5جمل لمزيد من التفاصيل.
        النص التالي هو نسخة من محاضرة باللغة العربية.
        تم إجراء النسخ بواسطة نموذج تعلم آلي، ودقته ليست 100٪.
        قد تحتوي النسخة على ضوضاء خلفية أو أوصاف لسير المحاضرة.
        يرجى قراءة النسخة أدناه والإجابة على سؤال المستخدم.

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        من محتوى النسخة، يرجى تلخيص النقاط التالية باللغة العربية.
        استخدم تنسيق markdown، وحدد النقاط المهمة بخط عريض، واجعل العناوين أوضح لسهولة القراءة.

        ## 1. ملخص المحاضرة
        ## 2. النقاط الرئيسية المشروحة في المحاضرة
        ## 3. استنتاجات المحاضرة
        ## 4. ملاحظات أخرى حول محتوى المحاضرة
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        هذه النسخة طويلة جدًا، يرجى تلخيصها مع الحفاظ على النقاط الأساسية.
        لاحظ أن هذه النسخة قد تكون جزءًا من نسخة أطول.
        """
    )


class RussianLecturePrompts(Enum):
    TRANSCRIBE_FORMAT: str = "Транскрипция лекции по теме {content}."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        Пожалуйста, объясните каждый пункт в 4-5 предложениях для большей детализации.
        Следующий текст — это транскрипция лекции на русском языке.
        Транскрипция выполнена моделью машинного обучения и может быть неточной.
        Она может содержать фоновый шум или описание хода лекции.
        Пожалуйста, прочтите транскрипцию и ответьте на вопрос пользователя.

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        На основании транскрипта лекции кратко изложите следующие пункты на русском языке.
        Используйте формат markdown, выделяйте важные моменты жирным шрифтом и делайте заголовки более заметными.

        ## 1. Краткое содержание лекции
        ## 2. Ключевые пункты, объяснённые в лекции
        ## 3. Выводы лекции
        ## 4. Прочие заметки по содержанию лекции
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        Эта транскрипция слишком длинная, пожалуйста, сократите её, сохранив ключевые моменты.
        Учтите, что это может быть фрагмент более длинной транскрипции.
        """
    )



class PortugueseLecturePrompts(Enum):
    TRANSCRIBE_FORMAT: str = "Transcrição da aula sobre {content}."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        Por favor, explique cada ponto em 4-5 frases para mais detalhes.
        O texto a seguir é uma transcrição de uma aula em português.
        A transcrição foi feita por um modelo de aprendizado de máquina e pode não ser 100% precisa.
        Pode conter ruídos de fundo ou descrições do andamento da aula.
        Leia a transcrição abaixo e responda à pergunta do usuário.

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        Com base no conteúdo da transcrição da aula, resuma os seguintes pontos em português.
        Use o formato markdown, destaque os pontos importantes em **negrito** e torne os títulos mais visíveis.

        ## 1. Resumo da aula
        ## 2. Pontos chave explicados na aula
        ## 3. Conclusões da aula
        ## 4. Outras notas sobre o conteúdo da aula
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        Esta transcrição é muito longa, por favor resuma garantindo que os pontos-chave sejam mantidos.
        Note que esta transcrição pode ser parte de uma transcrição maior.
        """
    )



class UrduLecturePrompts(Enum):
    TRANSCRIBE_FORMAT: str = "{content} سے متعلق لیکچر کا ٹرانسکرپشن۔"
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        براہ کرم ہر نکتہ کو 4-5 جملوں میں وضاحت سے بیان کریں۔
        ذیل کا متن ایک اردو لیکچر کی ٹرانسکرپشن ہے۔
        یہ ٹرانسکرپشن ایک مشین لرننگ ماڈل نے تیار کی ہے اور یہ مکمل طور پر درست نہیں ہو سکتی۔
        اس میں پس منظر کی آوازیں یا لیکچر کی پیش رفت کی تفصیلات ہو سکتی ہیں۔
        براہ کرم نیچے دی گئی ٹرانسکرپشن کو پڑھیں اور صارف کے سوال کا جواب دیں۔

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        لیکچر کی ٹرانسکرپشن کے مواد کی بنیاد پر، براہ کرم اردو میں درج ذیل نکات کا خلاصہ فراہم کریں۔
        markdown فارمیٹ استعمال کریں، اہم نکات کو **بولڈ** کریں اور عنوانات کو واضح رکھیں۔

        ## 1. لیکچر کا خلاصہ
        ## 2. لیکچر میں بیان کیے گئے اہم نکات
        ## 3. لیکچر کے نتائج
        ## 4. لیکچر کے مواد سے متعلق دیگر نوٹس
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        یہ ٹرانسکرپشن بہت طویل ہے، براہ کرم اسے اہم نکات کے ساتھ مختصر کریں۔
        نوٹ کریں کہ یہ کسی بڑی ٹرانسکرپشن کا حصہ ہو سکتی ہے۔
        """
    )



class KoreanLecturePrompts(Enum):
    TRANSCRIBE_FORMAT: str = "{content}에 관한 강의 기록."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        각 항목을 4-5문장으로 자세하게 설명해 주세요.
        다음 텍스트는 한국어 강의의 전사입니다.
        전사는 머신러닝 모델에 의해 생성되었으며 정확도가 100%는 아닙니다.
        배경 소음이나 강의 진행에 대한 설명이 포함될 수 있습니다.
        아래 전사 내용을 읽고 사용자 질문에 답해주세요.

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        강의 전사 내용을 바탕으로 다음 항목을 한국어로 요약해주세요.
        마크다운 형식을 사용하고, 중요한 내용을 **굵게** 표시하고, 제목을 명확히 작성해주세요.

        ## 1. 강의 요약
        ## 2. 강의에서 설명된 주요 포인트
        ## 3. 강의 결론
        ## 4. 강의 내용에 대한 기타 메모
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        이 전사는 너무 깁니다. 핵심 내용을 유지하면서 요약해주세요.
        이 전사는 더 긴 전사의 일부일 수 있습니다.
        """
    )


class ItalianLecturePrompts(Enum):
    TRANSCRIBE_FORMAT: str = "Trascrizione della lezione riguardante {content}."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        Si prega di spiegare ogni punto in 4-5 frasi per maggiore dettaglio.
        Il seguente testo è una trascrizione di una lezione in italiano.
        La trascrizione è stata eseguita da un modello di apprendimento automatico e potrebbe non essere accurata al 100%.
        Potrebbero essere presenti rumori di fondo o descrizioni dello svolgimento della lezione.
        Leggi la trascrizione qui sotto e rispondi alla domanda dell'utente.

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        Sulla base della trascrizione della lezione, riassumi i seguenti punti in italiano.
        Utilizza il formato markdown, evidenzia i punti importanti in **grassetto** e rendi i titoli chiari.

        ## 1. Riassunto della lezione
        ## 2. Punti chiave spiegati nella lezione
        ## 3. Conclusioni della lezione
        ## 4. Altre note sul contenuto della lezione
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        Questa trascrizione è troppo lunga, per favore riassumila mantenendo i punti chiave.
        Nota che potrebbe trattarsi di una parte di una trascrizione più lunga.
        """
    )



class TurkishLecturePrompts(Enum):
    TRANSCRIBE_FORMAT: str = "{content} ile ilgili dersin dökümü."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        Lütfen her maddeyi 4-5 cümleyle detaylıca açıklayın.
        Aşağıdaki metin Türkçe bir dersin dökümüdür.
        Döküm, bir makine öğrenimi modeli tarafından yapılmıştır ve %100 doğru olmayabilir.
        Katılımcıların sözlerinin yanı sıra arka plan gürültüsü veya dersin gidişatına dair açıklamalar içerebilir.
        Lütfen aşağıdaki dökümü okuyun ve kullanıcının sorusunu yanıtlayın.

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        Ders dökümünün içeriğine dayanarak lütfen aşağıdaki noktaları Türkçe olarak özetleyin.
        Markdown formatını kullanın, önemli noktaları **kalın** yazın ve başlıkları açıkça belirtin.

        ## 1. Ders Özeti
        ## 2. Derste Açıklanan Temel Noktalar
        ## 3. Dersin Sonuçları
        ## 4. Ders İçeriğiyle İlgili Diğer Notlar
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        Bu döküm çok uzun, lütfen ana noktaları koruyarak özetleyin.
        Bu döküm daha uzun bir metnin parçası olabilir.
        """
    )




class BengaliLecturePrompts(Enum):
    TRANSCRIBE_FORMAT: str = "{content} সম্পর্কিত লেকচারের ট্রান্সক্রিপশন।"
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        অনুগ্রহ করে প্রতিটি বিষয়ে 4-5টি বাক্যে বিস্তারিতভাবে ব্যাখ্যা করুন।
        নিম্নলিখিত পাঠ্যটি একটি বাংলা লেকচারের ট্রান্সক্রিপশন।
        এটি একটি মেশিন লার্নিং মডেল দ্বারা তৈরি, এবং এর নির্ভুলতা ১০০% নয়।
        এতে ব্যাকগ্রাউন্ড শব্দ বা লেকচারের অগ্রগতির বর্ণনা থাকতে পারে।
        অনুগ্রহ করে ট্রান্সক্রিপশনটি পড়ুন এবং ব্যবহারকারীর প্রশ্নের উত্তর দিন।

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        লেকচারের ট্রান্সক্রিপশনের বিষয়বস্তুর উপর ভিত্তি করে নিচের বিষয়গুলো বাংলায় সংক্ষেপে উপস্থাপন করুন।
        markdown ফরম্যাট ব্যবহার করুন, গুরুত্বপূর্ণ বিষয়গুলো **bold** করুন এবং শিরোনামগুলো স্পষ্ট করুন।

        ## 1. লেকচারের সারাংশ
        ## 2. লেকচারে ব্যাখ্য়া করা মূল পয়েন্টসমূহ
        ## 3. লেকচারের উপসংহার
        ## 4. লেকচারের বিষয়বস্তুর অন্যান্য নোটস
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        এই ট্রান্সক্রিপশনটি অনেক বড়, অনুগ্রহ করে মূল বিষয়বস্তু বজায় রেখে এটি সংক্ষিপ্ত করুন।
        মনে রাখবেন এটি একটি বড় ট্রান্সক্রিপশনের অংশ হতে পারে।
        """
    )

