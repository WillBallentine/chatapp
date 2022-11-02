from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys

recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProptery('rate', 150)

todo_list = ['Go shopping', 'clean room']

mappings = {'greeting': }

assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()



assistant.request()