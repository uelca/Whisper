import whisper

# Lade das Whisper-Modell
model = whisper.load_model("large")

# Transkribiere die Audiodatei
result = model.transcribe("Pfad zum Interview", word_timestamps=True)

# Speicher als .txt file
with open("transciption.txt", "w") as f:
    f.write(result["text"])