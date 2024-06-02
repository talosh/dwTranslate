import pulsectl

def list_pulse_audio_devices():
    pulse = pulsectl.Pulse('device-list')
    devices = pulse.sink_list() + pulse.source_list()  # Sinks are output devices, sources are input devices
    for device in devices:
        print(f"Device Name: {device.name}")
        print(f"Description: {device.description}")
        print(f"Index: {device.index}")
        # print(f"Sample Rate: {device.sample_rate}")
        print(f"Channels: {device.channel_count}")
        print(f"Volume: {device.volume.values}")
        print(f"Muted: {device.mute}")
        print()

if __name__ == "__main__":
    list_pulse_audio_devices()
