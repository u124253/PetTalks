import sys, os
path = 'C:/Users/tomas/Downloads/PetTalks/PetTalks gui-v0.0/gui-gui-v0/'

audios = os.listdir(path + "software/sounds/")

for audio in audios:
    audios[audios.index(audio)] = audio.split('.')[0]

print(audios[0] + ".wav")
str = 'button1'
print(str[-1])