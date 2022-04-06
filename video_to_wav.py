import os
import speech_recognition as sr

def generate_wav(obj,filepath):
    obj.my_progress['value']=40
    command2mp3 = 'ffmpeg -i '+ filepath + ' interim_audio.mp3'
    obj.my_progress['value']=60
    command2wav = 'ffmpeg -i interim_audio.mp3 interim_audio.wav'
    obj.my_progress['value']=80
    os.system(command2mp3)
    os.system(command2wav)



