from pydub import AudioSegment
from os import listdir
from audiostretchy.stretch import stretch_audio
import os



def combineAudioFiles(folder_path:str, saveName, speedRate = 1.0):
    os.makedirs("out", exist_ok=True)
    audio_files = [f for f in listdir(folder_path) if f.endswith((".mp3", ".wav", ".ogg"))]
    audio_segments = [AudioSegment.from_file(folder_path + "/" + f) for f in audio_files]
    combined_audio = AudioSegment.empty()
    for segment in audio_segments:
        combined_audio += segment
    
    combined_audio.export(f"tem/audio/{saveName}.mp3", format="mp3")
    
    if(speedRate != 1.0):
        stretch_audio(f"tem/audio/{saveName}.mp3", f"out/{saveName}_speed.mp3", ratio=1/speedRate)
        return
    
    combined_audio.export(f"out/{saveName}.mp3", format="mp3")  # Choose your desired format
    