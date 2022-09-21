# for reference use this website
# https://pytube.io/en/latest/user/install.html



# for only one video download
# ***video***

from pytube import YouTube

link = input("Enter the link for video download\n")

you = YouTube(link)

print("Title of video : ", you.title)

# print("Thumbnail url is: ", you.thumbnail_url)

# videoArray = you.streams.all() #for all stream
videoArray = you.streams.filter(only_audio=True) # for only audio stream
# videoArray=you.streams.filter(progressive=True)
# videoArray=you.streams.get_by_itag(22)

# vstream = list(enumerate(videoArray))

# for i in vstream:
#     print(i)

# stream = int(input("Enter the index number:\n"))

videoArray[1].download()

print("Download sucessful")

# for downloading all video playlist
# ***playlist***
#
# from pytube import Playlist, YouTube

# link = input("Enter the link for video playlist download\n")
# py = Playlist(link)

# # print("Title of Playlist: ", py.title)
# print(f'Downloading :{py.title}')

# for video in py.videos:
#     video.streams.get_highest_resolution().download()

# print("Download Playlist Sucessfully ")