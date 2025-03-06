from downloader import *
from moviepy.editor import VideoFileClip, AudioFileClip
from inputs import *


def mixer(title,a,v):
    print(f'\n[i] Mixing video and audio')

    video_clip = VideoFileClip(v)
    audio_clip = AudioFileClip(a)

    video_clip = video_clip.set_audio(audio_clip)
    video_clip.write_videofile(title, codec="libx264", audio_codec="aac")

    print(f'\n---- Mixing Completed ----\n---- Saved File: {title}\n')

def video():
    print(f'\n[D] Downloading video [D]')
    yt = url_data()

    for index in yt.streams.filter(only_audio=True,abr=AUDIO_QUALITY).itag_index:
        audio_stream = yt.streams.get_by_itag(index)
        audio_stream.download(filename=f'audio.mp3')

    for index in yt.streams.filter(only_video=True, res=VIDEO_QUALITY).itag_index:
        video_stream = yt.streams.get_by_itag(index)
        video_stream.download(filename=f'video.mp4')

    print(f'\n[C] Download complete. ')
    mixer(f'{yt.title}.mp4', 'audio.mp3', 'video.mp4')