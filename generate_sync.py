from gtts import gTTS
import os
import subprocess

def generate_sync_narration():
    print("Generating synchronized narration...")
    
    # Read the narration script
    with open("sync_narration.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
    # Generate TTS in English with slower speed for better sync
    tts = gTTS(text=text, lang='en', slow=True)
    tts.save("sync_narration.mp3")
    
    # Find ffmpeg
    ffmpeg_path = r"C:\Users\senag\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0-full_build\bin\ffmpeg.exe"
    
    if os.path.exists(ffmpeg_path):
        # Convert to wav
        subprocess.run([ffmpeg_path, "-i", "sync_narration.mp3", "-acodec", "pcm_s16le", "-ar", "44100", "sync_narration.wav", "-y"])
        
        # Get audio duration
        result = subprocess.run([ffmpeg_path, "-i", "sync_narration.wav"], 
                              capture_output=True, text=True, stderr=subprocess.STDOUT)
        print("Audio generated: sync_narration.wav")
        print(result.stdout)
    else:
        print(f"FFmpeg not found")

if __name__ == "__main__":
    generate_sync_narration()
