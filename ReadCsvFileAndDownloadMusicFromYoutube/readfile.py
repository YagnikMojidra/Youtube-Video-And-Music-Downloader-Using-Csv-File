import csv
from pytube import YouTube

with open('mlink2.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    for line in (csv_reader):
        st=line[0]
        # print(st)
        # for only music download with the help of the csv file
        videoArray = YouTube(st).streams.filter(only_audio=True)
        videoArray[1].download()
        print("Music download is completed")

