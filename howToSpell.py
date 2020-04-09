import speech_recognition as sr
import os
import random
import time

def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"
    return response

def spellWord(word):
    leng = len(word)
    n = 0
    os.system("say " + word)
    while n<leng:
        if word[n] == ' ':
            os.system("say space")
        else:
            os.system("say " + word[n])
        n+=1
    os.system("say " + word)

    
if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print("Working...")
    time.sleep(1)

    print("Say the word you want to spell.")
    said = recognize_speech_from_mic(recognizer,microphone)
    if said["transcription"]:
        print("you said ", said["transcription"])
        word = said["transcription"].lower()
        spellWord(word)