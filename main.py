import os
from random import randint, choice
from time import sleep

monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
pI = {} # Player Info
gI = {} # Game Info
filePath = ""

def getStatus():
    return ["Poor", "Lower Class", "Middle Class", "Upper Class", "Super Rich"][pI["status"] - 1]

def nextDay():
    gI["day"] = days[(days.index(gI["day"]) + 1) % 7]
    if gI["currentDay"] < monthDays[gI["currentMonth"] - 1]:
        gI["currentDay"] += 1
    else:
        gI["currentDay"] = 1
        gI["currentMonth"] = (gI["currentMonth"] % 12) + 1

def startDay():
    majorChange = False
    if gI["currentDay"] == pI["birthDay"] and gI["currentMonth"] == pI["birthMonth"]: 
        majorChange = True
        pI["age"] += 1
    if gI["currentDay"] == 1 and gI["currentMonth"] == 1: 
        majorChange = True
        gI["year"] += 1
    if majorChange: print(f"Year {gI["year"]}, Age: {pI["age"]}")

    print(f"{gI["currentDay"]:02d}/{gI["currentMonth"]:02d} ({gI["day"]})")

def loadFile():
    global filePath
    fileType = input("Load or Create New Game (L/N): ").upper()
    while not fileType in "LN": 
        fileType = input("Load or Create New Game (L/N): ").upper()

    if fileType == "N":
        fileName = input("Enter New File Name (only char and digits, without file extension): ")
        while not fileName.isalnum() or f"{fileName}.txt" in os.listdir():
            fileName = input("Problem with Name. Enter New File Name: ")
        filePath = f"{fileName}.txt"
        saveGame(True)
    elif fileType == "L":
        fileName = input("Enter Existing File Name: ")
        while not f"{fileName}.txt" in os.listdir():
            fileName = input("File not found. Enter Existing File Name: ").upper()
        filePath = f"{fileName}.txt"
        file = open(filePath, "r")
        pI["name"], pI["gender"], pI["birthDay"], pI["birthMonth"] = [int(x) if x.isdigit() else x for x in file.readline().strip().split(" ")]
        pI["age"], pI["status"], pI["health"], pI["balance"], pI["hunger"] = [int(x) if x.isdigit() else x for x in file.readline().strip().split(" ")]
        pI["problems"] = file.readline().strip().split("; ")
        gI["currentDay"], gI["currentMonth"], gI["year"], gI["day"] = [int(x) if x.isdigit() else x for x in file.readline().strip().split(" ")]
        
    return filePath

def saveGame(firstTime = False):
    if firstTime: 
        print("New game will be created only after the following intro and saved every game day. ")
        pI["gender"] = choice(["Male", "Female"])
        pI["name"] = input(f"Enter Player Name (Gender: {pI["gender"]}): ") or "MathInfo"
        pI["birthMonth"] = randint(1, 12)
        pI["birthDay"] = randint(1, monthDays[pI["birthMonth"] - 1])
        gI["currentDay"] = pI["birthDay"]
        gI["currentMonth"] = pI["birthMonth"]
        pI["age"] = 0
        gI["year"] = 0 if pI["birthDay"] + pI["birthMonth"] == 2 else 1
        pI["status"] = randint(1, 5) # 1: Poor, 5: Super Rich
        pI["health"] = randint(80, 100)
        pI["problems"] = []
        pI["balance"] = 100 ** pI["status"]
        pI["hunger"] = 50
        # gI["date"] = (pI["birthDay"], pI["birthMonth"])
        gI["day"] = choice(days)
        print(f"\nHello {pI["name"]}, You are a {"boy" if pI["gender"] == "Male" else "girl"} born on {gI["day"]} {pI["birthDay"]:02d}/{pI["birthMonth"]:02d} (dd/mm)! ")
        print(f"Your family's current status is {getStatus()}. ")
        file = open(filePath, "x")
    else: 
        file = open(filePath, "w")
    file.write(f"{pI["name"]} {pI["gender"]} {pI["birthDay"]} {pI["birthMonth"]}\n")
    file.write(f"{pI["age"]} {pI["status"]} {pI["health"]} {pI["balance"]} {pI["hunger"]}\n")
    file.write(f"{"; ".join(pI["problems"])}\n")
    file.write(f"{gI["currentDay"]} {gI["currentMonth"]} {gI["year"]} {gI["day"]}")
    print("Game saved")
    file.close()

print(loadFile())
saveGame()
while True:
    startDay()
    hour = 0
    timeSlept = 0
    pI["hunger"] -= 15
    while hour < 24:
        command = input(f"Hour {hour}: ").lower()
        if command == "sleep":
            timeSlept += 0.5
        elif command.startswith("eat"):
            if "menu" in command:
                print("Menu 1: Fast-Food, $2, 7")
                print("Menu 2: Fast-Food, $5, 10")
                print("Menu 1: Home-meal, $4, 10")
                print("Menu 1: Home-meal, $10, 15")
                print("Menu 1: Restaurant, $15, 10")
                print("Menu 1: Restaurant, $25, 15")
        hour += 0.5
    
    saveGame()
    nextDay()
