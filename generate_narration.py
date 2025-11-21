from gtts import gTTS
import os
import subprocess

def generate_narration():
    print("Generating English narration...")
    
    # Read the narration script
    with open("narration_script.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
    # Generate TTS in English
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("narration_audio.mp3")
    
    # Find ffmpeg
    ffmpeg_path = r"C:\Users\senag\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0-full_build\bin\ffmpeg.exe"
    
    if os.path.exists(ffmpeg_path):
        # Convert to wav
        subprocess.run([ffmpeg_path, "-i", "narration_audio.mp3", "-acodec", "pcm_s16le", "-ar", "44100", "narration_audio.wav", "-y"])
        print("Narration audio generated: narration_audio.wav")
    else:
        print(f"FFmpeg not found, skipping WAV conversion")

def generate_subtitles():
    print("Generating English subtitles from script...")
    
    # Read the narration script
    with open("narration_script.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
    # Split into paragraphs
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    
    # Create SRT file with timing based on text length
    # Approximate: 150 words per minute = 2.5 words per second
    with open("narration_subtitles.srt", "w", encoding="utf-8") as f:
        current_time = 0
        for i, paragraph in enumerate(paragraphs):
            words = len(paragraph.split())
            duration = max(3, words / 2.5)  # At least 3 seconds per subtitle
            
            start = format_timestamp(current_time)
            end = format_timestamp(current_time + duration)
            
            f.write(f"{i+1}\n")
            f.write(f"{start} --> {end}\n")
            f.write(f"{paragraph}\n\n")
            
            current_time += duration
    
    print("Subtitles generated: narration_subtitles.srt")

def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

if __name__ == "__main__":
    generate_narration()
    generate_subtitles()
