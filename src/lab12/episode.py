import sys
from pathlib import Path

import src.lab11.turn_combat as tc
import src.lab11.pygame_combat as pygc
from src.lab11.pygame_ai_player import PyGameAICombatPlayer

''' 
Lab 12: Beginnings of Reinforcement Learning
We will modularize the code in pygrame_combat.py from lab 11 together.

Then it's your turn!
Create a function called run_episode that takes in two players
and runs a single episode of combat between them. 
As per RL conventions, the function should return a list of tuples
of the form (observation/state, action, reward) for each turn in the episode.
Note that observation/state is a tuple of the form (player1_health, player2_health).
Action is simply the weapon selected by the player.
Reward is the reward for the player for that turn.
'''
#This is the main branch

def run_episode(AI_player, computer):
    # begin combat
    combat = tc.Combat()

    # list to hold the end of turn tuples
    turns_tuple = []

    # run the game
    while not combat.gameOver:
        turn_end = pygc.run_turn(AI_player, computer, combat)
        turns_tuple.append(turn_end)

    return turns_tuple


if __name__ == '__main__':
    player = PyGameAICombatPlayer("Computer Boy")
    opponent = pygc.PyGameComputerCombatPlayer("Computer")
    resp = run_episode(player, opponent)
    print(resp)