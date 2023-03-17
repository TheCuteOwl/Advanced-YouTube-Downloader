from pytube import *
import ctypes
import requests

url = ''


def thumbnail():
    d = YouTube(url)
    img_data = requests.get(d.thumbnail_url).content

    with open('Thumbnail.jpg' 'wb') as handler:
        handler.write(img_data)
    input('Succesfully downloaded press enter to quit')
    quit()


def playlistdownload():
    p = input('Playlist URL :')
    playlist = Playlist(p)
    print(f'Downloading videos from : ' + str(playlist))
    resolution2 = input('''What resolution do you want ?
         1 = Highest Resolution
         2 = Lowest
         3 = Audio Only''')

    number = 0
    if resolution2 == '1':
        for video in playlist.videos:
            video.streams.get_highest_resolution().download()
            number += 1
            print('Downloaded : ' + str(number) + ' with the highest quality')
        input('Succesfully downloaded press enter to quit')
        quit()

    if resolution2 == '2':
        for video in playlist.videos:
            video.streams.get_lowest_resolution().download()
            number += 1
            print('Downloaded : ' + str(number) + ' with the lowest quality')
        input('Succesfully downloaded press enter to quit')
        quit()

    if resolution2 == '3':
        for video in playlist.videos:
            video.streams.get_audio_only().download(filename=video.title + '.mp3')
            number += 1
            print('Downloaded : ' + str(number) + ' videos from the playlist')
        input('Succesfully downloaded press enter to quit')
        quit()


def channeldownload():
    c = input('Youtube Channel URL')
    channel = Channel(c)
    print(f'Downloading videos by:' + channel.channel_name)
    number = 0
    resolution2 = input( '''What resolution do you want ?
     1 = Highest Resolution
     2 = Lowest
     3 = Audio Only''')

    if resolution2 == '1':
        for video in channel.videos:
            video.streams.get_highest_resolution().download()
            number += 1
            print('Downloaded : ' + str(number) + ' videos from ' + channel.channel_name + ' With the highest quality')

    elif resolution2 == '2':
        for video in channel.videos:
            video.streams.get_lowest_resolution().download()
            number += 1
            print('Downloaded : ' + str(number) + ' videos from ' + channel.channel_name + ' With the lowest quality')

    elif resolution2 == '3':
        for video in channel.videos:
            video.streams.get_audio_only().download(filename=video.title + '.mp3')
            number += 1
            print('Downloaded : ' + str(number) + ' videos from the playlist In the format mp3')

    else:
        print('Unvalid value')
        channeldownload()
    input('Downloaded every video on the Youtube Channel press enter to quit')
    exit()


Choosing = input( '''
 Do you want to download 1 video 
 or a whole channel video ? :
 [1] One video
 [2] A whole channel video
 [3] A whole playlist
 [4] Thumbnail''')


if Choosing == '1':
    url = input( 'Youtube URL (Video or Channe:l : ')
elif Choosing == '2':
    channeldownload()
elif Choosing == '3':
    playlistdownload()
elif Choosing == '4':
    url = input( 'Youtube URL : ')
    yt = pytube.YouTube(url)
    thumbnail()

ctypes.windll.kernel32.SetConsoleTitleW("Youtube Downloader | By https://github.com/TheCuteOwl")

resolution = input( '''What resolution do you want ?
 1 = Highest Resolution
 2 = Lowest
 3 = Audio
 
''')


if resolution == '1''2''3':
    def stuff():
        print(' Information about the video : ')
        print('Author : ' + yt.author)
        print('Channel Url : ' + yt.channel_url)
        print('Video Title : ' + yt.title)
        print('Is video restricted : ' + str(yt.age_restricted))
        print('Description : Will not be shown it take too many place')
        print('Number of views : ' + str(yt.views))
        print('Length of video : ' + str(yt.length) + 'seconds')
        print('Published date : ' + str(yt.publish_date))
        print('The video is getting downloaded... ')

if resolution == '1':
    yt = pytube.YouTube(url)
    yt.streams.get_highest_resolution().download()
    print('Succesfully downloaded' + yt.title + '.mp4 | with the best quality ')
elif resolution == '2':
    yt = pytube.YouTube(url)
    yt.streams.get_lowest_resolution().download()
    print('Succesfully downloaded' + yt.title + '.mp4 | with the lowest quality')
elif resolution == '3':
    yt = pytube.YouTube(url)
    yt.streams.get_audio_only().download(filename=yt.title + '.mp3')
    print('Succesfully downloaded' + yt.title + '.mp3')
