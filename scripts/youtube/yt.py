from pytube import YouTube
import asyncio
import time
import requests
import ffmpeg
import os


async def download(video_url):
    show_progress = True
    yt = YouTube(video_url, on_progress_callback=show_progress)
    stream = yt.streams.filter(only_audio=True).first()
    ffmpeg.input(stream.url, ss=0, t=yt.length).output('/data/output/{}.mp4'.format(yt.title)).run()
    print('length', yt.length)
    print("Download finished")


async def cli():
    print(f"started at {time.strftime('%X')}")
    # get the current directory
    current_dir = os.getcwd()

    # create the full path for the links.txt file
    links_file_path = os.path.join("/data/scripts/youtube", 'links.txt')

    # read the links from the links.txt file and download the videos
    with open(links_file_path, 'r') as f:
        for line in f:
            await download(line.strip())

def main():
    asyncio.run(cli())

if __name__ == '__main__':
    main()
