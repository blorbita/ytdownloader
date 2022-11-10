from pytube import YouTube
from sys import argv

link = argv[1]
YT_LINK = YouTube(link)

print('Title: ', YT_LINK.title)

print("Views: ", YT_LINK.views)

yd = YT_LINK.streams.get_highest_resolution()

yd.download('D:\YT_downloads')