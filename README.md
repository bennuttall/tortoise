# IoT: Internet of Tortoises

Collection of Python scripts running on a Raspberry Pi, used for looking after
[Leo the tortoise](https://twitter.com/leo_tortoise)

## Timed heat lamp

Uses Energenie to turn the heat lamp on between 9am and 6pm. Simple GPIO Zero
script.

## Web stream camera

Uses picamera and jsmpeg to stream video over the web (can be internal only or
external if port forwarding is configured). Modified version of
[pistreaming](https://github.com/waveform80/pistreaming)
