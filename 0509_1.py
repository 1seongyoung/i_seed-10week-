from gtts import gTTS
import playsound

tts = gTTS("I am going to school",lang = 'en')
tts.save("mySound1.mp3")

