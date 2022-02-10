
class Parachute:
    def __init__(self):
        self.__last_state = 4
        self.__figure_state = self._chute = [
                  '  ___',
                  '/ ___ \ ',
                  '\     /',
                  ' \   /',
                  '   O  ',
                  '  /|\ ',
                  '  / \ '
                  ]

    def print(self, errors):
        if (errors >= self.__last_state):
            print(self.__figure_state[self.__last_state])
        else:
            print(self.__figure_state[errors])
        print("^^^^^^")

    def last_state(self):
        return self.__last_state
