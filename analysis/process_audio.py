import os

print("Current working directory:", os.getcwd())
raw_path = "../raw_audio"
if os.path.exists(raw_path):
    print("Found raw_audio folder")
    wav_files = [f for f in os.listdir(raw_path) if f.endswith(".wav")]
    print("Found WAV files:", wav_files)
else:
    print("raw_audio folder not found!")
    wav_files = []
    
import json
import librosa

for file in wav_files:
    wav_path = os.path.join(raw_path, file)
    print("Processing:", wav_path)
    
    # Load the audio
    y, sr = librosa.load(wav_path, sr=None)
    
    # Prepare JSON data
    data = {
        "file": file,
        "sample_rate": sr,
        "amplitude": y.tolist()
    }
    
    # Save to processed folder
    processed_path = os.path.join("../processed", file.replace(".wav", ".json"))
    with open(processed_path, "w") as f:
        json.dump(data, f)
    
    print("Saved JSON:", processed_path)
import json
import librosa
import os

raw_path = "../raw_audio"

for file in os.listdir(raw_path):
    if not file.endswith(".wav"):
        continue

    wav_path = os.path.join(raw_path, file)
    print("Processing:", wav_path)

    # Load audio
    y, sr = librosa.load(wav_path, sr=None)

    # Prepare JSON data
    data = {
        "file": file,
        "sample_rate": sr,
        "amplitude": y.tolist()
    }

    # Save to processed folder
    processed_path = os.path.join("../processed", file.replace(".wav", ".json"))
    with open(processed_path, "w") as f:
        json.dump(data, f)

    print("Saved JSON:", processed_path)

