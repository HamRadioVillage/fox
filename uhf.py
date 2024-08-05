import board
import digitalio
import time
import busio
import adafruit_rfm69



# Message to TX.
MORSE_MESSAGE = "K0HRV IR FOX 1"
PACKET_MESSAGE = "IT'S A SECRET"

# Seconds to wait before repeating.
DELAY = 10 


# Timing.  Generally you should only adjust the dit length.
DIT_LENGTH = 0.2
DAH_LENGTH = DIT_LENGTH * 3
SPACE_LENGTH = DIT_LENGTH * 7
BIT_SPACE_LENGTH = DIT_LENGTH
CHARACTER_SPACE_LENGTH = DAH_LENGTH

MORSE_CODE = { 
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.', 
    'G':'--.', 
    'H':'....',
    'I':'..', 
    'J':'.---', 
    'K':'-.-',
    'L':'.-..', 
    'M':'--', 
    'N':'-.',
    'O':'---', 
    'P':'.--.', 
    'Q':'--.-',
    'R':'.-.', 
    'S':'...', 
    'T':'-',
    'U':'..-', 
    'V':'...-', 
    'W':'.--',
    'X':'-..-', 
    'Y':'-.--', 
    'Z':'--..',
    '1':'.----',
    '2':'..---', 
    '3':'...--',
    '4':'....-', 
    '5':'.....', 
    '6':'-....',
    '7':'--...', 
    '8':'---..', 
    '9':'----.',
    '0':'-----', 
    ', ':'--..--', 
    '.':'.-.-.-',
    '?':'..--..', 
    '/':'-..-.', 
    '-':'-....-',
    '(':'-.--.', 
    ')':'-.--.-',
    ' ':' ' # Define space character as valid character
}

MORSE_BITS = {
  ".": DIT_LENGTH,
  "-": DAH_LENGTH
}


def send_message(message):
  
  for character in message:
    if character == " ":
        time.sleep(SPACE_LENGTH)
        continue
    character_bits = MORSE_CODE[character]
    for bit in character_bits:
        transmit(MORSE_BITS[bit])
        time.sleep(BIT_SPACE_LENGTH)
    time.sleep(CHARACTER_SPACE_LENGTH)

def transmit(duration):
    print("Transmitting packet message %s for %r seconds" % (PACKET_MESSAGE, duration))
    led.value = True
    start = time.monotonic()
    end = start + duration
    while time.monotonic() < end:
      rfm69.send(PACKET_MESSAGE)
    led.value = False


# Setup LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Setup the radio
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.RFM69_CS)
reset = digitalio.DigitalInOut(board.RFM69_RST)
rfm69 = adafruit_rfm69.RFM69(spi, cs, reset, 433.0)

count = 0

while True:
    send_message(MORSE_MESSAGE)
    count += 1
    print("Transmitted ""%s"" %r times" % (MORSE_MESSAGE, count))
    time.sleep(DELAY)