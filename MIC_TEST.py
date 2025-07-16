import pyaudio
import wave

# Audio settings
CHUNK = 1024
FORMAT = pyaudio.paInt16  # 16-bit resolution
CHANNELS = 1              # Mono input
RATE = 44100              # 44.1kHz sampling rate
RECORD_SECONDS = 5        # Duration to record
WAVE_OUTPUT_FILENAME = "test_audio.wav"

print("🔴 Recording for", RECORD_SECONDS, "seconds...")

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

frames = []

for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("✅ Recording complete.")

# Stop and close stream
stream.stop_stream()
stream.close()
p.terminate()

# Save to WAV file
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print(f"🎧 Saved as {WAVE_OUTPUT_FILENAME}. You can play it to verify.")
