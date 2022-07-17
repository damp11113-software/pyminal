import youtube_dl
import os
import time


def main():
    print('--------------------Format--------------------')
    print('mp3 = 192')
    print('m4a = 140')
    print('mp4 144p = 160')
    print('mp4 240p = 133')
    print('mp4 360p = 134')
    print('mp4 480p = 135')
    print('mp4 720p = 136')
    print('mp4 1080p = 137')
    print('gp3 176x144 = 17')
    print('gp3 320x240 = 36')
    print('flv = 5')
    print('webm = 43')
    print('mp4 640x360 = 18')
    print('mp4 1280x720 = 22')
    print('webm 3840x2160 2160p = 313')
    print('webm 3840x2160 60fps 2160p60 = 315')
    print('----------------------------------------------')

    url = input('url: ')
    Format = input('Format: ')

    print('start...')
    if Format == '192':
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    elif Format == '140':
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
                'preferredquality': '140',
            }],
        }
    else:
        ydl_opts = {
        'format': f'{Format}+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s.%(ext)s'
        }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except:
        print(f'fail to download {url}')


main()