from asset_manager import Asset
from gfx import Sprite
from scene._scene import Scene
from scene._game_scene import GameScene
from gui import Label, Button, ButtonState


class MenuScene(Scene):
    def __init__(self, game):
        super().__init__(game)

        self._background = Sprite(game)
        self._background.image = game.asset_manager.get_image(Asset.MAIN_MENU_BACKGROUND)

        self._label = Label(game)
        self._label.text = 'Menu'
        self._label.color = (255, 255, 255)
        self._label.position = (100, 100)

        self._new_game_button = Button(game)
        self._new_game_button.text = 'new game'
        self._new_game_button.color = (255, 255, 255)
        self._new_game_button.position = (100, 150)

        self._exit_button = Button(game)
        self._exit_button.text = 'exit'
        self._exit_button.color = (255, 255, 255)
        self._exit_button.position = (100, 200)

        self.add_child(self._background)
        self.add_child(self._label)
        self.add_child(self._new_game_button)
        self.add_child(self._exit_button)

    def update(self, ticks: int) -> None:
        super(MenuScene, self).update(ticks)

        if self._new_game_button.state == ButtonState.PRESSED:
            self.game.scene = GameScene(self.game)

        if self._exit_button.state == ButtonState.PRESSED:
            self.game.stop()
