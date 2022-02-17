class Parachute:
    """A class that print the state o parachute, if a word is incorrect removes a line.  
    

    Attributes:
        __last_state (int): Basically means the number of lives
        __figure_state (String[]): Represents the lines of parachute figure
    """

    def __init__(self):
        """Constructs a new Parachute."""
        self.__last_state = 4
        self.__figure_state = [
            "  ___",
            "/ ___ \ ",
            "\     /",
            " \   /",
            "   O",
            "  /|\ ",
            "  / \ ",
        ]

    def print(self, errors):
        """Print the figure on screen
        
        Args:
            String[]: errors
        
        """
        for i in range(errors, len(self.__figure_state)):
            if errors >= self.__last_state and self.__figure_state[i] == "   O":
                self.__figure_state[i] = "   X"

            print(self.__figure_state[i])

        print("^^^^^^")

    def last_state(self):
        """return the last_state value
        
        Returns:
            int: __last_state
        
        """
        return self.__last_state
