#main gameplay
from guess import *
from randomWord import *

class gameplay:
  def __init__(self):
    self.isPlaying = True
    self._lives = 4
    self._win = False
  
  def word(self):
    self.word = Word
    return self.word

  def letter(self):
    self._guess = Guess
    return self._guess
  
  def playing(self):
    if self._lives != 0 and self._win != True:
      self.isPlaying
    else:
      self.isPlaying = False

  def msg(self):
    if self._lives != 0 and self._win != True:
      self._msg = 'You Win!'
    else:
      self._msg = 'You Died! X_X'

  def game(self):
    #plays the game
    while self.isPlaying:
      #gets a word
      self.word()

      #gets a letter
      self.letter(self)

      #updates
      print('NEWWORD')
    
    else:
      self._msg(self)
      quit()