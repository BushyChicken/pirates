from game import event
import random
from game.player import Player
from game.context import Context
from game.display import announce
import game.config as config
import game.ship as ship
import game.world as world
import game.events.drowned_pirates as drowned_pirates

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
        if (verb == 'ignore'):
            self.go = True
        elif (verb == 'fish'):
            self.go = True
            r = random.randint(1,10)
            if (r==10):
                self.result["message"] = 'You caught a huge swordfish. This will feed your crew for weeks.'
                self.food = self.food + 50
            elif (9>=r>7):
                self.result["message"] = 'You caught a fine seahorse. This will hold for a while.'
                self.food = self.food + 25
            elif (7>=r>3):
                self.result["message"] = 'You caught a tiny sunfish. Makes a good snack.'
                self.food = self.food + 10
            else:
                drowned_pirates.DrownedPirates().process

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
