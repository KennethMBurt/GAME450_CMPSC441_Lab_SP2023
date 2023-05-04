import sys
import pygame
import random
from sprite import Sprite
from pygame_combat import run_pygame_combat
from pygame_human_player import PyGameHumanPlayer
from landscape import get_landscape, get_combat_bg
import numpy as np
from Yippee import generate_encouragement
from pygame_ai_player import PyGameAIPlayer

from pathlib import Path

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from src.lab2.cities_n_routes import get_randomly_spread_cities, get_routes
from src.lab3.travel_cost import get_route_cost
from src.lab5.landscape import elevation_to_rgba
from src.lab7.ga_cities import get_elevation, solution_to_cities, setup_GA, game_fitness

pygame.font.init()
game_font = pygame.font.SysFont("Comic Sans MS", 15)


def get_landscape_surface(size):
    landscape = get_landscape(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface


def get_combat_surface(size):
    landscape = get_combat_bg(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface


def setup_window(width, height, caption):
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return window


def displayCityNames(city_locations, city_names):
    for i, name in enumerate(city_names):
        text_surface = game_font.render(str(i) + " " + name, True, (0, 0, 150))
        screen.blit(text_surface, city_locations[i])


class State:
    def __init__(
        self,
        current_city,
        destination_city,
        travelling,
        encounter_event,
        cities,
        routes,
        money
    ):
        self.current_city = current_city
        self.destination_city = destination_city
        self.travelling = travelling
        self.encounter_event = encounter_event
        self.cities = cities
        self.routes = routes
        self.money = money


if __name__ == "__main__":
    size = width, height = 640, 480
    black = 1, 1, 1
    start_city = 0
    end_city = 9
    sprite_path = "C:/Users/labadmin/PycharmProjects/GAME450_CMPSC441_Lab_SP2023Real/assets/lego.png"
    sprite_speed = 1
    start_money = 1000

    screen = setup_window(width, height, "Game World Gen Practice")

    #implementation of GA cities from labs 5 and 7
    elevation = get_elevation(size)

    # normalize landscape
    elevation = np.array(elevation)
    elevation = (elevation - elevation.min()) / (elevation.max() - elevation.min())
    landscape_surface = pygame.surfarray.make_surface(elevation)

    combat_surface = get_combat_surface(size)
    city_names = [
        "Morkomasto",
        "Morathrad",
        "Eregailin",
        "Corathrad",
        "Eregarta",
        "Numensari",
        "Rhunkadi",
        "Londathrad",
        "Baernlad",
        "Forthyr",
    ]

    # setup fitness function and GA
    fitness = lambda cities, idx: game_fitness(
        cities, idx, elevation=elevation, size=size
    )
    fitness_function, ga_instance = setup_GA(fitness, 10, size)

    # Show one of the initial solutions.
    cities = ga_instance.initial_population[0]
    cities = solution_to_cities(cities, size)

    # Run the GA to optimize the parameters of the function.
    ga_instance.run()

    # Show the best solution after the GA finishes running.
    cities = ga_instance.best_solution()[0]
    cities_t = solution_to_cities(cities, size)

    #cities
    routes = get_routes(cities_t)


    random.shuffle(routes)
    routes = routes[:10]

    player_sprite = Sprite(sprite_path, cities_t[start_city])

    player = PyGameHumanPlayer()
    """ Add a line below that will reset the player variable to 
    a new object of PyGameAIPlayer class."""

    state = State(
        current_city=start_city,
        destination_city=start_city,
        travelling=False,
        encounter_event=False,
        cities=cities_t,
        routes=routes,
        money=start_money,
    )

    while True:
        action = player.selectAction(state)
        if 0 <= int(chr(action)) <= 9:
            if int(chr(action)) != state.current_city and not state.travelling:
                start = cities_t[state.current_city]
                state.destination_city = int(chr(action))
                destination = cities_t[state.destination_city]
                # only allow movement between connected cities
                goNext = False
                for route in routes:
                    if int(start[0]) is int(route[0][0]) and int(start[1]) is int(route[0][1]):
                        if int(destination[0]) is int(route[1][0]) and int(destination[1]) is int(route[1][1]):
                            goNext = True
                    elif int(start[0]) is int(route[1][0]) and int(start[1]) is int(route[1][1]):
                        if int(destination[0]) is int(route[0][0]) and int(destination[1]) is int(route[0][1]):
                            goNext = True

                if goNext:
                    player_sprite.set_location(cities_t[state.current_city])
                    state.travelling = True

                    #calculating cost of route
                    cost = get_route_cost((start, destination), elevation)
                    state.money = state.money - cost
                    if state.money < 0:
                        print('You ran out of money. You Lose!')
                        print(generate_encouragement())
                        break
                    print(
                        "Travelling from", state.current_city, "to", state.destination_city
                    )
                    print(generate_encouragement())
                else:
                    print("Those Cities are not connected")
                    print(generate_encouragement())

        screen.fill(black)
        screen.blit(landscape_surface, (0, 0))

        for city in cities_t:
            pygame.draw.circle(screen, (255, 0, 0), city, 5)

        for line in routes:
            pygame.draw.line(screen, (255, 0, 0), *line)

        displayCityNames(cities_t, city_names)
        if state.travelling:
            state.travelling = player_sprite.move_sprite(destination, sprite_speed)
            state.encounter_event = random.randint(0, 1000) < 2
            if not state.travelling:
                print('Arrived at', state.destination_city)
                print(generate_encouragement())

        if not state.travelling:
            encounter_event = False
            state.current_city = state.destination_city

        if state.encounter_event:
            run_pygame_combat(combat_surface, screen, player_sprite)
            state.encounter_event = False
        else:
            player_sprite.draw_sprite(screen)
        pygame.display.update()
        if state.current_city == end_city:
            print('You have reached the end of the game!')
            break
