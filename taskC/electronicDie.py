from sense_hat import SenseHat
from time import sleep

import random

# init Sense Hat
sense = SenseHat()

# init colours for dice
e = (0, 0, 0) # empty pixels
x = (255, 0, 0,) # red

# init pixel displays for dice
one = [
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, e, e, e,
   e, e, e, x, x, e, e, e,
   e, e, e, x, x, e, e, e,
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, e, e, e
]
two = [
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, x, x, e,
   e, e, e, e, e, x, x, e,
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, e, e, e,
   e, x, x, e, e, e, e, e,
   e, x, x, e, e, e, e, e,
   e, e, e, e, e, e, e, e
]
three = [
   e, e, e, e, e, e, x, x,
   e, e, e, e, e, e, x, x,
   e, e, e, e, e, e, e, e,
   e, e, e, x, x, e, e, e,
   e, e, e, x, x, e, e, e,
   e, e, e, e, e, e, e, e,
   x, x, e, e, e, e, e, e,
   x, x, e, e, e, e, e, e
]
four = [
   e, e, e, e, e, e, e, e,
   e, x, x, e, e, x, x, e,
   e, x, x, e, e, x, x, e,
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, e, e, e,
   e, x, x, e, e, x, x, e,
   e, x, x, e, e, x, x, e,
   e, e, e, e, e, e, e, e
]
five = [
   x, x, e, e, e, e, x, x,
   x, x, e, e, e, e, x, x,
   e, e, e, e, e, e, e, e,
   e, e, e, x, x, e, e, e,
   e, e, e, x, x, e, e, e,
   e, e, e, e, e, e, e, e,
   x, x, e, e, e, e, x, x,
   x, x, e, e, e, e, x, x
]
six = [
   e, x, x, e, e, x, x, e,
   e, x, x, e, e, x, x, e,
   e, e, e, e, e, e, e, e,
   e, x, x, e, e, x, x, e,
   e, x, x, e, e, x, x, e,
   e, e, e, e, e, e, e, e,
   e, x, x, e, e, x, x, e,
   e, x, x, e, e, x, x, e
]

class Die:

         

  def rollDie(self):
    gen = random.randint(1,7)

    display = one
    rollInt = 0

    if gen == 1:
      display = one
      rollInt = 1
    elif gen == 2:
      display = two
      rollInt = 2
    elif gen == 3:
      display = three
      rollInt = 3
    elif gen == 4:
      display = four
      rollInt = 4
    elif gen == 5:
      display = five
      rollInt = 5
    elif gen == 6:
      display == six 
      rollInt = 6

    sense.set_pixels(display)

    # Return Roll Integer for Score Counting
    return rollInt


GameDice = Die()
GameDice.rollDie()

