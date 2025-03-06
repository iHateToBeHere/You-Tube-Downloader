from pytubefix import YouTube
from pytubefix.cli import on_progress
from inputs import *

def url_data():
    yt = YouTube(YouTube_URL,on_progress_callback=on_progress)
    return yt