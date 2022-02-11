class Parachute:
    def __init__(self):
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
        for i in range(errors, len(self.__figure_state)):
            if errors >= self.__last_state and self.__figure_state[i] == "   O":
                self.__figure_state[i] = "   X"

            print(self.__figure_state[i])

        print("^^^^^^")

    def last_state(self):
        return self.__last_state
