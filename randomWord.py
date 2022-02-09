#code for the random word
from random import choice

class Word:
  #defines a class for picking a random word
  #variable words creates a list of words
  #variable word creates get a word

  def __init__(self):
    #creating vars
    self._words = ['PYTHON', 'CLASS', 'FUNCTION']
    self._word = ''

  def randomWord(self):
    #chooses a random word from a list of words
    self._word = (choice(self._words))
    return self._word

#This is a temporary call 
Word().randomWord()