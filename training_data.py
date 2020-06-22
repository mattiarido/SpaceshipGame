from spaceship_game import *

def generate_training_data(display, clock):
    training_data_x = []
    training_data_y = []
    training_games = 10000
    steps_per_game = 2000

    for _ in tqdm(range(training_games)):
        spaceship_position, rocks_position, distance_from_rock, score = starting_positions()
        prev_rock_distance = rock_distance_from_spaceship(rocks_position, spaceship_position)

        for _ in range(steps_per_game):
            button_direction = generate_random_direction(distance_from_rock)
            is_up_blocked, is_down_blocked = blocked_directions(spaceship_position)

            training_data_x.append(
                [is_up_blocked, is_down_blocked])

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
            training_data_y.append([0, 0, 0])
        else:
            training_data_y.append([1, 0, 0])

    elif button_direction == -1:
        if is_down_blocked == True:
            training_data_y.append([0, 0, 0])
        else:
            training_data_y.append([0, 0, 1])
    
    else:
        training_data_y.append([0, 0, 0])

    return button_direction, training_data_y


if __name__ == '__main__':
    import csv

    display_width = 400
    display_height = 250
    green = (0,255,0)
    red = (255,0,0)
    black = (0,0,0)
    white = (255,255,255)

    pygame.init()
    display=pygame.display.set_mode((display_width,display_height))
    clock=pygame.time.Clock()

    training_data_x, training_data_y = generate_training_data(display,clock)

    train_data = np.zeros((len(training_data_x), 5), dtype = int)
    train_data[:,0:2] = np.array(training_data_x)
    train_data[:,2:] = np.array(training_data_y)

    with open('train_data.csv', 'w', newline = '') as myfile:
        #colnames = ['is_up_blocked', 'is_down_blocked', 'move_up', 'stay', 'move_down']
        wr = csv.writer(myfile, quoting = csv.QUOTE_NONE, delimiter = ';')
        #wr.writerow(colnames)
        for row in train_data:
            wr.writerow(row)