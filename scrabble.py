import os
from ast import literal_eval
from random import shuffle

from termcolor import colored

"""
Scrabble Game
Classes:
Tile - keeps track of the tile letter and value
Rack - keeps track of the tiles in a player's letter rack
Bag - keeps track of the remaining tiles in the bag
Word - checks the validity of a word and its placement
Board - keeps track of the tiles' location on the board
"""
#Keeps track of the score-worth of each letter-tile.
LETTER_VALUES = {"A": 1,
                 "B": 3,
                 "C": 3,
                 "D": 2,
                 "E": 1,
                 "F": 4,
                 "G": 2,
                 "H": 4,
                 "I": 1,
                 "J": 8,
                 "K": 5,
                 "L": 1,
                 "M": 3,
                 "N": 1,
                 "O": 1,
                 "P": 3,
                 "Q": 10,
                 "R": 1,
                 "S": 1,
                 "T": 1,
                 "U": 1,
                 "V": 4,
                 "W": 4,
                 "X": 8,
                 "Y": 4,
                 "Z": 10,
                 "#": 0}

def print_instructions():
    print(colored("INSTRUCTIONS".center(os.get_terminal_size()[0],"!"),'red'))
    print(
        """This Scrabble(TM) Game has been designed for 2-4 players
NOTE: All characters can be typed lower- or upper-case.
-----BLANK/WILDCARD TILES-----
There are two blank/wildcard tiles in the game (represented by #).
]These tiles are worth 0 points, but may help you build words.
To use a blank tile, type the word with # in its place.
For example, type 'wor#' if you want to use it to play 'word'.
The program will ask you to pick what letter # will represent.
When the wildcard is placed on the board, it will look like '.D.'
-----USING THE BOARD-----
The board has its columns and rows labeled for reference.
You will provide a start position and direction of the word.
Start position is the column and row of the first letter.
Direction is how to orient the word, down or right.
You will provide a 3-character command for placement.
    First = column, second = row, third = direction
Here are some examples:
    77d - would start at column 7, row 7, and go down from there
    0ar - would start at column 0, row a, and go to the right
-----SPECIAL SPACES-----
"""+colored(" + ","white","on_light_magenta")+"= DOUBLE WORD SCORE            "+colored(" * ","white","on_red")+"""= TRIPLE WORD SCORE
"""+colored(" < ","white","on_light_blue")+"= DOUBLE LETTER SCORE          "+colored(" ^ ","white","on_blue")+"""= TRIPLE LETTER SCORE
-----SPECIAL COMMANDS-----
When you are asked to type a word, you can also type commands:
    shuffle rack - will randomly shuffle your tiles
    print instructions - will print the instructions again
Other special commands will be added as required"""
    )
    input("Press ENTER to continue")

def wait_until_terminal_size_correct():
    if os.get_terminal_size().lines < 28:
        print("Your terminal is too short. Increase the height of your terminal (or decrease the size of the font).")
        while os.get_terminal_size().lines < 28:
            continue
    if os.get_terminal_size().columns < 66:
        print("Your terminal is too narrow. Increase the width of your terminal (or decrease the size of the font).")
        while os.get_terminal_size().columns < 66:
            continue

class Tile:
    """
    Class that allows for the creation of a tile. Initializes using an uppercase string of one letter,
    and an integer representing that letter's score.
    """
    def __init__(self, letter, letter_values):
        #Initializes the tile class. Takes the letter as a string, and the dictionary of letter values as arguments.
        self.letter = letter.upper()
        if self.letter in letter_values:
            self.score = letter_values[self.letter]
        else:
            self.score = 0

    def get_letter(self):
        #Returns the tile's letter (string).
        return self.letter

    def set_letter(self,new_letter):
        #Set a blank tile to the letter to be used
        if self.letter == "#":
            self.letter = new_letter
        else:
            print(f"Trying to set a new letter when letter {self.letter} is already assigned.")

    def get_score(self):
        #Returns the tile's score value.
        return self.score

