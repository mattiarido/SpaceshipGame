import random
import time
import math
from tqdm import tqdm
import numpy as np
import pygame
import sys

def display_spaceship(spaceship_position, display):
    pygame.draw.rect(display, (0, 255, 0), pygame.Rect(spaceship_position[0], spaceship_position[1], 10, 10))


def display_rocks(rocks_position, display):
    for rock in rocks_position:
        pygame.draw.rect(display, (255, 0, 0), pygame.Rect(rock[0], rock[1], 10, 10))


def generate_rock():
    return [display_width, random.randrange(1, display_height / 10) * 10]


def starting_positions():
    spaceship_position = [0, 100]
    
    rocks_position = list()
    for i in range(0,5):
        rock_position = generate_rock()
        rocks_position.append(rock_position)

    score = 0

    return spaceship_position, rocks_position, score


def rock_distance_from_spaceship(rocks_position, spaceship_position):
    for rock in rocks_position:
        if rock[1] == spaceship_position[1]:
            rock_in_target = rock
    
    return spaceship_position[0] - rock[0]


def update_positions(spaceship_position, rocks_position, button_direction, score):
    for rock in rocks_position:
        if rock == spaceship_position:
            score = 1
    
    if button_direction == 1:
        spaceship_position[1] += 10
    elif button_direction == 2:
        spaceship_position[1] -= 10

    rocks_position = [[x[0] - 10] + [x[1]] for x in rocks_position] 

    if bool(np.random.binomial(1, 0.4, 1)):
        rocks_position.append(generate_rock())

    return spaceship_position, rocks_position, score

def collision_with_rock(rocks_position, score):
    
   score = 1   #implement later on , as is = 1 means loose
   return rocks_position, score


def blocked_directions(spaceship_position):

    is_up_blocked = 0
    is_down_blocked = 0 

    if spaceship_position[1] + 10 >= 500:
        is_up_blocked = 1
    
    if spaceship_position[1] - 10 <= 0:
        is_down_blocked = 1

    return spaceship_position, is_up_blocked, is_down_blocked


def play_game(spaceship_position, rocks_position, button_direction, score, display, clock):
    crashed = False
    while crashed is not True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or score == 1:
                crashed = True
                pygame.quit() 
                sys.exit()
        display.fill((255, 255, 255))

        display_rocks(rocks_position, display)
        display_spaceship(spaceship_position, display)

        spaceship_position, rocks_position, score = update_positions(spaceship_position, rocks_position, button_direction, score)
        pygame.display.set_caption("SCORE: " + str(score))
        pygame.display.update()
        clock.tick(10)

        return spaceship_position, rocks_position, score

'''
DOWN ->button_direction = 2
UP -> button_direction = 1
'''

display_width = 400
display_height = 250
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)

pygame.init()
display = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

test_games = 1
 
steps_per_game = 100

for _ in range(test_games):
        spaceship_position, rocks_position, score = starting_positions()

        count_same_direction = 0
        prev_direction = 0

        for _ in range(steps_per_game):
            spaceship_position, is_up_blocked, is_down_blocked = blocked_directions(spaceship_position)

            button_direction = 0

            spaceship_position, rocks_position, score = play_game(spaceship_position, rocks_position, button_direction, score, display, clock)

    

