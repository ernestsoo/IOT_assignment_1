from sense_hat import SenseHat
from time import sleep
import json

# Load Config Json file
with open('config.json') as f:
  config = json.load(f)

# Check file loaded successfully
print(config)

# Sense Hat Initialization
sense = SenseHat()
sense.clear()


# Colour Initialization
e = (0, 0, 0)  #black
r = (255, 0, 0) #red
b = (0, 181, 204) #blue
g = (41, 241, 195) #green

# Check temperature every 10 seconds and change pixels accordingly
while True:

  # Clear sensor
  sense.clear()

  # Get temperature from sensor
  temperature =  sense.get_temperature()  
 
  # Set colour of temperature display to the designated colours
  if temperature < 10:
   x = b	
  elif temperature > 9 and temperature < 25:
   x = g
  elif temperature > 24:
   x = r

  # Show temperature with the assigned colour
  sense.show_message(str(round(temperature,2)),0.2,x)

  # Refresh every 10 seconds
  sleep(10)