class Bag:
    """
    Creates the bag of all tiles that will be available during the game. Contains 98 letters and two blank tiles.
    Takes no arguments to initialize.
    """
    def __init__(self):
        #Creates the bag full of game tiles, and calls the initialize_bag() method, which adds the default 100 tiles to the bag.
        #Takes no arguments.
        self.bag = []
        self.initialize_bag()

    def add_to_bag(self, tile, quantity):
        #Adds a certain quantity of a certain tile to the bag. Takes a tile and an integer quantity as arguments.
        for i in range(quantity):
            self.bag.append(tile)

    def initialize_bag(self):
        #Adds the intiial 100 tiles to the bag.
        global LETTER_VALUES
        self.add_to_bag(Tile("A", LETTER_VALUES), 9)
        self.add_to_bag(Tile("B", LETTER_VALUES), 2)
        self.add_to_bag(Tile("C", LETTER_VALUES), 2)
        self.add_to_bag(Tile("D", LETTER_VALUES), 4)
        self.add_to_bag(Tile("E", LETTER_VALUES), 12)
        self.add_to_bag(Tile("F", LETTER_VALUES), 2)
        self.add_to_bag(Tile("G", LETTER_VALUES), 3)
        self.add_to_bag(Tile("H", LETTER_VALUES), 2)
        self.add_to_bag(Tile("I", LETTER_VALUES), 9)
        self.add_to_bag(Tile("J", LETTER_VALUES), 1)
        self.add_to_bag(Tile("K", LETTER_VALUES), 1)
        self.add_to_bag(Tile("L", LETTER_VALUES), 4)
        self.add_to_bag(Tile("M", LETTER_VALUES), 2)
        self.add_to_bag(Tile("N", LETTER_VALUES), 6)
        self.add_to_bag(Tile("O", LETTER_VALUES), 8)
        self.add_to_bag(Tile("P", LETTER_VALUES), 2)
        self.add_to_bag(Tile("Q", LETTER_VALUES), 1)
        self.add_to_bag(Tile("R", LETTER_VALUES), 6)
        self.add_to_bag(Tile("S", LETTER_VALUES), 4)
        self.add_to_bag(Tile("T", LETTER_VALUES), 6)
        self.add_to_bag(Tile("U", LETTER_VALUES), 4)
        self.add_to_bag(Tile("V", LETTER_VALUES), 2)
        self.add_to_bag(Tile("W", LETTER_VALUES), 2)
        self.add_to_bag(Tile("X", LETTER_VALUES), 1)
        self.add_to_bag(Tile("Y", LETTER_VALUES), 2)
        self.add_to_bag(Tile("Z", LETTER_VALUES), 1)
        self.add_to_bag(Tile("#", LETTER_VALUES), 2)
        shuffle(self.bag)

    def take_from_bag(self):
        #Removes a tile from the bag and returns it to the user. This is used for replenishing the rack.
        return self.bag.pop()

    def return_to_bag(self, letters):
        #Puts tiles back in that player wishes to return
        for letter in letters:
            self.add_to_bag(letter, 1)

    def get_remaining_tiles(self):
        #Returns the number of tiles left in the bag.
        return len(self.bag)

class Rack:
    """
    Creates each player's 'dock', or 'hand'. Allows players to add, remove and replenish the number of tiles in their hand.
    """
    def __init__(self, bag):
        #Initializes the player's rack/hand. Takes the bag from which the racks tiles will come as an argument.
        self.rack = []
        self.bag = bag
        self.initialize()

    def add_to_rack(self):
        #Takes a tile from the bag and adds it to the player's rack.
        self.rack.append(self.bag.take_from_bag())

    def initialize(self):
        #Adds the initial 7 tiles to the player's hand.
        for i in range(7):
            self.add_to_rack()

    def get_rack_str(self):
        #Displays the user's rack in string form.
        return ", ".join(str(item.get_letter()) for item in self.rack)

    def get_rack_pts(self):
        #Display the user's letter scores in string form
        return ", ".join(str(item.get_score()) for item in self.rack)

    def get_rack_arr(self):
        #Returns the rack as an array of tile instances
        return self.rack

    def shuffle_rack(self):
        shuffle(self.rack)

    def remove_from_rack(self, tile):
        #Removes a tile from the rack (for example, when a tile is being played).
        self.rack.remove(tile)

    def get_rack_length(self):
        #Returns the number of tiles left in the rack.
        return len(self.rack)

    def replenish_rack(self):
        #Adds tiles to the rack after a turn such that the rack will have 7 tiles (assuming a proper number of tiles in the bag).
        while self.get_rack_length() < 7 and self.bag.get_remaining_tiles() > 0:
            self.add_to_rack()

