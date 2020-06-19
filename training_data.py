from Spaceship_Game import *

def generate_training_data(display, clock):
    training_data_x = []
    training_data_y = []
    training_games = 2
    steps_per_game = 100

    for _ in tqdm(range(training_games)):
        spaceship_position, rocks_position, distance_from_rock, score = starting_positions()
        prev_rock_distance = rock_distance_from_spaceship(rocks_position, spaceship_position)

        for _ in range(steps_per_game):
            button_direction = generate_random_direction(distance_from_rock)
            is_up_blocked, is_down_blocked = blocked_directions(spaceship_position)

            training_data_x.append(
                [is_up_blocked, is_down_blocked, button_direction])

            button_direction, training_data_y = generate_training_data_y(
                spaceship_position
                ,button_direction
                ,training_data_y
                ,is_up_blocked
                ,is_down_blocked
            )

            spaceship_position, rocks_position, score = play_game(
                    spaceship_position, 
                    rocks_position, 
                    button_direction, 
                    score, 
                    display, 
                    clock
                )

            if score < -2000:
                break


    return training_data_x, training_data_y


def generate_training_data_y(spaceship_position, button_direction, training_data_y, is_up_blocked, is_down_blocked):
    if button_direction == 1:
        if is_up_blocked == True:
            training_data_y.append([0])
        else:
            training_data_y.append([1])

    elif button_direction == -1:
        if is_down_blocked == True:
            training_data_y.append([0])
        else:
            training_data_y.append([-1])
    
    else:
        training_data_y.append([0])

    return button_direction, training_data_y