from game import Game
from scene import MenuScene

if __name__ == '__main__':
    game = Game()
    game.scene = MenuScene(game)
    game.run()
