from enum import Enum

import pygame
from pygame.event import Event

from gui import Label


class ButtonState(Enum):
    NORMAL = 0
    PRESSED = 1


class Button(Label):
    def __init__(self, game):
        super().__init__(game)
        self._state = ButtonState.NORMAL

    def handle_event(self, event: Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x, click_y = event.pos
            pos_x, pos_y = self.position
            width, height = self.size

            if pos_x <= click_x <= pos_x + width and pos_y <= click_y <= pos_y + height:
                self._state = ButtonState.PRESSED
        elif event.type == pygame.MOUSEBUTTONUP:
            self._state = ButtonState.NORMAL

    @property
    def state(self):
        return self._state
