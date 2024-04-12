import speech_recognition as sr

r = sr.Recognizer()

def listen_for_wake_word(source):
  print("Listening for keyword")

  while True:
      audio = r.listen(source)
      try:
          text = r.recognize_google(audio)
          print(text)

      except sr.UnknownValueError:
          pass

with sr.Microphone() as source:
  listen_for_wake_word(source)