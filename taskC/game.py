
from sense_hat import SenseHat
from time import sleep

# Import csv module to write winner highscore
import csv 

# Import datetime module to get time for winner record
import datetime

# Import Die Class from electronic Die.py
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

    # Init Winner
    self.winner = 0
  
  # Function to manage the flow of the game
  def startGame(self):
    # Display Instructions
    sense.show_message('Game Start. Shake Pi to Roll Dice. First to roll over 30 wins.', 0.05)
   

    turn = 1

    while self.won != True:
     
      
           
      sense.show_message('Player '+ str(turn) +' roll dice', 0.02)

      self.detectShake(turn)

      # Init Winning Score
      score = 10

      # Check if Game has been won
      if self.p1 > score:
        self.won = True
        self.winner = 1
        self.endGame()

      if self.p2 > score:
        self.won = True
        self.winner = 2
        self.endGame()

      # Change player turns after every dice roll
      if turn == 1:
        turn = 2
      else:
        turn = 1
  
  # Function to detect shake from player. Once shaken, exit function.
  def detectShake(self, playerID):
    
    shaken = False;
  
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
          print('p1',self.p1)
        elif playerID == 2:
          self.p2 = self.p2 + self.dice.rollDie()
          print('p2',self.p2)

        # Shaken set to true till next Shake
        shaken = True
           
        # Freeze Die for 2 seconds before next turn
        sleep(2)

  # Function to handle game end
  def endGame(self):
    
    if self.winner == 1:
      tempWinner = self.p1
    else:
      tempWinner = self.p2

    sense.show_message('Game END. Player '+str(self.winner)+' WON! P'+str(self.winner)+' Score: '+str(tempWinner)+' THE END.',0.05);
    
    # End the program here by writing to file
    self.writeToFile(tempWinner)


  # Function to save score to winner.csv
  def writeToFile(self, score):
    with open(r'winner.csv', mode='a') as csv_file:
      fieldnames = ['player_id', 'datetime', 'score']
      writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
      

      # Write header only for the first time
      ###writer.writeheader()
    
      writer.writerow({'player_id' : 'p'+str(self.winner), 'datetime': str( datetime.datetime.now( )), 'score':  str(score)})  
     




# Instantiate Game Dice Object
GameDice = Die()

# Pass Die Object into Game Object instance
Game = DiceGame(GameDice)

# Start Game
Game.startGame()
