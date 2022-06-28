import os
import random
from playsound import playsound

AUDIO_CLIP_DIR = "./audio/"
audio_clips = []

# Get filenames of audio clips in sub-dir
for root, dirs, files in os.walk(AUDIO_CLIP_DIR):
    for filename in files:
        if filename.lower().endswith((".mp3", ".wav")):
            audio_clips.append(filename)


rand = random.randint(0, len(audio_clips) - 1)

playsound(AUDIO_CLIP_DIR + audio_clips[rand])
