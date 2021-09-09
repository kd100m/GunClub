import random

map = ['Warehouse', 'Urban Sprawl', 'Savannah', 'Area 51', 'Jungle']
time_of_day = ['Night','Day']


def draw_map():
  print(random.choice(map))
  print(random.choice(time_of_day))
