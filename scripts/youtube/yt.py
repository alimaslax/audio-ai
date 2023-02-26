
import asyncio
import time
import requests
import ffmpeg
import os
import subprocess
import sys
from pytube import YouTube

async def download(video_url):
    show_progress = True
    yt = YouTube(video_url, on_progress_callback=show_progress)
    stream = yt.streams.filter().order_by('abr').desc().first()
    # set the output to stdout
    output = subprocess.PIPE
    # download the stream to stdout
    subprocess.run([stream.download()], stdout=output, shell=True)
    audio_type = stream.mime_type
    return audio_type

async def cli(links):
    print(f"started at {time.strftime('%X')}")

    # loop through the links and download the videos
    for link in links.split(','):
        return await download(link.strip())

def app(environ, start_response):
    # Get the request payload
    length = int(environ.get('CONTENT_LENGTH', '0'))

    links = environ.get('QUERY_STRING').split('=', 1)[1]
    print(links)

    # Run the main function
    audio_type = main(links)
    status = '200 OK'
    headers = [('Content-type', audio_type)]
    start_response(status, headers)

    # Return the contents of the WAV file as the response body
    output = subprocess.PIPE
    return [output.stdout.decode()]

def main(links):
    return asyncio.run(cli(links))


asyncio.run(cli('https://www.youtube.com/watch?v=w07DANgC6wA'))