import sounddevice as sd

def list_audio_devices():
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        print(f"Device {i}: {device['name']} - {device['max_input_channels']} input channels, {device['max_output_channels']} output channels")

if __name__ == "__main__":
    list_audio_devices()