class Player:
    """
    Creates an instance of a player. Initializes the player's rack, and allows you to set/get a player name.
    """
    def __init__(self, bag):
        #Intializes a player instance. Creates the player's rack by creating an instance of that class.
        #Takes the bag as an argument, in order to create the rack.
        self.name = ""
        self.rack = Rack(bag)
        self.running_score = []
        self.score = 0

    def set_name(self, name):
        #Sets the player's name.
        self.name = name

    def get_name(self):
        #Gets the player's name.
        return self.name

    def get_rack_str(self):
        #Returns the player's rack.
        return self.rack.get_rack_str()

    def get_rack_pts(self):
        #Returns the player's letter point values
        return self.rack.get_rack_pts()

    def get_rack_arr(self):
        #Returns the player's rack in the form of an array.
        return self.rack.get_rack_arr()

    def shuffle_rack(self):
        self.rack.shuffle_rack()

    def increase_score(self, increase):
        #Increases the player's score by a certain amount. Takes the increase (int) as an argument and adds it to the score.
        self.score += increase

    def add_running_score(self, score):
        # add score for a round
        self.running_score.append(score)

    def get_running_score(self):
        # display the running score
        if len(self.running_score) > 10:
            return "...+"+"+".join([str(x) for x in self.running_score[-10:]])
        return "+".join([str(x) for x in self.running_score])

    def get_score(self):
        #Returns the player's score
        return self.score

class Board:
    """
    Creates the scrabble board.
    """
    def __init__(self):
        #Creates a 2-dimensional array that will serve as the board, as well as adds in the premium squares.
        self.board = [["___" for i in range(15)] for j in range(15)]
        self.add_premium_squares()

    def get_board(self):
        #Returns the board in string form.
        board_str = " | " + " | ".join(str(item) for item in range(10)) + " | " + " | ".join(ch for ch in 'abcde') + " | \n"
        # board_str = "   |  " + "  |  ".join(str(item) for item in range(10)) + "  | " + "  | ".join(str(item) for item in range(10, 15)) + " |"
        # board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
        board = list(self.board)
        for i in range(len(board)):
            if i < 10:
                board[i] = str(i) + "|" + "|".join(str(item) for item in board[i]) + "|"+str(i)
                # board[i] = str(i) + "  | " + " | ".join(str(item) for item in board[i]) + " |"
            if i >= 10:
                board[i] = hex(i)[2] + "|" + "|".join(str(item) for item in board[i]) + "|"+hex(i)[2]
                # board[i] = str(i) + " | " + " | ".join(str(item) for item in board[i]) + " |"
        board_str += "\n".join(board)
        board_str += "\n | " + " | ".join(str(item) for item in range(10)) + " | " + " | ".join(ch for ch in 'abcde') + " | "
        # board_str += "\n   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n".join(board)
        # board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
        return board_str

    def add_premium_squares(self):
        #Adds all of the premium squares that influence the word's score.
        TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
        DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10), (7,7))
        TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
        DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

        for coordinate in TRIPLE_WORD_SCORE:
            self.board[coordinate[0]][coordinate[1]] = colored("_*_","white","on_red")
        for coordinate in TRIPLE_LETTER_SCORE:
            self.board[coordinate[0]][coordinate[1]] = colored("_^_","white","on_blue")
        for coordinate in DOUBLE_WORD_SCORE:
            self.board[coordinate[0]][coordinate[1]] = colored("_+_","white","on_light_magenta")
        for coordinate in DOUBLE_LETTER_SCORE:
            self.board[coordinate[0]][coordinate[1]] = colored("_<_","white","on_light_blue")

    def place_word(self, word, location, direction, player, blanks):
        #Allows you to play words, assuming that they have already been confirmed as valid.
        global premium_spots
        premium_spots = []
        direction = direction.lower()
        word = word.upper()

        count = 0

        #Places the word going rightwards
        if direction.lower() == "right":
            for i in range(len(word)):
                if '.' in self.board[location[0]][location[1]+i]:
                    premium_spots.append((word[i], "ZPT", i))
                    continue
                elif self.board[location[0]][location[1]+i] == word[i].join(["_"]*2):
                    continue
                else:
                    if self.board[location[0]][location[1]+i] != "___":
                        premium_spots.append((word[i], self.board[location[0]][location[1]+i].split("_")[1].join(['_']*2), i))
                    if word[i] != "#":
                        self.board[location[0]][location[1]+i] = "_" + word[i] + "_"
                    else:
                        premium_spots.append((blanks[0], "ZPT", i))
                        self.board[location[0]][location[1]+i] = "." + blanks[0] + "."
                        blanks = blanks[1:]
                    #Removes tiles from player's rack
                    for tile in player.get_rack_arr():
                        if tile.get_letter() == word[i]:
                            print(f"Removed {tile.get_letter()} from player rack.")
                            player.rack.remove_from_rack(tile)
                            count += 1
                            break

        #Places the word going downwards
        elif direction.lower() == "down":
            for i in range(len(word)):
                if '.' in self.board[location[0]+i][location[1]]:
                    premium_spots.append((word[i], "ZPT", i))
                    continue
                elif self.board[location[0]+i][location[1]] == word[i].join(["_"]*2):
                    continue
                else:
                    if self.board[location[0]+i][location[1]] != "___":
                        premium_spots.append((word[i], self.board[location[0]+i][location[1]].split("_")[1].join(['_']*2), i))
                    if word[i] != "#":
                        self.board[location[0]+i][location[1]] = "_" + word[i] + "_"
                    else:
                        premium_spots.append((blanks[0], "ZPT", i))
                        self.board[location[0]+i][location[1]] = "." + blanks[0] + "."
                        blanks = blanks[1:]
                    #Removes tiles from player's rack
                    for tile in player.get_rack_arr():
                        if tile.get_letter() == word[i]:
                            # print(f"Removed {tile.get_letter()} from player rack.")
                            player.rack.remove_from_rack(tile)
                            count += 1
                            break

        if count == 7:
            print("BONUS for using all 7 of your tiles!!!")
            player.increase_score(50)
        #Replaces tiles with tiles from the bag.
        player.rack.replenish_rack()

    def prelim_place_word(self, word, location, direction, player):
        #Allows you to play words, assuming that they have already been confirmed as valid.
        global premium_spots
        premium_spots = []
        direction = direction.lower()
        word = word.upper()

        #Places the word going rightwards
        if direction.lower() == "right":
            for i in range(len(word)):
                if '.' in self.board[location[0]][location[1]+i]:
                    premium_spots.append((word[i], "ZPT", i))
                elif self.board[location[0]][location[1]+i] != "___":
                    premium_spots.append((word[i], self.board[location[0]][location[1]+i].split("_")[1].join(['_']*2), i))

        #Places the word going downwards
        elif direction.lower() == "down":
            for i in range(len(word)):
                if '.' in self.board[location[0]+i][location[1]]:
                    premium_spots.append((word[i], "ZPT", i))
                elif self.board[location[0]+i][location[1]] != "___":
                    premium_spots.append((word[i], self.board[location[0]+i][location[1]].split("_")[1].join(['_']*2), i))

    def board_array(self):
        #Returns the 2-dimensional board array.
        return self.board

