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


# Class Monitor to encapsulated or Monitoring and Displaying Functions
class Monitor:

  # Function to get sense temperature  
  def senseTemperature(self):
    # Clear sensor
    sense.clear()

    # Return read temperature
    return sense.get_temperature()

  # Functino to display temperature
  def display(self):

    # Check temperature every 10 seconds and change pixels accordingly 
    while True:

      # Set colour of temperature display to the designated colours
      if self.senseTemperature() < config['cold_max']:
        x = b	
      elif self.senseTemperature() >= config['cold_max'] and self.senseTemperature() < config['comfortable_max']:
        x = g
      elif self.senseTemperature() >= config['hot_min']:
        x = r

      # Show temperature with the assigned colour
      sense.show_message(str(round(self.senseTemperature(),2)),0.2,x)

      # Refresh every 10 seconds
      sleep(10)



monitorInstance = Monitor()

# Display Temperature
monitorInstance.display()
