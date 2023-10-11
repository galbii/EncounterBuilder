import builder as dnd

#also difficulty = 1, 2, 3, 4 = easy, med, hard, deadly
#create an encounter
enc = dnd.Encounter(4)

#create PlayerManager object
#important note: use player manager funcitons first to add list
pm = dnd.PlayerManager("Medium")

#add_player function takes the level of the player as a parameter since we wont need to 
pm.add_player(20)
pm.add_player(20)
pm.add_player(3)

print(pm.calc_thresh())


