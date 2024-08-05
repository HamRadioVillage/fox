import time
import board
import digitalio

# Message to TX.
MESSAGE = "K0HRV IR FOX 1"

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
        irled.value = True
        time.sleep(MORSE_BITS[bit])
        irled.value = False
        time.sleep(BIT_SPACE_LENGTH)
    time.sleep(CHARACTER_SPACE_LENGTH)


#Init LED
irled = digitalio.DigitalInOut(board.D5)
irled.direction = digitalio.Direction.OUTPUT

 #  count variable
count = 0

# Convert to all caps
MESSAGE = MESSAGE.upper()

while True:
    send_message(MESSAGE)
    
    #  increase count
    count += 1

	#  print to REPL
    print("Sent ""%s"" over IR %d times!" % (MESSAGE, count))

	#  delay before repeating
    time.sleep(DELAY)
