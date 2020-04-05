
from sense_hat import SenseHat
from time import sleep

# Init Sense Hat
sense = SenseHat()

y = (255, 255, 0) # Yellow
o = (255, 69, 0) # Orange 
r = (255, 0, 0) # Red

b = (0, 0, 0) # Black

# Init Emojit Constants
EMOJI1 = [
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, b, b, y, y, b, b, y,
   y, b, b, y, y, b, b, y,
   y, y, y, y, y, y, y, y,
   y, b, b, y, y, b, b, y,
   y, y, y, b, b, y, y, y,
   y, y, y, y, y, y, y, y
]

EMOJI2 = [
   o, o, o, o, o, o, o, o,
   o, o, o, o, o, o, o, o,
   o, b, b, o, o, b, b, o,
   o, o, o, o, o, o, o, o,
   o, o, o, o, o, o, o, o,
   o, o, o, b, b, o, o, o,
   o, b, b, o, o, b, b, o,
   o, o, o, o, o, o, o, o
]

EMOJI3 = [
   r, r, r, r, r, r, r, r,
   r, r, r, r, r, r, r, r,
   r, b, b, r, r, b, b, r,
   r, b, b, r, r, b, b, r,
   r, r, r, b, b, r, r, r,
   r, r, b, r, r, b, r, r,
   r, r, r, b, b, r, r, r,
   r, r, r, r, r, r, r, r
]


# Emoji Class that displays an Emoji based on index
class Emoji:

  def __init__(self, display):
    self.display = display

  def displayEmoji(self):
    sense.set_pixels(self.display)

# Instantiate 3 different emoji variables
emoji1 = Emoji(EMOJI1)
emoji2 = Emoji(EMOJI2)
emoji3 = Emoji(EMOJI3)


# Loop and display an emoji every 3 seconds
while True:
  emoji1.displayEmoji()
  sleep(3)
  emoji2.displayEmoji()
  sleep(3)
  emoji3.displayEmoji()
  sleep(3)
