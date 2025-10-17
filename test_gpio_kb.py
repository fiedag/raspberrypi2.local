import RPi.GPIO as GPIO
import time

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Safe GPIO pins for output (exclude power, ground, and reserved pins)
gpio_pins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
             20, 21, 23, 24, 25, 26, 27]

# Setup all pins as outputs and start LOW
for pin in gpio_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

print("Cycling through GPIO pins one at a time.")
print("Press Enter to test the next pin, or Ctrl+C to stop.")

try:
    while True:
        for pin in gpio_pins:
            input(f"\nPress Enter to test GPIO {pin}...")

            print(f"Pin {pin} HIGH")
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(2.5)

            GPIO.output(pin, GPIO.LOW)
            print(f"Pin {pin} LOW")

except KeyboardInterrupt:
    print("\nExiting and cleaning up...")

finally:
    GPIO.cleanup()


