from gtts import gTTS
from playsound import playsound
from os import remove


def syn_speech(text):
    # Function uses google's gTTS package to synthesize any given speech
    # Accent codes can be found at https://gtts.readthedocs.io/en/latest/module.html#localized-accents

    file_name = "message.mp3"  # Name of mp3 file, prevents differences in commands

    # 3 parameters: text, languange, and accent.
    tts = gTTS(text, lang="en", tld="ca")  # Creates the message, I found the canadian accent to sound the best
    tts.save(file_name)  # Doesn't speak it, you have to save the speech to a MP3 file

    playsound(file_name)  # Plays the message
    remove(file_name)  # Deletes file to prevent clogging or data confusion
