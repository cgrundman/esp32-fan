# esp32-fan
Code for simple I/O control of a 5V fan.

## Setup

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate
```

## Deployment

The .py files in the esp32-code folder are the software that runs on the ESP32.

To flash micropython to the ESP32:

```bash
esptool --port /dev/ttyUSB0 erase-flash
esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 write-flash -z 0x1000 ./ESP32_GENERIC-20250911-v1.26.1.bin
```

To upload a file to the ESP32: 
```bash
mpremote connect /dev/ttyUSB0 fs cp main.py :main.py
```

To run a file from the computer without saving it on the ESP32:
```bash
mpremote connect /dev/ttyUSB0 run test.py
```

To enter REPL: 
```bash
mpremote connect /dev/ttyUSB0
    In REPL: ctrl+d for soft reboot
```

To see which device is connected to which port:
```bash
ls -l /dev/serial/by-id/
```
