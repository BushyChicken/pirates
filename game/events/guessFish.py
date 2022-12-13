import random
class GuessingGame:
    """This is a number guessing game. When an instance is created, it picks a number between 1 and 10, and the user can be asked to guess the number."""
    def __init__(self):
        """When an instance is created, it picks a number between 1 and 10."""
        self.num = random.randint(30,40)

    def getRules(self):
        """Returns a string describing what the player should do, suitable to be printed to prompt them to guess a number between 1 and 10."""
        return "There looks to be between 30 and 40 fish, they said you only have 3 guesses or else."

    def guessCorrect(self):
        """Returns a boolean value, True if the guess matches the object's chosen number or False otherwise."""
        if (x==self.num):
            return "True"
        else:
            return "False"
    def checkGuess(self,guess):
        """Returns 1 if the guess is greater than the chosen number, -1 if it is smaller, and 0 if it is the same."""
        z=guess
        if (z>int(self.num)):
            return 1
        elif (z<int(self.num)):
            return -1
        elif (z==int(self.num)):
            return 0
    def playGame(self):
        """Instructs the current game instance to play itself with the user via the terminal (std i/o)."""
        print(self.getRules())
        z=0
        while z!=3 or z!=4:
            y=self.checkGuess(int(input()))
            if y==-1:
                print ("Too low")
                z=z+1
                if z==3:
                    return 'lost'
            if y==1:
                print ("Too high")
                z=z+1
                if z==3:
                    return 'lost'
            if y==0:
                print ("You have guessed correctly and recieved some food and medicine in return.")
                z=4
                return 'won'