class Word:
    def __init__(self, word, location, player, direction, board):
        self.word = word.upper()
        self.location = location
        self.player = player
        self.direction = direction.lower()
        self.board = board
        self.other_words_intersect = []

    def check_word(self):
        #Checks the word to make sure that it is in the dictionary, and that the location falls within bounds.
        #Also controls the overlapping of words.
        global round_number, players
        word_score = 0
        global dictionary 
        if "dictionary" not in globals():
            dictionary = open("dic.txt").read().splitlines()

        current_board_ltr = ""
        # other_words_intersect = []
        needed_tiles = ""
        blank_tile_val = []

        #Assuming that the player is not skipping the turn:
        if self.word != "":

            #Raises an error if the location of the word will be out of bounds.
            if self.location[0] > 14 or self.location[1] > 14 or self.location[0] < 0 or self.location[1] < 0 or (self.direction == "down" and (self.location[0]+len(self.word)-1) > 14) or (self.direction == "right" and (self.location[1]+len(self.word)-1) > 14):
                return ["Location out of bounds.\n"]

            #Allows for players to declare the value of a blank tile.
            i = 0
            while "#" in self.word:
                ordinals = ['first','second','third','fourth','fifth','sixth','seventh']
                blank_tile_val.append(input(f"Please enter the letter value of the {ordinals[i]} blank tile: ").upper())
                self.word = self.word[:self.word.index("#")] + blank_tile_val[i].upper() + self.word[(self.word.index("#")+1):]
                i += 1

            #Reads in the board's current values under where the word that is being played will go. Raises an error if the direction is not valid.
            if self.direction == "right":
                j = -1
                while self.location[1]+j >= 0 and ("." in self.board[self.location[0]][self.location[1]+j] or "." not in self.board[self.location[0]][self.location[1]+j] and self.board[self.location[0]][self.location[1]+j].split("_")[1].join(['_']*2) not in ["__","_^_","_*_","_<_","_+_"]):
                    current_board_ltr = self.board[self.location[0]][self.location[1]+j][1] + current_board_ltr
                    self.word = self.board[self.location[0]][self.location[1]+j][1] + self.word
                    j -= 1
                for i in range(len(self.word)):
                    if "." in self.board[self.location[0]][self.location[1]+i]:
                        current_board_ltr += self.board[self.location[0]][self.location[1]+i][1]
                    elif self.board[self.location[0]][self.location[1]+i].split("_")[1].join(['_']*2) in ["__","_^_","_*_","_<_","_+_"]:
                        current_board_ltr += "_"
                        j = -1
                        other_word = ""
                        while self.location[0]+j>=0 and ("." in self.board[self.location[0]+j][self.location[1]+i] or "." not in self.board[self.location[0]+j][self.location[1]+i] and self.board[self.location[0]+j][self.location[1]+i].split("_")[1].join(['_']*2) not in ["__","_^_","_*_","_<_","_+_"]):
                            other_word = self.board[self.location[0]+j][self.location[1]+i][1] + other_word
                            start_position = [self.location[0]+j, self.location[1]+i]
                            j -= 1
                        if other_word:
                            other_word += self.word[i]
                            j = 1
                            while self.location[0]+j<=14 and ("." in self.board[self.location[0]+j][self.location[1]+i] or "." not in self.board[self.location[0]+j][self.location[1]+i] and self.board[self.location[0]+j][self.location[1]+i].split("_")[1].join(['_']*2) not in ["__","_^_","_*_","_<_","_+_"]):
                                other_word += self.board[self.location[0]+j][self.location[1]+i][1]
                                j += 1
                        else:
                            start_position = [self.location[0], self.location[1]+i]
                            j = 1
                            while self.location[0]+j<=14 and ("." in self.board[self.location[0]+j][self.location[1]+i] or "." not in self.board[self.location[0]+j][self.location[1]+i] and self.board[self.location[0]+j][self.location[1]+i].split("_")[1].join(['_']*2) not in ["__","_^_","_*_","_<_","_+_"]):
                                other_word += self.board[self.location[0]+j][self.location[1]+i][1]
                                j += 1
                            if other_word:
                                other_word = self.word[i] + other_word
                        if other_word:
                            # print(f"Found an intersecting word: {other_word}")
                            self.other_words_intersect.append(Word(other_word, start_position, self.player, 'down', self.board))
                    else:
                        current_board_ltr += self.board[self.location[0]][self.location[1]+i][1]
                i += 1
                while self.location[1]+i <= 14 and ("." in self.board[self.location[0]][self.location[1]+i] or "." not in self.board[self.location[0]][self.location[1]+i] and self.board[self.location[0]][self.location[1]+i].split("_")[1].join(['_']*2) not in ["__","_^_","_*_","_<_","_+_"]):
                    current_board_ltr += self.board[self.location[0]][self.location[1]+i][1]
                    self.word += self.board[self.location[0]][self.location[1]+i][1]
                    i += 1
            elif self.direction == "down":
                j = -1
                while self.location[0]+j >= 0 and ("." in self.board[self.location[0]+j][self.location[1]] or "." not in self.board[self.location[0]+j][self.location[1]] and self.board[self.location[0]+j][self.location[1]].split("_")[1].join(['_']*2) not in ["__","_^_","_*_","_<_","_+_"]):
                    current_board_ltr = self.board[self.location[0]+j][self.location[1]][1] + current_board_ltr
                    self.word = self.board[self.location[0]+j][self.location[1]][1] + self.word
                    j -= 1
                for i in range(len(self.word)):
                    if "." in self.board[self.location[0]+i][self.location[1]]:
                        current_board_ltr += self.board[self.location[0]+i][self.location[1]][1]
                    elif self.board[self.location[0]+i][self.location[1]].split("_")[1].join(['_']*2) in ["__","_^_","_*_","_<_","_+_"]:
                        current_board_ltr += "_"
                        j = -1
                        other_word = ""
                        while self.location[1]+j>=0 and ("." in self.board[self.location[0]+i][self.location[1]+j] or "." not in self.board[self.location[0]+i][self.location[1]+j] and self.board[self.location[0]+i][self.location[1]+j].split("_")[1].join(['_']*2) not in ["__","_^_","_*_","_<_","_+_"]):
                            other_word = self.board[self.location[0]+i][self.location[1]+j][1] + other_word
                            start_position = [self.location[0]+i, self.location[1]+j]
                            j -= 1
                        if other_word:
                            other_word += self.word[i]
                            j = 1
                            while self.location[1]+j<=14 and ("." in self.board[self.location[0]+i][self.location[1]+j] or "." not in self.board[self.location[0]+i][self.location[1]+j] and self.board[self.location[0]+i][self.location[1]+j].split("_")[1].join(['_']*2) not in ["__","_^_","_*_","_<_","_+_"]):
                                other_word += self.board[self.location[0]+i][self.location[1]+j][1]
                                j += 1
                        else:
                            start_position = [self.location[0]+i, self.location[1]]
                            j = 1
                            while self.location[1]+j<=14 and ("." in self.board[self.location[0]+i][self.location[1]+j] or "." not in self.board[self.location[0]+i][self.location[1]+j] and self.board[self.location[0]+i][self.location[1]+j].split("_")[1].join(['_']*2) not in ["__","_^_","_*_","_<_","_+_"]):
                                other_word += self.board[self.location[0]+i][self.location[1]+j][1]
                                j += 1
                            if other_word:
                                other_word = self.word[i] + other_word
                        if other_word:
                            # print(f"Found an intersecting word: {other_word}")
                            self.other_words_intersect.append(Word(other_word, start_position, self.player, 'right', self.board))
                    else:
                        current_board_ltr += self.board[self.location[0]+i][self.location[1]][1]
                i += 1
                while self.location[0]+i <= 14 and ("." in self.board[self.location[0]+i][self.location[1]] or "." not in self.board[self.location[0]+i][self.location[1]] and self.board[self.location[0]+i][self.location[1]].split("_")[1].join(['_']*2) not in ["__","_^_","_*_","_<_","_+_"]):
                    current_board_ltr += self.board[self.location[0]+i][self.location[1]][1]
                    self.word += self.board[self.location[0]+i][self.location[1]][1]
                    i += 1
            else:
                return ["Error: please enter a valid direction."]

            #Raises an error if the word being played is not in the official scrabble dictionary (dic.txt).
            if self.word not in dictionary:
                return [f"Please enter a valid dictionary word. {self.word} is not in the dictionary.\n"]

            for one_other_word in self.other_words_intersect:
                if one_other_word.word not in dictionary:
                    return [f"One of the intersecting words - {one_other_word.word} - is not a valid dictionary word."]

            #Ensures that the words overlap correctly. If there are conflicting letters between the current board and the word being played, raises an error.
            for i in range(len(self.word)):
                if current_board_ltr[i] == "_":
                    needed_tiles += self.word[i]
                elif current_board_ltr[i] != self.word[i]:
                    print("Current_board_ltr: " + str(current_board_ltr) + ", Word: " + self.word + ", Needed_Tiles: " + needed_tiles)
                    return ["The letters do not overlap correctly, please choose another word."]

            #If there is a blank tile, remove it's given value from the tiles needed to play the word.
            for blank_tile in blank_tile_val:
                needed_tiles = needed_tiles[needed_tiles.index(blank_tile.upper())+1:] + needed_tiles[:needed_tiles.index(blank_tile.upper())]

            #Ensures that the word will be connected to other words on the playing board.
            if (round_number != 1 or (round_number == 1 and players[0] != self.player)) and current_board_ltr == "_" * len(self.word) and len(self.other_words_intersect)==0:
                print("Current_board_ltr: " + str(current_board_ltr) + ", Word: " + self.word + ", Needed_Tiles: " + needed_tiles)
                return ["Please connect the word to a previously played letter."]

            #Raises an error if the player does not have the correct tiles to play the word.
            for letter in needed_tiles:
                if letter not in self.player.get_rack_str() or self.player.get_rack_str().count(letter) < needed_tiles.count(letter):
                    return ["You do not have the tiles for this word\n"]

            #Ensures that first turn of the game will have the word placed at (7,7).
            if round_number == 1 and players[0] == self.player:
                if (self.direction == "down" and self.location[1] != 7 or self.location[0] > 7 or (self.location[0]+len(self.word)-1) < 7
                ) or (self.direction == "right" and self.location[0] != 7 and self.location[1] > 7 and (self.location[1]+len(self.word)-1) < 7):
                    return ["The first turn must pass through location (7, 7).\n"]
            return [True, self.word, blank_tile_val]

        #If the user IS skipping the turn, confirm. If the user replies with "Y", skip the player's turn. Otherwise, allow the user to enter another word.
        else:
            if input("Are you sure you would like to skip your turn? (y/n)").upper() == "Y":
                if round_number == 1 and players[0] == self.player:
                    return "Please do not skip the first turn. Please enter a word."
                return [True, self.word]
            else:
                return ["Please enter a word."]

    def calculate_word_score(self):
        #Calculates the score of a word, allowing for the impact by premium squares.
        global LETTER_VALUES, premium_spots
        word_score = 0
        for i, letter in enumerate(self.word):
            for spot in premium_spots:
                if letter == spot[0] and i == spot[2]:
                    if spot[1] == "_^_":
                        word_score += LETTER_VALUES[letter] * 3
                        break
                    elif spot[1] == "_<_":
                        word_score += LETTER_VALUES[letter] * 2
                        break
                    elif spot[1] == "ZPT":
                        break
            else:
                word_score += LETTER_VALUES[letter]
        for spot in premium_spots:
            if spot[1] == "_*_":
                word_score *= 3
            elif spot[1] == "_+_":
                word_score *= 2
        self.player.increase_score(word_score)

    def calculate_other_word_score(self):
        #Calculates the score of a word, allowing for the impact by premium squares.
        global LETTER_VALUES
        word_score = 0
        for i, letter in enumerate(self.word):
            for spot in premium_spots:
                if letter == spot[0] and i == spot[2]:
                    if spot[1] == "_^_":
                        word_score += LETTER_VALUES[letter] * 3
                        break
                    elif spot[1] == "_<_":
                        word_score += LETTER_VALUES[letter] * 2
                        break
                    elif spot[1] == "ZPT":
                        break
            else:
                word_score += LETTER_VALUES[letter]
        for spot in premium_spots:
            if spot[1] == "_*_":
                word_score *= 3
            elif spot[1] == "_+_":
                word_score *= 2
        self.player.increase_score(word_score)

    def set_word(self, word):
        self.word = word.upper()

    def set_location(self, location):
        self.location = location

    def set_direction(self, direction):
        self.direction = direction

    def get_word(self):
        return self.word

