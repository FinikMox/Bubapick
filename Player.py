from pygame import *
from Платформер import pyganim, Blocks, Mobs
from Платформер.Blocks import *

MOVE_SPEED = 7
MOVE_LOW_SPEED = 2.5  # замедление
WIDTH = 32
HEIGHT = 32
COLOR = "#888888"

JUMP_POWER = 8
JUMP_LOW_POWER = 2  # дополнительная -сила прыжка
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз
ANIMATION_DELAY = 0.1  # скорость смены кадров
ANIMATION_LOW_SPEED_DELAY = 0.15  # скорость смены кадров при замедлении

ANIMATION_RIGHT = ['hero/hero_right_1.png',
                   'hero/hero_right_2.png']
ANIMATION_LEFT = ['hero/hero_left_1.png',
                  'hero/hero_left_2.png']

ANIMATION_JUMP_LEFT = [('hero/hero_jump_2.png', 0.1)]
ANIMATION_JUMP_RIGHT = [('hero/hero_jump_1.png', 0.1)]
ANIMATION_JUMP = [('hero/hero_jump.png', 0.1)]
ANIMATION_STAY = [('hero/hero.png', 0.1)]


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным

        #  Анимация движения вправо
        boltAnim = []
        boltAnimLowSpeed = []

        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
            boltAnimLowSpeed.append((anim, ANIMATION_LOW_SPEED_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        self.boltAnimRightSuperSpeed = pyganim.PygAnimation(boltAnimLowSpeed)
        self.boltAnimRightSuperSpeed.play()

        #  Анимация движения влево
        boltAnim = []
        boltAnimLowSpeed = []

        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
            boltAnimLowSpeed.append((anim, ANIMATION_LOW_SPEED_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()
        self.boltAnimLeftSuperSpeed = pyganim.PygAnimation(boltAnimLowSpeed)
        self.boltAnimLeftSuperSpeed.play()

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()

        self.winner = False
        self.KEY = False

    def update(self, left, right, up, running, platforms):
        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER
                if running and up:  # если есть замедление и мы прыгаем
                    self.yvel -= JUMP_LOW_POWER  # то прыгаем выше
                self.image.fill(Color(COLOR))
                self.boltAnimJump.blit(self.image, (0, 0))

        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n
            self.image.fill(Color(COLOR))
            if running:  # если замедление
                self.xvel += MOVE_LOW_SPEED  # то передвигаемся медленнее
                if not up:  # и если не прыгаем
                    self.boltAnimLeftSuperSpeed.blit(self.image, (0, 0))  # то отображаем медленную анимацию
            else:  # если не бежим
                if not up:  # и не прыгаем
                    self.boltAnimLeft.blit(self.image, (0, 0))  # отображаем анимацию движения
            if up:  # если же прыгаем
                self.boltAnimJumpLeft.blit(self.image, (0, 0))  # отображаем анимацию прыжка

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image.fill(Color(COLOR))
            if running:
                self.xvel -= MOVE_LOW_SPEED
                if not up:
                    self.boltAnimRightSuperSpeed.blit(self.image, (0, 0))
            else:
                if not up:
                    self.boltAnimRight.blit(self.image, (0, 0))
            if up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0
            if not up:
                self.image.fill(Color(COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if isinstance(p, Blocks.Thorns) or isinstance(p,
                                                              Mobs.Angry_cloud):  # если пересакаемый блок -
                    # Шипы или Злое Облако
                    self.die()  # умираем
                elif isinstance(p, Blocks.Flag):  # если коснулись флага
                    self.winner = True  # победа
                elif isinstance(p, Blocks.InActive_platform):  # невидимая платформа
                    pass
                elif isinstance(p, gold_key):  # подбираем ключ
                    self.KEY = True
                elif isinstance(p, Blocks.Locked_door) and self.KEY:  # взаимодействие с дверьми после подбора ключа
                    pass
                else:
                    if xvel > 0:  # если движется вправо
                        self.rect.right = p.rect.left  # то не движется вправо

                    if xvel < 0:  # если движется влево
                        self.rect.left = p.rect.right  # то не движется влево

                    if yvel > 0:  # если падает вниз
                        self.rect.bottom = p.rect.top  # то не падает вниз
                        self.onGround = True  # и становится на что-то твердое
                        self.yvel = 0  # и энергия падения пропадает

                    if yvel < 0:  # если движется вверх
                        self.rect.top = p.rect.bottom  # то не движется вверх
                        self.yvel = 0  # и энергия прыжка пропадает

    def die(self):
        time.wait(500)
        self.KEY = False
        self.rect.x = self.startX
        self.rect.y = self.startY  # перемещаемся в начальные координаты
# CHANGE
