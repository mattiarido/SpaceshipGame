from spaceship_game import *
from training_data import generate_training_data

from keras.models import Sequential
from keras.layers import Dense
import csv
import numpy as np



display_width = 400
display_height = 250
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)

pygame.init()
display=pygame.display.set_mode((display_width,display_height))
clock=pygame.time.Clock()

'''
DOWN ->button_direction = -1
UP -> button_direction = 1
'''

with open('train_data.csv', newline = '\n') as csvfile:
    training_data = list(csv.reader(csvfile, delimiter = ';', quoting = csv.QUOTE_NONNUMERIC))

# training_data_x, training_data_y = generate_training_data(display,clock)

training_data_x = np.array(training_data)[1:,0:2]
training_data_y = np.array(training_data)[1:,2:]


model = Sequential()
model.add(Dense(units=9,input_dim=2))

model.add(Dense(units=15, activation='relu'))
model.add(Dense(units=15, activation='relu'))
model.add(Dense(units=3, activation = 'softmax')) 

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
model.fit((np.array(training_data_x).reshape(-1,2)), np.array(training_data_y).reshape(-1, 3), batch_size = 256,epochs= 3)

model.save_weights('model.h5')
model_json = model.to_json()
with open('model.json', 'w') as json_file:
    json_file.write(model_json)

