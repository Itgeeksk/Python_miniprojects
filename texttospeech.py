from gtts import gTTS
import os


user_inp = input("Enter the text which you want to convert: ")
def convert():
    word = gTTS(text = user_inp, lang='en')
    filename = "Texttospeech.mp3"
    word.save(filename)
    os.system(f"start {filename}")

convert()