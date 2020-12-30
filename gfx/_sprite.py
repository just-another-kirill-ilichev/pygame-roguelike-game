from __future__ import annotations

import pygame
from pygame import Surface
from pygame.event import Event

from game import GameObject


class Sprite(GameObject):
    def __init__(self, game):
        super().__init__(game)
        self._sprite = pygame.sprite.Sprite()

    @property
    def image(self):
        return self._sprite.image

    @image.setter
    def image(self, image: Surface):
        self._sprite.image = image
        self._sprite.rect = image.get_rect()

    @property
    def position(self) -> tuple:
        return self._sprite.rect.x, self._sprite.rect.y

    @position.setter
    def position(self, pos: tuple) -> None:
        self._sprite.rect.move(pos[0], pos[1])

    @property
    def size(self) -> tuple:
        return self._sprite.rect.size

    @size.setter
    def size(self, size: tuple) -> None:
        self._sprite.rect.size = size

    def move(self, step: pygame.Vector2):
        self._sprite.rect.move(step.x, step.y)

    def check_collision(self, other: Sprite) -> bool:
        return pygame.sprite.collide_rect(self._sprite, other._sprite)

    def handle_event(self, event: Event) -> None:
        super(Sprite, self).handle_event(event)

    def redraw(self, screen: Surface) -> None:
        assert(self.image is not None)

        screen.blit(self._sprite.image, self._sprite.rect)

    def update(self, ticks: int) -> None:
        super(Sprite, self).update(ticks)
