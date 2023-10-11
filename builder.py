import csv
import random
import pandas as pd

class Monster:

    def __init__(self, name, level = 1):
        self.mName = name
        self.mLevel = level
        self.armor = {}

#player difficulty based on exp values given by Wizard's of the Coast in their Dungeon Master Guide Book

#made a player class so that we can compute player difficulty
class Player:
    def __init__(self, level = 1):
        self.level = level

#manages players will need to call on this class first so we can parse the player list to the encounter manager
class PlayerManager:
    def __init__(self, difficulty = "Easy"):
        self.players = []
        self.player_count = 0
        self.xpthresh = pd.read_csv('xpthreshhold.csv', index_col = 0)
        self.thresholds = []
        self.diff = difficulty

    def add_player(self, level = 1):
        player_name = f"player{self.player_count}"
        self.players.append(Player(level)) 
        self.player_count += 1

    def get_list(self):
        return self.players

    def calc_thresh(self):
        if self.players:
            for player in self.players:
                self.thresholds.append(self.xpthresh.loc[self.xpthresh.index == player.level][self.diff].values[0])
            return self.thresholds
        else:
            print("[error] player List is empty. please add players")
            return None


class Encounter:

    def __init__(self, difficulty = 1):
        self.monster =  []
        self.names = []
        self.exp = []
        self.difficulty = difficulty
        #TODO: import info from csv into object Encounter 
        #import info from dd5e_monsters.csv from https://www.kaggle.com/datasets/patrickgomes/dungeons-and-dragons-5e-monsters/data
         #monsters only from monster manual
        df =pd.read_csv('Dd5e_monsters.csv')
        name = df['Name']
        size = df['Size']
        df[['Race', 'Alignment']] = df['Race + alignment'].str.split(",",n=1,expand=True)
        race = df['Race']
        alignment = df['Alignment']
        #Could drop the original column with:
        #df.drop('Race + alignment', axis=1, inplace=True)
        #cleaning unused columns
        df.drop(['HP','Armor','Speed'], axis=1, inplace=True)

    
    #TODO: Calculate Difficulties
    #TODO: Make a random generator that generates a encounter that is practical and meets the rerquirement
    #TODO: Make the monsters already chosen have a higher weight of being chosen
    #TODO: Calculate Modifier based on party size



