from __future__ import annotations

from abc import ABC, abstractmethod

import pygame
from pygame.event import Event
from pygame.surface import Surface

from asset_manager import AssetManager

SCREEN_SIZE = (800, 600)


class Game:
    def __init__(self):
        pygame.init()

        self._screen = pygame.display.set_mode(SCREEN_SIZE)
        self._running = True
        self._scene = None
        self._asset_manager = AssetManager()

    @property
    def asset_manager(self):
        return self._asset_manager

    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, scene: GameObject):
        self._scene = scene

    def run(self):
        assert(self._scene is not None)

        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                else:
                    self._scene.handle_event(event)

            self._scene.update(16)  # TODO

            self._screen.fill((0, 0, 0))
            self._scene.redraw(self._screen)
            pygame.display.flip()

    def stop(self):
        self._running = False


class GameObject(ABC):
    def __init__(self, game):
        self._children = []
        self._game = game

    @abstractmethod
    def handle_event(self, event: Event) -> None:
        for child in self._children:
            child.handle_event(event)

    @abstractmethod
    def redraw(self, screen: Surface) -> None:
        for child in self._children:
            child.redraw(screen)

    @abstractmethod
    def update(self, ticks: int) -> None:
        for child in self._children:
            child.update(ticks)

    @property
    def game(self):
        return self._game

    def add_child(self, child: GameObject) -> None:
        self._children.append(child)

    def remove_child(self, child: GameObject) -> None:
        self._children.remove(child)

    def __getitem__(self, index: int) -> GameObject:
        return self._children[index]
