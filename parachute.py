#parachute code

class Parachute:
  #builds the parachute
  #variable chute creates the person and chute
  
  def __init__(self):
    #creating the person and chute
    self._chute = [
                  '  ___',
                  '/ ___ \ ',
                  '\     /',
                  ' \   /',
                  '   O  ',
                  '  /|\ ',
                  '  / \ '
                  ]

  def person(self):
    for i in self._chute:
      print(i)
  
  def removeChute(self):
    #This function is currently empty

    return self.removed