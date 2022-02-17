from Parachute import Parachute
from Word import Word


class Jumper:
    """This class contains the logic of the Jumper game  
    

    Attributes:
        __word (String): Basically means the number of lives
        __correct (String[]): The correct letters that user typed. 
        __incorrect (String[]): The incorrect letters that user typed. 
        __figure  (Parachute): The figure
    """

    def __init__(self):
        """Constructs a new Parachute."""
        self.__word = Word().get_random_word()
        self.__correct = []
        self.__incorrect = []
        self.__figure = Parachute()

    def play(self):
        """Start the game"""
        Word.show_blanks(self.__word, self.__correct)
        self.__figure.print(len(self.__incorrect))

        while len(self.__incorrect) < self.__figure.last_state():
            option = input("Guess a letter [a-z]: ")
            if option in self.__word:
                self.__correct.append(option)
            else:
                self.__incorrect.append(option)

            Word.show_blanks(self.__word, self.__correct)
            self.__figure.print(len(self.__incorrect))
            if self.win():
                print("You win! 😀")
                break

    def win(self):
        """Check if the game is over

        Returns:
            Boolean: win.

        """
        win = False
        for l in self.__word:
            if l in self.__correct:
                win = True
            else:
                return False
        return win
