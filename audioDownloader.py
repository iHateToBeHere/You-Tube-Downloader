from downloader import *
from inputs import *

def audio():
    print(f'\n[D] Downloading mp3 song [D]')
    yt = url_data()
    for index in yt.streams.filter(only_audio=True,abr=AUDIO_QUALITY).itag_index:
        audio_stream = yt.streams.get_by_itag(index)
        audio_stream.download(filename=f'{yt.title}.mp3')
   
    print(f'\n --- Download complete ---\n Saved File: {yt.title}')
