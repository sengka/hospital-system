from gtts import gTTS
import whisper
import os
import subprocess

def generate_tts():
    print("Generating TTS...")
    text = "Bu demo videosunda, geliştirdiğim Hastane Randevu Yönetim Sistemi'nin hasta, doktor ve admin akışlarını göreceksiniz."
    tts = gTTS(text=text, lang='tr')
    tts.save("audio_rst.mp3")
    
    # Find ffmpeg in WinGet packages
    ffmpeg_path = r"C:\Users\senag\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0-full_build\bin\ffmpeg.exe"
    
    if os.path.exists(ffmpeg_path):
        # Convert to wav
        subprocess.run([ffmpeg_path, "-i", "audio_rst.mp3", "-acodec", "pcm_s16le", "-ar", "44100", "audio_rst.wav", "-y"])
        print("TTS generated: audio_rst.wav")
    else:
        print(f"FFmpeg not found at {ffmpeg_path}, skipping WAV conversion")

def generate_subtitles():
    print("Generating Subtitles with Whisper (Small model)...")
    video_path = "cypress/videos/hospital_demo.cy.js.mp4"
    
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
        return

    model = whisper.load_model("small")
    result = model.transcribe(video_path, language="tr")
    
    # Write SRT manually
    with open("subtitles.srt", "w", encoding="utf-8") as f:
        for i, segment in enumerate(result["segments"]):
            start = format_timestamp(segment["start"])
            end = format_timestamp(segment["end"])
            text = segment["text"].strip()
            f.write(f"{i+1}\n")
            f.write(f"{start} --> {end}\n")
            f.write(f"{text}\n\n")
    
    print("Subtitles generated: subtitles.srt")

def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

if __name__ == "__main__":
    generate_tts()
    if os.path.exists("cypress/videos/hospital_demo.cy.js.mp4"):
        generate_subtitles()
    else:
        print("Video not found, skipping subtitles generation for now.")
