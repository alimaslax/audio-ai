# audio-ai

## yt

## Demucs

Mac OSX
```
docker build -t demucs ./
docker run --rm -it --name=demucs -v $(PWD)/music/input:/data/input -v $(PWD)/music/output:/data/output -v $(PWD)/demucs/models:/data/models -v $(PWD)/scripts:/data/scripts demucs /bin/bash
demucs --two-stem=vocals /data/input/song.mp4
mv ./separated/htdemucs/song/no_vocals.wav /data/output/
mv ./separated/htdemucs/song/vocals.wav /data/output/
```

## Whisper

Mac OSX
```
whisper --model small.en 
```