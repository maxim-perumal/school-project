import pygame
import random
import math
import numpy as np

from pygame.color import THECOLORS

import pymunk
from pymunk.vec2d import Vec2d
from pymunk.pygame_util import draw

# Initialisation of Pygame. Initialisation de Pygame.
width = 1280 # Longueur en pixel.
height = 720 # Hauteur en pixel.
screeDimensions = (width,height)
pygame.init()
screen = pygame.display.set_mode(screeDimensions)

# We don't use this option. Nous n'utilisons pas cette option de pyGame.
screen.set_alpha(None)

# prototype
class Simulation:
    def __init__(self):
        self.car_is_crashed = False

        self.space = pymunk.Space()
        self.space.gravity = pymunk.Vec2d(0., 0.)

        # Create the car.
        self.create_car(100, 100, 0.5)

        zone = [
            pymunk.Segment(
                self.space.static_body,
                (0, 1), (0, height), 1),
            pymunk.Segment(
                self.space.static_body,
                (1, height), (width, height), 1),
            pymunk.Segment(
                self.space.static_body,
                (width-1, height), (width-1, 1), 1),
            pymunk.Segment(
                self.space.static_body,
                (1, 1), (width, 1), 1)
        ]

        for segment in zone:
            segment.friction = 1.
            segment.group = 1
            segment.collision_type = 1
            segment.color = THECOLORS['red']
        self.space.add(zone)

        def create_car(self, x, y, r):
            """
            inertia = pymunk.moment_for_circle(1, 0, 14, (0, 0))
            self.car_body = pymunk.Body(1, inertia)
            self.car_body.position = x, y
            self.car_shape = pymunk.Circle(self.car_body, 25)
            self.car_shape.color = THECOLORS["green"]
            self.car_shape.elasticity = 1.0
            self.car_body.angle = r
            driving_direction = Vec2d(1, 0).rotated(self.car_body.angle)
            self.car_body.apply_impulse(driving_direction)
            self.space.add(self.car_body, self.car_shape)
            """

        def move_car():
            pass

        def crash_car():
            pass

        def getSonarA():
            pass

        def getSonarB():
            pass

        def getSonarC():
            pass
            
        def refresh():
            pass



simulation = Simulation()

"""
play = True

x = 30
y = 30

clock = pygame.time.Clock()

while play:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (150,20,200), pygame.Rect(x, y, 60, 60))

    pygame.display.flip()
    clock.tick(60)
"""
