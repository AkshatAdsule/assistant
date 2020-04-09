import wikipedia
import os
import speech_recognition as sr
from howToSpell import recognize_speech_from_mic as rs
#import pyttsx
from gtts import gTTS 

def censor_string(txt, lst, char):
	return " ".join(char*len(word) if word in lst else word for word in txt.split() )

if __name__ == "__main__":
    #engine = pyttsx.init()
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print("Working...")

    print("Say what you want to search")
    said = rs(recognizer,microphone)
    if said["transcription"]:
        query = said["transcription"]
        print("Searching: " + said["transcription"])
        summary = wikipedia.summary(query,sentences=2)
        myobj = gTTS(text=summary, lang='en', slow=False) 
        myobj.save("welcome.mp3") 
        os.system("afplay welcome.mp3") 
        #engine.say(summary)
        #engine.runAndWait()

def search(query):
        summary = wikipedia.summary(query,sentences=2)
        myobj = gTTS(text=summary, lang='en', slow=False) 
        myobj.save("welcome.mp3") 
        os.system("afplay welcome.mp3")


    