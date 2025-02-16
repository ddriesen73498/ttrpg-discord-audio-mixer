import sounddevice as sd
import numpy as np

# Update these with the actual device numbers from your list_devices.py output
MIC_DEVICE = 1  # Replace with your microphone device index
SYSTEM_AUDIO_DEVICE = 2  # Replace with your system audio device index (VB-Audio Virtual Cable)
OUTPUT_DEVICE = 3  # Replace with the virtual microphone device index

# Audio settings
SAMPLE_RATE = 44100  # Standard CD-quality sample rate
BUFFER_SIZE = 1024   # Buffer size for real-time mixing

def audio_callback(indata, outdata, frames, time, status):
    if status:
        print("Audio Stream Error:", status)

    mic_audio = indata[:, 0]  # Microphone input (mono)
    system_audio = indata[:, 1]  # System audio input (mono)

    # Simple volume mix (averaging)
    mixed_audio = (mic_audio + system_audio) / 2

    # Output mixed audio
    outdata[:] = np.column_stack((mixed_audio, mixed_audio))  # Convert back to stereo

# Start the real-time audio mixing
with sd.Stream(device=(SYSTEM_AUDIO_DEVICE, OUTPUT_DEVICE),
               samplerate=SAMPLE_RATE,
               channels=2,
               callback=audio_callback,
               blocksize=BUFFER_SIZE):
    print("Streaming audio... Press Ctrl+C to stop.")
    while True:
        pass  # Keep the script running

