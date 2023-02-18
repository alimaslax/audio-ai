# audio-ai
docker build -t audio-ai ./
docker run --rm -it --name=audio-ai -v $(PWD)/music/input:/data/input -v $(PWD)/music/output:/data/output -v $(PWD)/demucs/models:/data/models -v $(PWD)/scripts:/data/scripts audio-ai /bin/bash

## yt
Add Links To End of Line Seperated links.txt
```
youtube
```
## Demucs

Mac OSX
```
demucs --two-stem=vocals /data/input/song.mp4
mv ./separated/htdemucs/song/no_vocals.wav /data/output/
mv ./separated/htdemucs/song/vocals.wav /data/output/
```

## Whisper

Mac OSX
```
whisper --model small.en 
```