def turn(player, board, bag):
    #Begins a turn, by displaying the current board, getting the information to play a turn, and creates a recursive loop to allow the next person to play.
    global round_number, players, skipped_turns
    wait_until_terminal_size_correct()

    #If the number of skipped turns is less than 6 and a row
    #Otherwise, end the game.
    if (skipped_turns < 6):

        #Displays whose turn it is, the current board, and the player's rack.
        print("\n"*(os.get_terminal_size().lines-24-len(players)))
        for plyr in players:
            print(f"{plyr.get_name()}'s score is {plyr.get_running_score()}={plyr.get_score()}")
        print("\nRound " + str(round_number) + ": " + player.get_name() + "'s turn\n")
        print(board.get_board())
        print(colored("_+_","white","on_light_magenta")+"= DWS |||"+colored("_*_","white","on_red")+"= TWS |||"+colored("_<_","white","on_light_blue")+"= DLS |||"+colored("_^_","white","on_blue")+"= TLS")
        print(f"Player tiles: {player.rack.get_rack_length()} --- Bag tiles: {bag.get_remaining_tiles()}")
        print(player.get_name() + "'s Letter Rack: " + player.get_rack_str())
        print(player.get_name() + " Letter Scores: " + player.get_rack_pts())

        #If the first word throws an error, creates a recursive loop until the information is given correctly.
        checked = ['']
        while len(checked) == 1:
            if checked[0] != '':
                print(checked[0])
            #Gets information in order to play a word.
            word_to_play = input("Word to play: ")
            if word_to_play.lower() == 'shuffle rack':
                player.shuffle_rack()
                turn(player, board, bag)
            elif 'instructions' in word_to_play.lower():
                print_instructions()
                turn(player, board, bag) 
            elif 'exchange tiles' in word_to_play.lower():
                if bag.get_remaining_tiles() >= 7:
                    tile_to_exchange = input('Which tiles do you want to exchange? ').upper()
                    for tile in tile_to_exchange:
                        for letter in player.get_rack_arr():
                            if letter.get_letter() == tile:
                                player.rack.remove_from_rack(letter)
                                bag.add_to_bag(tile, 1)
                                break
                    player.rack.replenish_rack()
                    player.add_running_score(round_score)
                    #Gets the next player.
                    if players.index(player) != (len(players)-1):
                        player = players[players.index(player)+1]
                    else:
                        player = players[0]
                        round_number += 1
                    #Recursively calls the function in order to play the next turn.
                    turn(player, board, bag)
                else:
                    print('There are not enough tiles remaining to exchange tiles.')
                    word_to_play = input("Word to play: ")
            CRD = ''
            while len(CRD)<3:
                # print("Enter CRD for the word (e.g. 7AR will start the word in col 7, row A, and build to the right)")
                CRD = input("Enter the CRD for the word: ").upper()
            try:
                col = literal_eval(f"0x{CRD[0]}")
                row = literal_eval(f"0x{CRD[1]}")
            except:
                col = ""
                row = ""
            if (col == "" or row == "") or (col not in range(15) or row not in range(15)):
                location = [-1, -1]
            else:
                location = [row, col]
            if CRD[2] == 'D':
                direction = 'down'
            elif CRD[2] == 'R':
                direction = 'right'
            else:
                direction = ''
            word = Word(word_to_play, location, player, direction, board.board_array())
            checked = word.check_word()
        word.word = checked[1]

        #If the user has confirmed that they would like to skip their turn, skip it.
        #Otherwise, plays the correct word and prints the board.
        old_score = player.get_score()
        if word.get_word() == "":
            print("Your turn has been skipped.")
            skipped_turns += 1
        else:
            blank_tile_val = checked[2]
            # need a way to check score for all words before placing the main word - calculate_other_word_score
            for one_other_word in word.other_words_intersect:
                board.prelim_place_word(one_other_word.word, one_other_word.location, one_other_word.direction, player)
                one_other_word.calculate_other_word_score()
            board.place_word(word_to_play, location, direction, player, blank_tile_val)
            word.calculate_word_score()
            skipped_turns += 0

        #Prints the current player's score
        round_score = player.get_score()-old_score
        player.add_running_score(round_score)        

        # If there are no tiles in the bag and a player has run out of tiles, end the game.
        if (player.rack.get_rack_length() == 0 and bag.get_remaining_tiles() == 0):
            end_game(board)
        else:
            #Gets the next player.
            if players.index(player) != (len(players)-1):
                player = players[players.index(player)+1]
            else:
                player = players[0]
                round_number += 1

            #Recursively calls the function in order to play the next turn.
            turn(player, board, bag)

    #If the number of skipped turns is over 6 or the bag has both run out of tiles and a player is out of tiles, end the game.
    else:
        end_game(board)

