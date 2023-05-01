from pytube import YouTube, Playlist
from srt import change
import time
import os


start_time = time.time()

def choose_path():
    available_directories = os.listdir("../youtube/yt_files")
    dircetory_map = []
    for x,y in enumerate(available_directories):
        dircetory_map.append({x:y})
    
    for x,y in enumerate(dircetory_map):
        print(f"Enter {x} to save your video to {y[x]}")
    print(f"Enter {len(dircetory_map) + 1} to create a new folder for your video")
    
    while True:
        try:
            command = int(input("Select one of the folders to store your video > "))
            if command > len(dircetory_map) + 1 or command < 0:
                raise ValueError
            else:
                break
        except Exception as err:
            print("Wrong input caused this exception {err}") 
            continue   
    try:
        if command == len(dircetory_map) +1:
            return f"yt_files/{input(f'Input your prefered name for your folder > ')}"
        return f'yt_files/{dircetory_map[(command)][(command)]}'
    except (SystemError, ValueError) as ess:
        UserWarning("Try using correct format and using numbers ==> {ess}" )
      



def download_video(link):

    yt = YouTube(link)
    path = choose_path()
    print(f"Attempting to download {yt.title}")
    yt.streams.filter(res="720p").first().download(output_path=path)
    print(f"Completed downloading {yt.title}")
    print("Downloading subtitle")
    change(link=link, name=yt.title, path=path)
    print("Done downloading subtitle")
   
      


def download_playlist(link):
    p = Playlist(link)
    print(f'Downloading: {p.title}')
    for video in p.videos:
        # video.streams.first().download()
        try:
            video.streams.get_highest_resolution().download(output_path=choose_path())
            print(f'Downloading: {video.title}')
        except Exception as err:
            print(video.title)
            print(f"An exception {err} occured")


def loop(links, type="1"):
    
    if type == "1":
        for x in links:
            try:
                download_video(x)
            except Exception as err:
                print(f"An exception occured ==> {err}")
            print("Next ====> ")
    else:
        for x in links:
            download_playlist(x)


links = []


def run():
    mode = input("1 == video -----------------------  2 === Playlist:  ")

    while True:
        try:
            links.append(str(input("Input link to video: ")))
            if input("Enter 0 to start download > ") == "0":
                break
        except Exception as err:
            print(f"{err} happened try again")
            continue
    
    if mode in "12":
        loop(type=mode, links=links)
    else:
        Warning("Fatal: Input correct mode")



run()


end_time = time.time()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.2f} seconds")
