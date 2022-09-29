
from pytube import Playlist
import os
p= Playlist(input('Link: '))

named=input('folder name: ')
there=os.path.exists(f"D:/downloaded/{named}")
if there == False:
    mkdir(f"D:/downloaded/{named}")

res= input('pick a resolution 360p 720p or audio: ')
for vid in p.videos:
    if res=="360p" or res=="720p":
        try:
            print(f"video title: {vid.title}")
            print(vid.streams.filter(type="video", resolution=res, progressive=True).first().download(output_path=f"D:/downloaded/{named}/"))
        except:
            continue    
        
    else:
        try:
            print(f"audio title: {vid.title}")
            print(vid.streams.filter(mime_type="audio/mp4", type="audio", abr="128kbps", progressive=False).first().download(output_path=f"D:/downloaded/{named}/"))
        except:
            continue
    
    