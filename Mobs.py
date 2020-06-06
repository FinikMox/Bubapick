from pygame import *
import pyganim
import Платформер.Player

MOB_WIDTH = 32
MOB_HEIGHT = 32
MOB_COLOR = "#2110FF"

ANIMATION_MOBHORYSONTAL = [('mobs/Angry_cloud_1.png'),
                           ('mobs/Angry_cloud_2.png'),
                           ('mobs/Angry_cloud_3.png')]

ANIMATION_MOBDEATH = [('mobs/Angry_cloudDeath_1.png'),
                      ('mobs/Angry_cloudDeath_2.png'),
                      ('mobs/Angry_cloudDeath_3.png'),
                      ('mobs/Angry_cloudDeath_4.png'),
                      ('mobs/Angry_cloudDeath_5.png')]


class Angry_cloud(sprite.Sprite):
    def __init__(self, x, y, left, up, maxLengthLeft, maxLengthUp):
        sprite.Sprite.__init__(self)
        self.image = Surface((MOB_WIDTH, MOB_HEIGHT))
        self.image.fill(Color(MOB_COLOR))
        self.rect = Rect(x, y, MOB_WIDTH, MOB_HEIGHT)
        self.image.set_colorkey(Color(MOB_COLOR))
        self.startX = x  # начальные координаты
        self.startY = y
        self.maxLengthLeft = maxLengthLeft  # максимальное расстояние, которое может пройти в одну сторону
        self.maxLengthUp = maxLengthUp  # максимальное расстояние, которое может пройти в одну сторону, вертикаль
        self.xvel = left  # cкорость передвижения по горизонтали, 0 - стоит на месте
        self.yvel = up  # скорость движения по вертикали, 0 - не двигается

        boltAnim = []
        for anim in ANIMATION_MOBHORYSONTAL:
            boltAnim.append((anim, 0.3))
        self.boltAnim = pyganim.PygAnimation(boltAnim)
        self.boltAnim.play()

    def update(self, platforms):  # по принципу героя

        self.image.fill(Color(MOB_COLOR))
        self.boltAnim.blit(self.image, (0, 0))

        self.rect.y += self.yvel
        self.rect.x += self.xvel

        self.collide(platforms)

        if (abs(self.startX - self.rect.x) > self.maxLengthLeft):
            self.xvel = -self.xvel  # если прошли максимальное растояние, то идеи в обратную сторону
        if (abs(self.startY - self.rect.y) > self.maxLengthUp):
            self.yvel = -self.yvel  # если прошли максимальное растояние, то идеи в обратную сторону, вертикаль

    def collide(self, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p) and self != p:  # если с чем-то или кем-то столкнулись
                self.xvel = - self.xvel  # то поворачиваем в обратную сторону
                self.yvel = - self.yvel
