#Code for guessing a number
from randomWord import Word

class Guess:
  #guesses a letter

  def __init__(self):
    self._letter = ''

  def guessing(self):
    self.letter = input('Choose a letter (a-z): ')
    return self._letter
  
  def correct(self):
    if self._letter in Word.randomWord(self):
      print('Yay!')

Guess().correct()
