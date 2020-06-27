from pathlib import Path
from tempfile import NamedTemporaryFile
import random
import time

from gtts import gTTS
import vlc

SECONDS_IN_TRIAD = 2

audio_buffer = NamedTemporaryFile(suffix='triad_type.mp3')


def say(statement):
    language = 'en'
    myobj = gTTS(text=statement, lang=language, slow=False)
    myobj.save(audio_buffer.name)
    p =vlc.MediaPlayer(f"file://{audio_buffer.name}")
    # Playing the converted file
    p.play()
    print(statement)
    time.sleep(SECONDS_IN_TRIAD)

triad_type = [
    "diminished",
    "augmented",
    "major",
    "minor",
    "suspended",
]

while True:
    say(random.choice(triad_type))