def start_game():
    wait_until_terminal_size_correct()
    #Begins the game and calls the turn function.
    global round_number, players, skipped_turns
    board = Board()
    bag = Bag()

    print_instructions()

    #Asks the player for the number of players.
    num_of_players = 0
    while num_of_players < 2 or num_of_players > 4:
        try:
            num_of_players = int(input("Please enter the number of players (2-4): "))
        except:
            num_of_players = 0

    #Welcomes players to the game and allows players to choose their name.
    print("\nWelcome to Scrabble! Please enter the names of the players below.")
    players = []
    for i in range(num_of_players):
        players.append(Player(bag))
        name = ''
        while name == '' or name.lower() in [player.get_name().lower() for player in players]:
            name = input("Please enter a unique name for player " + str(i+1) + ": ")
        players[i].set_name(name)
    #Randomly select order of players
    shuffle(players)
    #Sets the default value of global variables.
    round_number = 1
    skipped_turns = 0
    current_player = players[0]
    turn(current_player, board, bag)

def end_game(board):
    #Forces the game to end when the bag runs out of tiles.
    global players
    print("\n"*(os.get_terminal_size().lines-24-len(players)))
    for plyr in players:
        print(f"{plyr.get_name()}'s score is {plyr.get_running_score()}={plyr.get_score()}")
    print(board.get_board())
    point_bonus = 0
    for player in players:
        if player.rack.get_rack_length()>0:
            lost_points = sum([int(tile_pts) for tile_pts in player.get_rack_pts().split(', ')])
            player.increase_score(-lost_points)
            print(f"{player.get_name()} lost {lost_points} points due to end-of-game penalty.")
            point_bonus += lost_points
    for player in players:
        if player.rack.get_rack_length() == 0:
            player.increase_score(point_bonus)
            print(f"{player.get_name()} won {point_bonus} points due to end-of-game bonus.")
    highest_score = 0
    winning_player = [] 
    for player in players:
        print(f"{player.get_name()} = {player.get_score()}")
        if player.get_score() > highest_score:
            highest_score = player.get_score()
            winning_player = [player.get_name()]
        elif player.get_score() == highest_score:
            winning_player.append(player.get_name())
    print("The game is over!\n!!!!!" + " & ".join(winning_player) + ", you have won!!!!!")

    if input("\nWould you like to play again? (y/n)").upper() == "Y":
        start_game()

start_game()