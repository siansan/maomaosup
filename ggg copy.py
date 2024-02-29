from google.oauth2 import service_account
from google.cloud import speech
import speech_recognition

client_file='C:/Users/sian/Desktop/test/new_mem_nobg/sianporject-e1d148b0e481.json'
# credentials=service_account.Credentials.from_service_account_file(client_file)
client=speech.SpeechClient.from_service_account_file(client_file)

print(0)
    
config=speech.RecognitionConfig(
encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
sample_rate_hertz=44100,
language_code="zh-TW",
)
r=speech_recognition.Recognizer()   
print('-----------')
with speech_recognition.Microphone() as source:
    # r.adjust_for_ambient_noise(source, duration=0.01)
    # print("a")
    r.adjust_for_ambient_noise(source, duration=0.01)
    audio = r.listen(source)
    # n=r.recognize_google(audio,language="zh_tw")
print(1)
with open("audio_file.wav","wb") as f:
    f.write(audio.get_wav_data())
print(2)    
with open("audio_file.wav","rb") as au:
    data=au.read()
    au=speech.RecognitionAudio(content=data)
    response=client.recognize(config=config,audio=au)
    for result in response.results:
        print((result.alternatives[0].transcript).replace(' ',''))
        
print(3)
    # n=r.recognize_google(audio,key="ad6415ee7029dd7f7b31faa5fd43e785137639b4")
    # n=n.replace(' ','')
    #language="zh_tw"
    # try:
    #     n=n.replace('1','e')
    # except:
    #     pass
    # print(n)