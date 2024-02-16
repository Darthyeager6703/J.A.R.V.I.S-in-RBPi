# import os
# import re
# import requests
# import urllib.parse
# import urllib.request
# from bs4 import BeautifulSoup
#
# music_name = "Linkin Park Numb"
# query_string = urllib.parse.urlencode({"search_query": music_name})
# formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
#
# search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
# clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
# clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
#
# inspect = BeautifulSoup(clip.content, "html.parser")
# yt_title = inspect.find_all("meta", property="og:title")
#
# for concatMusic1 in yt_title:
#     pass
#
# print(concatMusic1['content'])
#
# mpv_path = r'"C:\Program Files\mpv\mpv.exe"'
# command = f"{mpv_path} {clip2} --no-video --loop=inf --input-ipc-server=\\\\.\\pipe\\mpv-pipe"
#
# # Use os.system to run the command and wait for it to complete
# os.system(command)
import os
import yt_dlp

def play_song(song_name):
    # The query to search for
    query = song_name

    # Options for yt_dlp
    options = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True
    }

    # Use yt_dlp to scrape the song link
    with yt_dlp.YoutubeDL(options) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
            url = info['webpage_url']
        except Exception:
            return "Couldn't find the song."

    # Use the os.system command to open the song in MPV
    os.system(f"mpv {url}")

    return "Playing the song."

# Test the function
# song_name = input("Enter the song name: ")
# print(play_song(song_name))
