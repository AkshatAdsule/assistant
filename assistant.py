import speech_recognition as sr
from howToSpell import recognize_speech_from_mic as rs
from howToSpell import spellWord
from voiceSearch import search
from game import game
from os import system
import sys


def getCommand():
    print("Say a command")
    system("say "  + "Start")
    said = rs(recognizer, microphone)
    while not said in ["search", "play", "spell"]:
        if said["transcription"]:
            break
        if not said["success"]:
            break
        print("I didn't catch that. What did you say?\n")
        system("say " + "I didn't catch that. What did you say?")
        getCommand()
        
    query = said["transcription"].lower()
    split = query.split(" ")
    if split[0] == "search":
        search(query.partition("search")[2])
    elif split[0] == "play":
        game(recognizer,microphone)
    elif split[0] == "spell":
        spellWord(query.partition("spell ")[2])
    elif split[0] == "exit":
        sys.exit()

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print("Working...")

    while True:
        getCommand()