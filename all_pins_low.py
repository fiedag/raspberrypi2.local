import RPi.GPIO as GPIO

# Use BCM numbering
GPIO.setmode(GPIO.BCM)

# List of GPIO pins you want to pull LOW on startup
gpio_pins = [2, 3, 4, 17, 27, 22, 10, 9, 11,
             5, 6, 13, 19, 26, 14, 15, 18,
             23, 24, 25, 8, 7, 12, 16, 20, 21]

# Set each pin as output and pull LOW
for pin in gpio_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

print("All GPIO pins set to LOW.")

