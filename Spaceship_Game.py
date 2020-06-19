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
    rocks_position.append(generate_rock())

    score = 0

    distance_from_rock = rock_distance_from_spaceship(rocks_position, spaceship_position)

    return spaceship_position, rocks_position, distance_from_rock, score


def rock_distance_from_spaceship(rocks_position, spaceship_position):

    distance_from_rock = 5

    for rock in rocks_position:
        if rock[1] == spaceship_position[1]:
            distance_from_rock = rock[0] - spaceship_position[0]
    
    return distance_from_rock



def generate_random_direction(distance_from_rock): 
    if distance_from_rock > 0:
        direction = random.choice([1,-1])
    else:
        direction = 0

    return direction


def update_positions(spaceship_position, rocks_position, button_direction, score):
    for rock in rocks_position:
        if rock == spaceship_position:
            score -= 1000
    
    if button_direction == 1:
        spaceship_position[1] += 10
    elif button_direction == -1:
        spaceship_position[1] -= 10

    rocks_position = [[x[0] - 10] + [x[1]] for x in rocks_position] 

    if bool(np.random.binomial(1, 0.4, 1)):
        rocks_position.append(generate_rock())

#    distance_from_rock = rock_distance_from_spaceship(rocks_position, spaceship_position)
    score += 1

    return spaceship_position, rocks_position, score

def collision_with_rock(rocks_position, score):
    
   score = 1   #implement later on , as is = 1 means loose
   return rocks_position, score


def blocked_directions(spaceship_position):

    is_up_blocked = False
    is_down_blocked = False 

    if spaceship_position[1] + 10 >= display_height:
        is_up_blocked = True
    
    if spaceship_position[1] - 10 <= 0:
        is_down_blocked = True

    return is_up_blocked, is_down_blocked


def play_game(spaceship_position, rocks_position, button_direction, score, display, clock):
    display.fill((255, 255, 255))

    display_rocks(rocks_position, display)
    display_spaceship(spaceship_position, display)

    is_up_blocked, is_down_blocked = blocked_directions(spaceship_position)
    if button_direction == 1 and is_up_blocked == True:
        score -= 1000
    elif button_direction == -1 and is_down_blocked == True:
        score -= 1000

    spaceship_position, rocks_position, score = update_positions(spaceship_position, rocks_position, button_direction, score)
    pygame.display.set_caption("SCORE: " + str(score))
    pygame.display.update()

    clock.tick(10)

    return spaceship_position, rocks_position, score

'''
DOWN ->button_direction = -1
UP -> button_direction = 1
'''
display_width = 400
display_height = 250
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)

if __name__ == "__main__":

    pygame.init()
    display = pygame.display.set_mode((display_width,display_height))
    clock = pygame.time.Clock()

    test_games = 1

    steps_per_game = 200

    for _ in range(test_games):
        spaceship_position, rocks_position, distance_from_rock, score = starting_positions()

        while _ in range(steps_per_game):

            distance_from_rock = rock_distance_from_spaceship(rocks_position, spaceship_position)
            button_direction = generate_random_direction(distance_from_rock)

            spaceship_position, rocks_position, score = play_game(
                    spaceship_position
                , rocks_position
                , button_direction
                , score
                , display
                , clock
            )

            if score < -2000:
                break
        
        pygame.quit() 
        sys.exit()




