import pytube
import ctypes
from pystyle import *
ctypes.windll.kernel32.SetConsoleTitleW("Youtube Downloader | By https://github.com/TheCuteOwl")
url = input(Colorate.Horizontal(Colors.blue_to_green, 'Youtube URL : '))



resolution = input(Colorate.Horizontal(Colors.blue_to_green, '''What resolution do you want ?
 1 = Highest Resolution
 2 = Lowest
 3 = Audio
'''))

yt = pytube.YouTube(url)

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
    yt.streams.get_highest_resolution().download()
    print('Succesfully downloaded' + yt.title + '.mp4 | with the best quality ')
elif resolution == '2':
    yt.streams.get_lowest_resolution().download()
    print('Succesfully downloaded' + yt.title + '.mp4 | with the lowest quality')
elif resolution == '3':
    yt.streams.get_audio_only().download(filename=yt.title + '.mp3')
    print('Succesfully downloaded' + yt.title + '.mp3')
