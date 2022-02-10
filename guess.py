#Code for guessing a number
from randomWord import Word

class Guess:
  #guesses a letter

  def __init__(self):
    self._letter = ''
    self._word = Word()

  def guessing(self):
    self._letter = input('Choose a letter (a-z): ').upper()
    return self._letter
  
  def correct(self):
    if self._letter == '':
      print(f'You guessed: {self._letter}')
    else:
      print('X_X')
    
  def main(self):
    self.guessing()
    self.correct()
    print('💩')
    print(self._word)

Guess().correct()
