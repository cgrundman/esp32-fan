import serial
import time
import re

ESP32_PORT = "/dev/ttyUSB0"
BAUD = 115200
LOG_FILE = "esp32/esp32_log.txt"

# --- Open serial connection ---
ser = serial.Serial(ESP32_PORT, BAUD, timeout=1)
time.sleep(2)  # Let the board settle

# --- Send command to run main.py ---
ser.write(b"\r\nimport main\r\n")
#time.sleep(0.1)

# --- Read and log output ---
with open(LOG_FILE, 'a') as f:
    try:
        while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line:
                luminance = re.findall(r'\d+\.\d+',line)[0] #just the number
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                log_line = f"{timestamp}, {line}"
                print(log_line)
                f.write(log_line + '\n')
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        ser.close()