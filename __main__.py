import arcade
from constants import *
from game.game_logic.game import Game
def main():
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()



if __name__=='__main__':
    main()