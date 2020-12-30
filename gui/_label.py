import pygame
from pygame import Surface
from pygame.event import Event

from game import GameObject


class Label(GameObject):
    def __init__(self, game):
        super().__init__(game)
        self._text_surface = None
        self._font = pygame.font.SysFont('Comic Sans MS', 30)
        self._color = (0, 0, 0)
        self.text = ''
        self._position = (0, 0)

    def _update_surface(self):
        self._text_surface = self._font.render(self.text, True, self._color)

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, text: str) -> None:
        self._text = text
        self._update_surface()

    @property
    def position(self) -> tuple:
        return self._position

    @position.setter
    def position(self, pos: tuple) -> None:
        self._position = pos

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: tuple):
        self._color = color
        self._update_surface()

    @property
    def size(self):
        return self._text_surface.get_size()

    def redraw(self, screen: Surface) -> None:
        screen.blit(self._text_surface, self.position)

    def update(self, ticks: int) -> None:
        pass

    def handle_event(self, event: Event) -> None:
        pass
