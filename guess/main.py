from Jumper import Jumper


class Game:
    """ Delegate the game  
    
    """
    def start(self):
        """Start Jumping"""
        jumper = Jumper()
        jumper.play()


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
