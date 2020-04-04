
from sense_hat import SenseHat
from time import sleep

from electronicDie import Die

# init Sense Hat
sense = SenseHat()


class DiceGame:

  # Constructor to initialize Game Dice
  def __init__(self, dice):
    self.dice = dice

    # Init player scores
    self.p1 = 0
    self.p2 = 0

    # Init Game State (Loop till Game Won)
    self.won = False
  
  # Function to manage the flow of the game
  def startGame(self):
    # Display Instructions
    sense.show_message('Game Start', 0.05)
   
    while self.won != True:
     
      turn = 1
           
      sense.show_message('Player '+ str(turn) +' please roll dice', 0.01)

      self.detectShake(turn)

      # Check if Game has been won
      if self.p1 > 30:
        self.won = True

      if self.p2 > 30:
        self.won = True

      # Change player turns after every dice roll
      if turn == 1:
        turn = 2
      else:
        turn = 1
  

  def detectShake(self, playerID):
    
    shaken = False;
    print("Ran Here!")
  
    while shaken != True:
      acceleration = sense.get_accelerometer_raw()
      x = acceleration['x']
      y = acceleration['y']
      z = acceleration['z']

      x = abs(x)
      y = abs(y)
      z = abs(z)
      
      # Half a second shake window
      sleep(0.5)

      # If Shaken, Roll Dice and save score
      if x > 1 or y > 1 or z > 1:
        if playerID == 1:
	  self.p1 = self.p1 + self.dice.rollDie()
        else:
          self.p2 = self.p2 + self.dice.rollDie()

        # Shaken set to true till next Shake
        shaken = True
           
        # Freeze Die for 2 seconds before next turn
        sleep(2)

# Instantiate Game Dice Object
GameDice = Die()

# Pass Die Object into Game Object instance
Game = DiceGame(GameDice)

# Start Game
Game.startGame()
