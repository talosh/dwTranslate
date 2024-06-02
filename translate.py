import pulsectl

from pprint import pprint

import pulsectl

def list_pulseaudio_sinks():
    with pulsectl.Pulse('python-pulse-control') as pulse:
        sinks = pulse.sink_list()
        for sink in sinks:
            print(f"Serial.device.serial: {sink.proplist['Serial.device.serial']}")
            '''
            print(f"Sink Name: {sink.name}")
            print(f"Description: {sink.description}")
            print(f"Index: {sink.index}")
            print(f"State: {sink.state}")
            print(f"Sample Specification: {sink.sample_spec}")
            # print(f"Channel Map: {sink.channel_map}")
            print(f"Volume: {sink.volume}")
            print(f"Muted: {sink.mute}")
            print(f"Monitor Source: {sink.monitor_source}")
            print(f"Monitor Source Name: {sink.monitor_source_name}")
            print(f"Latency: {sink.latency}")
            print(f"Driver: {sink.driver}")
            print(f"Flags: {sink.flags}")
            print(f"Properties: {sink.proplist}")
            print(f"Configured Latency: {sink.configured_latency}")
            print(f"Base Volume: {sink.base_volume}")
            # print(f"Sink Input By: {sink.sink_input_by}")
            print(f"Module Index: {sink.owner_module}")
            print("-" * 40)
            '''

if __name__ == "__main__":
    list_pulseaudio_sinks()
