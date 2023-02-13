from pydub import AudioSegment
from pydub.utils import which
from gtts import gTTS
import datetime
import time
from pydub import AudioSegment 
from playsound import playsound 

AudioSegment.converter = which("ffmpeg")
text = "Digite Seu texto."
tts = gTTS(text=text, lang='pt')
tts.write_to_fp(open("sample.mp3", "wb"))
sound = AudioSegment.from_file("sample.mp3", format="mp3")
sound.export("sample2.wav", format="wav")

def alarm(hours, minutes,sound):
    current_time = datetime.datetime.now()
    alarm_time = current_time.replace(hour=hours, minute=minutes, second=0, microsecond=0)
    if alarm_time < current_time:
        alarm_time = alarm_time + datetime.timedelta(days=1)

    while datetime.datetime.now() < alarm_time:
        time.sleep(1)
    playsound('<Digite o caminho do arquivo>')

hours = int(input("Digite as horas para o despertador (0-23): "))
minutes = int(input("Digite os minutos para o despertador (0-59): "))
alarm(hours, minutes, sound)


