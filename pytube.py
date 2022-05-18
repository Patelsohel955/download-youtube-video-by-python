from pytube import YouTube
url = input("url name") # for giving input of url to download video
link = url
video = YouTube(link)
print(video.title)
youtube = video.streams.all()
vid = list(enumerate(youtube))
for i in vid:
    print(i)
stream = int(input("Enter the stream format as 0,1,2, .... as per vedio quality"))
youtube[stream].download()
print('sucessfully downloaded')
