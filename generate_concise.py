from gtts import gTTS
import os
import subprocess

def generate_concise_narration():
    print("Generating concise English narration...")
    
    # Read the narration script
    with open("narration_concise.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
    # Generate TTS in English
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("narration_concise.mp3")
    
    # Find ffmpeg
    ffmpeg_path = r"C:\Users\senag\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0-full_build\bin\ffmpeg.exe"
    
    if os.path.exists(ffmpeg_path):
        # Convert to wav
        subprocess.run([ffmpeg_path, "-i", "narration_concise.mp3", "-acodec", "pcm_s16le", "-ar", "44100", "narration_concise.wav", "-y"])
        print("Concise narration audio generated: narration_concise.wav")
    else:
        print(f"FFmpeg not found, skipping WAV conversion")

def generate_concise_subtitles():
    print("Generating concise English subtitles...")
    
    # Read the narration script
    with open("narration_concise.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
    # Split into lines (each line is a subtitle)
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    # Create SRT file with timing
    # Approximate timing: 2.5 seconds per line
    with open("narration_concise.srt", "w", encoding="utf-8") as f:
        current_time = 0
        for i, line in enumerate(lines):
            words = len(line.split())
            duration = max(2, words / 2.5)  # At least 2 seconds per subtitle
            
            start = format_timestamp(current_time)
            end = format_timestamp(current_time + duration)
            
            f.write(f"{i+1}\n")
            f.write(f"{start} --> {end}\n")
            f.write(f"{line}\n\n")
            
            current_time += duration
    
    print("Concise subtitles generated: narration_concise.srt")

def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

if __name__ == "__main__":
    generate_concise_narration()
    generate_concise_subtitles()
