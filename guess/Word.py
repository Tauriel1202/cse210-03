import random


class Word:
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
        self.__word_list = list

    def get_random_word(self):
        return random.choice(self.__word_list)

    def show_blanks(word, correct):
        to_print = ""
        for char in word:
            if char in correct:
                to_print += char
            else:
                to_print += " - "
        print(to_print)
