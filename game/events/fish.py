from game import event
import random
from game.player import Player
from game.context import Context
from game.display import announce
import game.config as config

class fish (event.Event):

    def __init__ (self):
        super().__init__()
        self.name = "school of fish"
        self.fish = 1
        self.verbs['ignore'] = self
        self.verbs['catch'] = self
        self.verbs['help'] = self
        self.result = {}
        self.go = False

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == 'ignore'):
            self.go = True
        elif (verb == 'catch'):
            self.go = True
