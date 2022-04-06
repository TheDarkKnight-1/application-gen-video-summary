from time import sleep
from wav_to_text import generate_text
from video_to_wav import generate_wav
import requests
import json
# from pathlib import Path

# filename = Path("C:\\Users\\cmishra2\\Downloads\\video_summary_gen\\project\\Introduction_to_Memory.mp4")
def find_summary(obj,filepath):
    
    generate_wav(obj,filepath)
    generate_text()
    obj.my_progress['value']=80
    f=open('output.txt','r')
    text=f.read()
    url = "https://8000-thedarkknight1-summaryge-m8pv6gswxju.ws-us38.gitpod.io/summary/"

    payload = json.dumps({
    "text": text
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    sleep(3)
    obj.my_progress['value']=100
    print(response.text)
    return response.text
    


# find_summary("C:\\Users\\cmishra2\\Downloads\\video_summary_gen\\project\\Introduction_to_Memory.mp4")
