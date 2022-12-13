import random
from game import event
from game.player import Player
from game.context import Context
from game.display import announce
import game.config as config
import game.ship as ship
import game.world as world
import game.events.drowned_pirates as drowned_pirates
import game.events.guessFish as guessFish
import game.crewmate as crewmate
import game.combat as combat

class Fish (Context, event.Event):

    def __init__ (self):
        super().__init__()
        self.name = "school of fish"
        self.fish = 1
        self.verbs['ignore'] = self
        self.verbs['fish'] = self
        self.verbs['help'] = self
        self.result = {}
        self.go = False
        
        
        
    def process_verb (self, verb, cmd_list, nouns):
        ship = config.the_player.ship
        hom = config.the_player.world
        if (verb == 'ignore'):
            self.go = True
        elif (verb == 'fish'):
            self.go = True
            r = random.randint(0,20)
            if (20>=r>18):
                self.result["message"] = 'You caught a huge swordfish. This will feed your crew for weeks.'
                ship.food = ship.food + 25
            elif (18>=r>15):
                self.result["message"] = 'You caught a fine seahorse. This will hold for a while.'
                ship.food = ship.food + 10
            elif (15>=r>11):
                self.result["message"] = 'You caught a tiny sunfish. Makes a good snack.'
                ship.food = ship.food + 5
            elif (11>=r>19):
                self.result["message"] = 'You defeated the drowned pirates.'
                drowned_pirates.DrownedPirates().process(config.the_player.world)
            elif (9>=r>6):
                self.result["message"] = 'Some bandages are caught in the line.'
                ship.medicine = ship.medicine + 1
            elif (6>=r>3):
                self.result["message"] = 'The coordinates for home port were found in the water.'
                print(hom.home)
            elif (3>=r>=0):
                print('A strange figure emerges from the water, they ask you to guess how many fish are.')
                x = guessFish.GuessingGame().playGame()
                if x == 'won':
                    self.result["message"] = 'You got it right, The figure decides to give food and medicine.'
                    ship.medicine = ship.medicine + 3
                    ship.food = ship.food + 25
                elif x == 'lost':
                    self.result["message"] = 'You lost, the figure spawns drowned pirates.'
                    drowned_pirates.DrownedPirates().process(config.the_player.world)
                
        elif (verb == "help"):
            print('The crew notices a school of fish passing through, you can try and catch or ignore')
            self.go = False
        else:
            print('Would you like to ignore or start fishing')
            self.go = False
            
    def process (self, world):

            self.go = False
            self.result = {}
            self.result["newevents"] = [ self ]
            self.result["message"] = "default message"

            while (self.go == False):
                print (str (self.fish) + " school of fish has appeared, what do you want to do?")
                Player.get_interaction ([self])

            return self.result
            
