import pygame
import pymunk
import pymunk.pygame_util
import math

# common
TITLE = "Pool Game"
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 678
BOTTOM_PANEL = 50
BACKGROUND_COLOR = (50, 50, 50)
TEXT_COLOR = (255, 255, 255)
# ball data
MAX_BALL = 17
BALL_MASS = 5
BALL_ELASTICITY = 0.8
BALL_DIAMETER = 36

# wall data
FRICTION = 1000
CUSHION_ELASTICITY = 0.6
POCKET_DIAMETER = 70

# shooting data
MAX_FORCE = 10000
FORCE_STEP = 100