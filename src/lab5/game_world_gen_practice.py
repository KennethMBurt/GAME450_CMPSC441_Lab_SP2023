'''
Lab 5: PCG and Project Lab

This a combined procedural content generation and project lab. 
You will be creating the static components of the game that will be used in the project.
Use the landscape.py file to generate a landscape for the game using perlin noise.
Use the lab 2 cities_n_routes.py file to generate cities and routes for the game.
Draw the landscape, cities and routes on the screen using pygame.draw functions.
Look for triple quotes for instructions on what to do where.
The intention of this lab is to get you familiar with the pygame.draw functions, 
use perlin noise to generate a landscape and more importantly,
build a mindset of writing modular code.
This is the first time you will be creating code that you may use later in the project.
So, please try to write good modular code that you can reuse later.
You can always write non-modular code for the first time and then refactor it later.
'''

import sys
import pygame
import random
import numpy as np
from landscape import get_landscape

from pathlib import Path
sys.path.append(str((Path(__file__)/'..'/'..').resolve().absolute()))
from lab2.cities_n_routes import get_randomly_spread_cities, get_routes

def generate_surface(size):
    landscape = get_landscape(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface


def draw_cities(surface, city_names, city_dict):
    city_color = pygame.Color(255, 0, 0)
    for name in city_names:
        pygame.draw.circle(surface, black, city_dict[name], 8)
        pygame.draw.circle(surface, city_color, city_dict[name], 6)

def draw_routes(surface, routes, cities):
    for route in routes:
        pygame.draw.line(surface, black, cities[route[0]], cities[route[1]])


if __name__ == "__main__":
    pygame.init()
    size = width, height = 640, 480
    black = 1, 1, 1

    screen = pygame.display.set_mode(size)
    pygame_surface = generate_surface(size)

    city_names = ['Morkomasto', 'Morathrad', 'Eregailin', 'Corathrad', 'Eregarta',
                  'Numensari', 'Rhunkadi', 'Londathrad', 'Baernlad', 'Forthyr']
    city_locations = [] 
    routes = []

    city_locations = get_randomly_spread_cities(size, 10)
    routes = get_routes(city_names)

    city_locations_dict = {name: location for name, location in zip(city_names, city_locations)}
    random.shuffle(routes)
    routes = routes[:10]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(black)
        screen.blit(pygame_surface, (0, 0))

        draw_cities(pygame_surface, city_names, city_locations_dict)
        draw_routes(pygame_surface, routes, city_locations_dict)

        # printing the name of the city on the map
        for name in city_names:
            font = pygame.font.SysFont(None, 24)
            img = font.render(name, True, black)
            screen.blit(img, city_locations_dict[name])

        pygame.display.flip()
