#author=AlphaSue
#date=20230116
#task='use whisper to auto generate video scripts'
#methods: python convert.py 苹果通用控制.webm apple2
#whisper github: https://github.com/openai/whisper
from datetime import timedelta
import os
import whisper
import sys

def transcribe_audio(path, output):
    model = whisper.load_model("large") # Change this to your desired model /
    # we can choose from tiny, base, small, medium, large.
    print("Whisper model loaded.")
    transcribe = model.transcribe(audio=path)
    segments = transcribe['segments']
    print(segments)
    for segment in segments:
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        segmentId = segment['id']+1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"
        print(segment)
        #srtFilename = os.path.join("SrtFiles", f"VIDEO_FILENAME.srt")
        srtFilename = output+'.srt'
        with open(srtFilename, 'a', encoding='utf-8') as srtFile:
        #with open(output+'.srt', 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment)
    return srtFilename

def main():
    path = sys.argv[1]
    output = str(sys.argv[2])
    res = transcribe_audio(path, output)
    print(res)

if __name__ == '__main__':
    main()


