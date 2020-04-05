from sense_hat import SenseHat
from time import sleep

import random

# init Sense Hat
sense = SenseHat()

# init colours for dice
e = (0, 0, 0) # empty pixels
x = (255, 0, 0,) # red

# init pixel displays for dice (CONST)
ONE = [
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, e, e, e,
   e, e, e, x, x, e, e, e,
   e, e, e, x, x, e, e, e,
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, e, e, e
]
TWO = [
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, x, x, e,
   e, e, e, e, e, x, x, e,
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, e, e, e,
   e, x, x, e, e, e, e, e,
   e, x, x, e, e, e, e, e,
   e, e, e, e, e, e, e, e
]
THREE = [
   e, e, e, e, e, e, x, x,
   e, e, e, e, e, e, x, x,
   e, e, e, e, e, e, e, e,
   e, e, e, x, x, e, e, e,
   e, e, e, x, x, e, e, e,
   e, e, e, e, e, e, e, e,
   x, x, e, e, e, e, e, e,
   x, x, e, e, e, e, e, e
]
FOUR = [
   e, e, e, e, e, e, e, e,
   e, x, x, e, e, x, x, e,
   e, x, x, e, e, x, x, e,
   e, e, e, e, e, e, e, e,
   e, e, e, e, e, e, e, e,
   e, x, x, e, e, x, x, e,
   e, x, x, e, e, x, x, e,
   e, e, e, e, e, e, e, e
]
FIVE = [
   x, x, e, e, e, e, x, x,
   x, x, e, e, e, e, x, x,
   e, e, e, e, e, e, e, e,
   e, e, e, x, x, e, e, e,
   e, e, e, x, x, e, e, e,
   e, e, e, e, e, e, e, e,
   x, x, e, e, e, e, x, x,
   x, x, e, e, e, e, x, x
]
SIX = [
   e, x, x, e, e, x, x, e,
   e, x, x, e, e, x, x, e,
   e, e, e, e, e, e, e, e,
   e, x, x, e, e, x, x, e,
   e, x, x, e, e, x, x, e,
   e, e, e, e, e, e, e, e,
   e, x, x, e, e, x, x, e,
   e, x, x, e, e, x, x, e
]


# Die Class to be imported into game.py
class Die:

         

  def rollDie(self):
    # Generate a random number for Dice Roll
    gen = random.randint(1,6)

    display = ONE

    # Set sense hat display based on generated number
    if gen == 1:
      display = ONE
    elif gen == 2:
      display = TWO
    elif gen == 3:
      display = THREE
    elif gen == 4:
      display = FOUR
    elif gen == 5:
      display = FIVE
    elif gen == 6:
      display = SIX 


    # Display results on sense hat
    sense.set_pixels(display)

    # Return Roll Integer for Score Counting
    return gen

