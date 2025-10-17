import RPi.GPIO as GPIO
import time
import json
import os

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Your list of GPIO pins you want to test
gpio_pins = [2, 4, 7, 10, 9, 5, 8, 1]

# Setup pins
for pin in gpio_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

relay_map_file = "relay_map_to_gpio_pins.json"
relay_map = {}

# Load existing mapping if available
if os.path.exists(relay_map_file):
    with open(relay_map_file, "r") as f:
        relay_map = json.load(f)
    print("Loaded existing relay map:")
    for relay, pin in relay_map.items():
        print(f"Relay {relay} → GPIO {pin}")
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin, GPIO.LOW)

else:
    print("No relay_map.json found. Starting interactive assignment...")
    try:
        for pin in gpio_pins:
            input(f"\nPress Enter to test GPIO {pin}...")

            print(f"Pin {pin} HIGH (relay ON)")
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.5)

            GPIO.output(pin, GPIO.LOW)
            print(f"Pin {pin} LOW (relay OFF)")

            # Ask which relay number this pin controls
            while True:
                try:
                    relay_num = int(input(f"Which relay number (1–8) is on GPIO {pin}? "))
                    if relay_num < 1 or relay_num > 8:
                        print("Relay number must be between 1 and 8.")
                    else:
                        relay_map[relay_num] = pin
                        break
                except ValueError:
                    print("Please enter a number between 1 and 8.")

        # Save mapping to JSON
        with open(relay_map_file, "w") as f:
            json.dump(relay_map, f, indent=4)
        print("\nRelay mapping complete! Saved to relay_map.json")

    except KeyboardInterrupt:
        print("\nExiting before saving...")

    finally:
        GPIO.cleanup()
