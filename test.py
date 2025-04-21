import pandas as pd 
import random 
import json 
players_position = {f"{i}":0 for i in range(1,4)}
gridsize = input("Enter Grid Size: ")
gridsize = int(gridsize)
winner = None
game_logs = []
all_player_first_time = True
def exisitingPlayerOnPosition(players_position, newPlayerPosition):
    for player in players_position:
        if players_position[player] == newPlayerPosition:
            players_position[player] = 0
        
    return players_position

def getCordinatesFromPostion(position, gridSize):
    row = (position-1)//gridSize
    col = (position-1)%gridSize

    if(row %2 == 1):
        col = gridSize-1-col
    return (col,row)

while not winner:
    for player in players_position:
        dice_roll_number = random.randint(1,6)
        
        newPlayerPosition = players_position[player]+dice_roll_number
        players_position = exisitingPlayerOnPosition(players_position,newPlayerPosition)
        if newPlayerPosition > gridsize*gridsize:
            newPlayerPosition =players_position[player]
        newPlayerPositionHistoryString = newPlayerPosition
        if (players_position[player] == 0 and all_player_first_time == False):
            newPlayerPositionHistoryString = "(0,"+str(newPlayerPosition)+")"
        players_position[player] = newPlayerPosition
        game_logs.append({
            "player":player,
            "diceRoll":dice_roll_number,
            "cords":getCordinatesFromPostion(newPlayerPosition,gridsize),
            "history":newPlayerPositionHistoryString,
            "status":newPlayerPosition == gridsize*gridsize
        })
        if newPlayerPosition == gridsize*gridsize:
            winner = player
            break
    all_player_first_time= False

output = [
    {
        "Player No." : "1",
        "Dice Roll":[],
        "Player Position":[],
        "Cordinates History":[],
        "Winner Status":False
    },
    {
        "Player No." : "2",
        "Dice Roll":[],
        "Player Position":[],
        "Cordinates History":[],
        "Winner Status":False
    },
    {
        "Player No." : "3",
        "Dice Roll":[],
        "Player Position":[],
        "Cordinates History":[],
        "Winner Status":False
    }
    
]
for logs in game_logs:
    for player in output:
        if(player["Player No."] == logs["player"]):
            player["Dice Roll"].append(logs["diceRoll"])
            player["Player Position"].append(logs["history"])
            player["Cordinates History"].append(logs["cords"])
            winnerStatus = ""
            if(logs["status"] == True):
                winnerStatus = True
            player["Winner Status"] = winnerStatus
    
# with open(r"C:\Users\BUNNY009\Desktop\test\output.json","w") as f:
#     json.dump(output,f)

print(pd.DataFrame(output))
