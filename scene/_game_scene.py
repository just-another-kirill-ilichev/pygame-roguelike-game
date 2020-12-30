import pygame
from pygame.event import Event

from actor import Actor
from asset_manager import Asset
from scene import Scene


class GameScene(Scene):
    def __init__(self, game):
        super().__init__(game)

        self._player = Actor(game)
        self._player.health = 100
        # self._player
        self._player.image = self.game.asset_manager.get_image(Asset.PLAYER)

        self.add_child(self._player)

    def handle_event(self, event: Event) -> None:
        super(GameScene, self).handle_event(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('w')
                self._player.apply_impulse(pygame.Vector2(10.0, 0.0))
            elif event.key == pygame.K_s:
                print('s')
                self._player.apply_impulse(pygame.Vector2(-10.0, 0.0))
            elif event.key == pygame.K_a:
                print('a')
                self._player.apply_impulse(pygame.Vector2(0.0, 10.0))
            elif event.key == pygame.K_d:
                print('d')
                self._player.apply_impulse(pygame.Vector2(0.0, -10.0))

    def update(self, ticks: int) -> None:
        super(GameScene, self).update(ticks)
