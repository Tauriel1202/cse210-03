import random


class Word:

    """A class that generate ramdon words from a list. 
    

    Attributes:
        __word_list (string[]): A list of words
    """

    def __init__(self):
        self.__word_list = [
            "story",
            "format",
            "dragon",
            "spread",
            "carbon",
            "digital",
            "haunt",
            "challenge",
            "sausage",
            "systematic",
            "sink",
            "genie",
            "diet",
            "strange",
            "minimize",
            "island",
            "compact",
            "conscience",
            "angle",
            "flex",
            "forest",
            "settlement",
            "camp",
            "giant",
            "cultivate",
            "angel",
            "equinox",
            "board",
            "lid",
            "view",
            "soprano",
            "elves",
            "environment",
            "surfboard",
            "twist",
            "legislature",
            "text",
            "agency",
            "defend",
            "tooth",
            "force",
            "ethnic",
            "wheel",
            "repeat",
            "essential",
            "swipe",
            "leader",
            "steep",
            "cultural",
            "counter",
        ]

    def _word_list(self, list):
        """Constructs a new Word."""
        self.__word_list = list

    def get_random_word(self):
        """Gets a new random word.
        
        Returns:
            String: Word.
        """
        return random.choice(self.__word_list)

    def show_blanks(word, correct):
        """Print the letters and blanks.
        """
        to_print = ""
        for char in word:
            if char in correct:
                to_print += char
            else:
                to_print += " - "
        print(to_print)
