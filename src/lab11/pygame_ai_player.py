import pygame
import random
import time
from lab11.turn_combat import CombatPlayer

class PyGameAIPlayer:
    def __init__(self) -> None:
        pass

    def selectAction(self, state):
        # there is no goal city yet so select some random city between 1 and 9
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        return random.randint(48, 57)
        #return ord(str(state.current_city)) # no keypress event?


class PyGameAICombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)
        self.initial_weapon = 1
        self.recognized_opponent = 0

    # using the selection strategy from lab 4 does not work
    # The percept is always saying 0 as the opponent weapon when its 1?
    def mimic_selection_strategy(self):
        # strategy that runs if the detected computer is mimic
        return (self.my_choices[-1] + 1) % 3


    def static_selection_strategy(self):
        # strategy that runs if the detected computer is not mimic
        print(self.opponent_choices[-1])
        return (self.opponent_choices[-1] + 1) % 3


    def weapon_selecting_strategy(self):
        while True:
            # on quit quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # too fast slow down
            time.sleep(.5)
            
            # check if the opponent has been identified
            if self.recognized_opponent == 1:
                self.weapon = self.static_selection_strategy()
                return self.weapon
            elif self.recognized_opponent == 2:
                self.weapon = self.mimic_selection_strategy()
                return self.weapon

            # pick random weapon first
            if len(self.opponent_choices) == 0:
                return self.initial_weapon

            # after 3 turns we know for certain if we are fighting the mimic
            elif len(self.opponent_choices) == 3:
                # at turn 3 set recognized_opponent according to who they are
                if self.opponent_choices[0] == self.opponent_choices[1] == self.opponent_choices[2]:
                    self.recognized_opponent = 1
                    self.weapon =  self.static_selection_strategy()
                    return self.weapon
                else:
                    self.recognized_opponent = 2
                    self.weapon = self.mimic_selection_strategy()
                    return self.weapon

            return (self.opponent_choices[-1] + 1) % 3
