
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

y = (255, 255, 0) # Yellow
o = (255, 69, 0) # Orange 
r = (255, 0, 0) # Red

b = (0, 0, 0) # Black

emoji1 = [
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, b, b, y, y, b, b, y,
   y, b, b, y, y, b, b, y,
   y, y, y, y, y, y, y, y,
   y, b, b, y, y, b, b, y,
   y, y, y, b, b, y, y, y,
   y, y, y, y, y, y, y, y
]


emoji2 = [
   o, o, o, o, o, o, o, o,
   o, o, o, o, o, o, o, o,
   o, b, b, o, o, b, b, o,
   o, o, o, o, o, o, o, o,
   o, o, o, o, o, o, o, o,
   o, o, o, b, b, o, o, o,
   o, b, b, o, o, b, b, o,
   o, o, o, o, o, o, o, o
]


emoji3 = [
   r, r, r, r, r, r, r, r,
   r, r, r, r, r, r, r, r,
   r, b, b, r, r, b, b, r,
   r, b, b, r, r, b, b, r,
   r, r, r, b, b, r, r, r,
   r, r, b, r, r, b, r, r,
   r, r, r, b, b, r, r, r,
   r, r, r, r, r, r, r, r
]


while True:
  sense.set_pixels(emoji1)
  sleep(3)
  sense.set_pixels(emoji2)
  sleep(3)
  sense.set_pixels(emoji3)
  sleep(3)
