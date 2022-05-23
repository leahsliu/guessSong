import json
import requests
from IPython.display import display, Audio, clear_output

def getURL(term):
    keyVals = {'term':term, 'media':'music'}
    link = requests.get('https://itunes.apple.com/search', params=keyVals)
    return link.json()

def write(data):
    with open('json_data.json','w') as outfile:
        json.dump(data, outfile)

def getListOfSongs():
    songlst = []
    while True:
        userInp = input('Enter the name of a band or artist (or "done" to exit): ')
        if userInp == 'done':
            return songlst
        else:
            data = getURL(userInp)
            songlst += data['results']
            print(len(songlst),'song total \n')

def playSong(data):
    audio_url = data[0]['previewUrl']
    Audio(url=audio_url)
    #display(Audio(audio_url, autoplay=True))

playSong(getListOfSongs())
