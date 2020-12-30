from __future__ import annotations

from pygame import Surface, Vector2
from pygame.event import Event

from game import GameObject
from gfx import Sprite


class Actor(GameObject):
    def __init__(self, game):
        super().__init__(game)
        self._health = 0
        self._damage = 0
        self._speed = Vector2(0.0, 0.0)

        self._drag = 0.2
        self._acceleration = Vector2(0.0, 0.0)
        self._sprite = Sprite(game)
        
        self.add_child(self._sprite)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, health: int) -> None:
        assert(health >= 0)
        self._health = health

    def take_damage(self, damage: int) -> None:
        if damage > self.health:
            self.health = 0
        else:
            self.health -= damage

    @property
    def image(self) -> Surface:
        return self._sprite.image
    
    @image.setter
    def image(self, image: Surface) -> None:
        self._sprite.image = image

    def apply_impulse(self, impulse: Vector2):
        self._speed += impulse

    def add_acceleration(self, acc):
        self._acceleration += acc

    def check_collision(self, other: Actor) -> bool:
        return self._sprite.check_collision(other._sprite)

    def move(self, step_x, step_y):
        self._sprite.move(Vector2(step_x, step_y))

    def handle_event(self, event: Event) -> None:
        super(Actor, self).handle_event(event)

    def redraw(self, screen: Surface) -> None:
        super(Actor, self).redraw(screen)

    def update(self, ticks: int) -> None:
        super(Actor, self).update(ticks)

        self.move(self._speed.x, self._speed.y)
        self._speed = self._speed - (self._drag * self._speed) + self._acceleration
