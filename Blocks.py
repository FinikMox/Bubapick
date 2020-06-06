from pygame import *
import pyganim

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#00000000"

ANIMATION_FLAG = [
    ('blocks/Flag_1.png'),
    ('blocks/Flag_2.png')]

ANIMATION_THORN = [
    ('blocks/thorn_1.png'),
    ('blocks/thorn_2.png'),
    ('blocks/thorn_3.png')]


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("blocks/platform.png")
        self.image.set_colorkey(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class InActive_platform(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("blocks/platform.png")


class Thorns(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        boltAnim = []
        for anim in ANIMATION_THORN:
            boltAnim.append((anim, 0.4))
        self.boltAnim = pyganim.PygAnimation(boltAnim)
        self.boltAnim.play()

    def update(self):
        self.image.fill(Color(PLATFORM_COLOR))
        self.boltAnim.blit(self.image, (0, 0))


class Flag(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        boltAnim = []
        for anim in ANIMATION_FLAG:
            boltAnim.append((anim, 0.3))
        self.boltAnim = pyganim.PygAnimation(boltAnim)
        self.boltAnim.play()

    def update(self):
        self.image.fill(Color(PLATFORM_COLOR))
        self.boltAnim.blit(self.image, (0, 0))


class Locked_door(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("blocks/locked_door.png")
        self.image.set_colorkey(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class gold_key(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("blocks/key.png")
        self.image.set_colorkey(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


'''DEFLECTOR_WIDTH = 64
DEFLECTOR_HEIGHT = 64
DEFLECTOR_COLOR = "#00000001"'''

'''ANIMATION_BROKEN_DEFLECTOR = [('blocks/broken_deflector_1.png'),
                              ('blocks/broken_deflector_2.png'),
                              ('blocks/broken_deflector_3.png')]'''

'''class Weather_deflector(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((DEFLECTOR_WIDTH, DEFLECTOR_HEIGHT))
        self.image.fill(Color(DEFLECTOR_COLOR))
        self.image = image.load("blocks/deflector.png")
        self.image.set_colorkey(Color(DEFLECTOR_COLOR))
        self.rect = Rect(x - 32, y - 32, DEFLECTOR_WIDTH, DEFLECTOR_HEIGHT)


class Weather_broken_deflector(Weather_deflector):
    def __init__(self, x, y):
        Weather_deflector.__init__(self, x, y)
        boltAnim = []
        for anim in ANIMATION_BROKEN_DEFLECTOR:
            boltAnim.append((anim, 0.5))
        self.boltAnim = pyganim.PygAnimation(boltAnim)
        self.boltAnim.play()

    def update(self):
        self.image.fill(Color(PLATFORM_COLOR))
        self.boltAnim.blit(self.image, (0, 0))

    def activate(self):
        self.image = Surface((DEFLECTOR_WIDTH, DEFLECTOR_HEIGHT))
        self.image.fill(Color(DEFLECTOR_COLOR))
        self.image = image.load("blocks/deflector.png")
        self.image.set_colorkey(Color(DEFLECTOR_COLOR))'''
