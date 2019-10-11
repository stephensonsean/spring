import sys
import random
import math

from pygame.locals import *

from Pygame.spring import app
from Pygame.spring.project_settings import *


class SpringGame(app.App):

    def __init__(self):
        super(SpringGame, self).__init__()
        self.spring_point = Dot(radius=8,
                         x=100,
                         y=100,
                         color=black,
                         )

        self.weight = Dot(radius=5,
                               x=(WINDOW_SIZE[0] / 2 - 3),
                               y=(WINDOW_SIZE[1] / 2 - 5),
                               color=orange,
                               speed=1,
                               gravity=0)

        self.k = 0.01 + (random.random() * .2)

        # self.weight.friction = random.randint(0, 1) * .5

    def update(self):

        distance = self.spring_point.position - self.weight.position
        if distance.length <= .001:
            self.weight.position = Vector(random.random() * WINDOW_SIZE[0],
                                               random.random() * WINDOW_SIZE[1])

            self.spring_point.position = Vector(random.random() * WINDOW_SIZE[0],
                                         random.random() * WINDOW_SIZE[1])

            self.k = 0.01 + (random.random() * .2)

            distance = self.spring_point.position - self.weight.position

        spring_force = distance * self.k

        self.weight.velocity.add_to(spring_force)

        self.weight.update()

    def draw(self):
        win.fill(off_white)

        self.spring_point.draw()
        self.weight.draw()

        self.line = pygame.draw.line(win,
                                     black,
                                     (self.spring_point.position.x, self.spring_point.position.y),
                                     (self.weight.position.x, self.weight.position.y),
                                     2)

        pygame.display.update()

    def loop(self):
        while self.game_loop:
            self.event()

            self.update()

            self.draw()

            clock.tick(60)

    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.weight.position = Vector(random.random() * WINDOW_SIZE[0],
                                                   random.random() * WINDOW_SIZE[1])

                self.spring_point.position = Vector(random.random() * WINDOW_SIZE[0],
                                             random.random() * WINDOW_SIZE[1])
            elif event.type == pygame.MOUSEBUTTONUP:
                pass
            elif event.type == pygame.MOUSEMOTION:
                pass
        keys = pygame.key.get_pressed()


class Asset(object):
    def __init__(self, width=6, height=10, x=(WINDOW_SIZE[0] / 2 - 3), y=(WINDOW_SIZE[1] / 2 - 5),
                 color=(255, 0, 0), speed=1, direction=random.random() * math.pi * 2, gravity = 0):
        self.width = width
        self.height = height
        # self.x = x
        # self.y = y
        self.position = Vector(x, y)
        self.velocity = Vector(0, 0)
        self.velocity.length = speed
        self.velocity.angle = direction
        self.gravity = Vector(0, gravity or 0)

        self.init_x = x
        self.init_y = y

        self.color = color

        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)

        self.friction = .9
        self.mass = 0
        self.bounce = -1

    def accelerate(self, accel):
        self.velocity += accel

    def update(self):
        print(self.velocity)
        self.velocity.multiply_by(self.friction)
        self.velocity.add_to(self.gravity)
        self.position.add_to(self.velocity)
        print(self.velocity)
        print('-------------')

    def draw(self):
        pygame.draw.rect(win, self.color, (self.position.x, self.position.y, self.width, self.height))
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)

    def reset(self):
        self.x = self.init_x
        self.y = self.init_y


class Dot(Asset):

    def __init__(self, radius=5, x=(WINDOW_SIZE[0] / 2 - 3), y=(WINDOW_SIZE[1] / 2 - 5),
                 color=(255, 0, 0), speed=50, direction=random.random() * math.pi * 2, gravity = 0):
        super(Dot, self).__init__(width=radius,
                                  height=radius,
                                  x=x,
                                  y=y,
                                  color=color,
                                  speed=speed,
                                  direction=direction,
                                  gravity=gravity)

        self.radius = radius


    def draw(self ):
        self.rect = pygame.Rect(self.position.x - (self.radius * 1.25),
                                self.position.y - (self.radius * 1.25),
                                self.width * 3 - 3.3,
                                self.height * 3 - 3.3)
        pygame.draw.circle(win, self.color, (int(self.position.x), int(self.position.y)), self.radius)


class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{}, {}'.format(self.x, self.y)

    def multiply_by(self, value):
        self.x *= value
        self.y *= value

    def divide_by(self, value):
        self.x /= value
        self.y /= value

    def add_to(self, other):
        self.x += other.x
        self.y += other.y

    def subtract_from(self, other):
        self.x -= other.x
        self.y -= other.y

    @property
    def angle(self):
        return math.atan2(self.y, self.x)

    @angle.setter
    def angle(self, angle):
        self.x = math.sin(angle) * self.length
        self.y = math.cos(angle) * self.length

    @property
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    @length.setter
    def length(self, length):
        self.x = math.sin(self.angle) * length
        self.y = math.cos(self.angle) * length

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, value):
        return Vector(self.x * value, self.y * value)


if __name__ == "__main__":
    game = SpringGame()
    game.loop()
