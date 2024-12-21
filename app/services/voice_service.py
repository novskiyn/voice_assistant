import speech_recognition as sr

class VoiceService:
    def recognize_speech(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Говорите:")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="ru-RU")
                print(f"Вы сказали: {text}")
                return text
            except sr.UnknownValueError:
                print("Не удалось распознать речь")
                return None
            except sr.RequestError as e:
                print(f"Ошибка запроса: {e}")
                return None
