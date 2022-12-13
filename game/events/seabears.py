from game import event
import random
from game.combat import Combat
from game.combat import Drowned
from game.display import announce

class seaBears (event.Event):

    def __init__ (self):
        self.name = " seabears attack"

    def process (self, world):
        result = {}
        result["message"] = "the seabears are defeated!"
        monsters = []
        min = 2
        uplim = 6
        if random.randrange(2) == 0:
            min = 1
            uplim = 5
            monsters.append(Drowned("Seabear leader"))
            monsters[0].speed = 1.2*monsters[0].speed
            monsters[0].health = 2*monsters[0].health
        n_appearing = random.randrange(min, uplim)
        n = 1
        while n <= n_appearing:
            monsters.append(Drowned("Drowned pirate "+str(n)))
            n += 1
        announce ("You are attacked by a herd of seabears!")
        Combat(monsters).combat()
        announce ("The crew makes good use of the seabears and makes bandages.")
        ship = config.the_player.ship
        ship.medicine = ship.medicine + 2
        result["newevents"] = [ self ]
        return result
