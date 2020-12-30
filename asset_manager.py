from enum import Enum

import pygame
from pygame import Surface


class AssetType(Enum):
    IMAGE = 0


class Asset(Enum):
    MAIN_MENU_BACKGROUND = (AssetType.IMAGE, 'assets/image/mainmenubg.png')
    PLAYER = (AssetType.IMAGE, 'assets/image/player.png')


class AssetManager:
    def __init__(self):
        self._cache = {}

    def get_image(self, asset: Asset) -> Surface:
        assert(asset.value[0] == AssetType.IMAGE)

        if asset not in self._cache.keys():
            self._cache[asset] = pygame.image.load(asset.value[1])

        return self._cache.get(asset)
