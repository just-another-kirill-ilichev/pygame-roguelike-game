from pygame import Surface
from pygame.event import Event

from game import GameObject


class Scene(GameObject):
    def handle_event(self, event: Event) -> None:
        super(Scene, self).handle_event(event)

    def redraw(self, screen: Surface) -> None:
        super(Scene, self).redraw(screen)

    def update(self, ticks: int) -> None:
        super(Scene, self).update(ticks)
