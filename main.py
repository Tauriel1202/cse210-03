#main gameplay
class gameplay:
  def __init__(self):
    self.isPlaying = True
    self._guess = ''
    self._lives = 10
    self._win = False
  
  def letter(self):
    self._guess = input('Choose a letter [a-z]: ').capitalize()
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
    if self.isPlaying:
      print('WORD')
      self.letter(self)
      print('NEWWORD')
    
    else:
      self._msg(self)
      quit()