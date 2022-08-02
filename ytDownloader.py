from pytube import YouTube
from sys import argv

link = argv[0]
yt = YouTube(link)
print("title :", yt.title)
print("view :", yt.view)

yd = yt.streams.get_highest_resolution()

yd.download('./User/lulam/Videos')
