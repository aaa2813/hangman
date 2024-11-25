# Basic hangman program
import re
import random
import os
import sys
import time

class word:
    '''
    A class defining a term to be guessed. A word can have spaces and some special characters for readability during the game, but only letters and numbers can be used in guesses.
    '''

    def __init__(self, inString : str):
        '''
        Word constructor. Takes a string and stores list of key letters and numbers. Only capital letters used.
        '''

        # Start with 6HP - 1 head, 1 torso, 2 arms, 2 legs
        self.HP = 6

        # Capitalize input string, store as key
        self.key = inString.upper()

        # Create string with underscores for use in game
        self.gamestring = re.sub("[A-Z0-9]", "_", self.key)

        # Drop non-letter and non-number characters from string
        letterString = re.sub("[^A-Z0-9]", "", self.key)

        # Get list of all characters in key
        characters = list(letterString)
        self.chars = set(characters) # Order not preserved

        # Also keep list of correct & incorrect guesses
        self.correct = []
        self.incorrect = []


    def __str__(self):
        '''
        Custom print out - adds spaces between underscores for readability
        '''
        string = re.sub("[ ]", "    ", self.gamestring) # Step 1 - add more space between words
        return re.sub("(_|[A-Z0-9])", " \\1", string) # Step 2 - add space between characters


    def guess(self, guesschar : str):
        '''
        Function for guessing. Returns boolean indicating match or no match.
        If guess is a match, replace all instances of the guess in the gamestring with the corresponding letter, do not deduct HP.
        If guess is not a match, do nothing to the gamestring, deduct 1HP.
        If guess is not a single letter/number entry, nothing is done.
        '''

        # Check guess length and type
        if not (len(guesschar)==1 and guesschar.isalnum()):
            print("Guess is not a valid character!")
        
        else:
            guesschar = guesschar.upper() # Capitalize guestchar
            # Check if guess is in chars
            if guesschar in self.chars:
                # Construct new gamestring by replacing old gamestring with each instance of guesschar found in key
                # TODO - need to fix this part
                newstring = ''
                for i,char in enumerate(self.key):
                    if self.key[i] == guesschar:
                        newstring += guesschar # Append guessed character to new string
                    else:
                        newstring += self.gamestring[i] # Append character (underscore or other) to new string
                self.gamestring = newstring # Update gamestring
                self.chars.remove(guesschar) # Removed guessed character from internal set
                self.correct.append(guesschar) # Add guessed character to correct list
                print("Congrats! {} was a valid guess!".format(guesschar))
            else:
                self.HP -= 1 # Deduct 1HP for incorrect guess
                self.incorrect.append(guesschar) # Add guessed character to incorrect list
                print("Sorry! {} was an incorrect guess!".format(guesschar))


class game:
    '''
    A class defining a single game session. Each game starts by getting a random entry from a specified .txt list and creating a word object. The game is over when:
        1. All characters were successfully guessed (chars list empty)
        2. HP reaches 0
        3. "Exit" or "quit" typed in console
    '''

    def __init__(self, filepath):
        '''
        Game constructor. Takes user-specified filepath and picks random entry as word for the game.
        '''
        try:
            entry = random_line(filepath).strip()
        except:
            print("File read failed.")
            exit()

        # Initialize game
        gameword = word(entry)

        print("Welcome to Hangman!")
        print("Type single characters (numbers & letters) to guess the word! Type 'quit' or 'exit' to end game.")
        time.sleep(5)

        # Main game loop
        while True:
            # Clear previous console text
            cls()

            # Print health, guessed characters, incorrect characters
            print("Guessed characters: {}    Misses: {}".format(gameword.correct, gameword.incorrect))
            print(HANGMANPICS[gameword.HP])
            print(gameword)
            guess = input("What is your guess? ")

            # Check exit conditions, otherwise keep playing
            if guess == "quit" or guess == "exit" or gameword.HP == 0:
                print("The word was '{}'. Better luck next time!".format(gameword.key))
                exit()
            # Word guessed
            elif guess.upper() == gameword.key:
                print("You got it! Congrats!".format(gameword.key))
                exit()
            # Game won
            elif not gameword.chars:
                print("The word was '{}'. Congrats!".format(gameword.key))
                exit()
            # Regular game guess
            else:
                gameword.guess(guess)
            time.sleep(5)

    def run(self):
        pass
    

def random_line(filename):
    '''
    Get random entry from file.
    '''
    with open(filename) as f:
        line = next(f)
        for num, aline in enumerate(f, 2):
            if random.randrange(num):
                continue
            line = aline
    return line

def cls():
    '''
    Clear screen.
    '''
    os.system('cls' if os.name=='nt' else 'clear')

HANGMANPICS = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']


if len(sys.argv) != 2:
    print("Incorrect number of arguments. Please specify file path as argument.")
else:
    cls()
    game(sys.argv[1])


'''
testword = word("Hello, world!")

print(testword)

testword.guess(";")
testword.guess("3") # Deducts HP, words stay the same

game("movies.txt")
'''