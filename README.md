# ESP32 Fan

Code for simple I/O control of a 5V fan.

## Setup

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate
```

Download the correct packages:

```bash
pip install --upgrade pip setuptools wheel
pip install esptool mpremote
```

Test downloaded packages:
```bash
which esptool.py
which mpremote
esptool.py version
mpremote version
```

## Deployment

The .py files in the esp32-code folder are the software that runs on the ESP32.

Test the connection port for the ESP32 (usually USB0):
```bash
ls /dev/ttyUSB*
```

To flash micropython to the ESP32:

```bash
esptool --chip esp32 --port /dev/ttyUSB0 erase_flash
esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 write-flash -z 0x1000 ./ESP32_GENERIC-20250911-v1.26.1.bin
```

To upload a file to the ESP32: 
```bash
mpremote connect /dev/ttyUSB0 fs cp main.py :main.py
mpremote connect /dev/ttyUSB0 reset
```

## Resources

[.bin](https://micropython.org/download/ESP32_GENERIC/) file for programming the board.
