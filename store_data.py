from random import randint, choice
from fixed_data import *
import os

def loadFile():
    filePath, pI, gI = "", dict(), dict()

    fileType = input("Load or Create New Game (L/N): ").upper()
    while not fileType in "LN": 
        fileType = input("Load or Create New Game (L/N): ").upper()

    if fileType == "N":
        fileName = input("Enter New File Name (only char and digits, without file extension): ")
        while not fileName.isalnum() or f"{fileName}.txt" in os.listdir():
            fileName = input("Problem with Name. Enter New File Name: ")
        filePath = f"{fileName}.txt"
        pI, gI = saveGame(filePath, firstTime = True)
    elif fileType == "L":
        fileName = input("Enter Existing File Name: ")
        while not f"{fileName}.txt" in os.listdir():
            fileName = input("File not found. Enter Existing File Name: ").upper()
        filePath = f"{fileName}.txt"
        file = open(filePath, "r")
        pI["name"], pI["gender"], pI["birthDay"], pI["birthMonth"] = [int(x) if x.isdigit() else x for x in file.readline().strip().split(" ")]
        pI["age"], pI["status"], pI["health"], pI["balance"], pI["hunger"], pI["happiness"] = [int(x) if x.isdigit() else x for x in file.readline().strip().split(" ")]
        pI["problems"] = file.readline().strip().split("; ")
        gI["currentDay"], gI["currentMonth"], gI["year"], gI["day"] = [int(x) if x.isdigit() else x for x in file.readline().strip().split(" ")]
        pI["school"] = [int(x) for x in file.readline().split(" ")]
        pI["job"] = [int(x) if x.isdigit() else x for x in file.readline().strip().split("; ")]
    return filePath, pI, gI

def saveGame(filePath, pI = dict(), gI = dict(), firstTime = False):
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
        pI["balance"] = 10 ** pI["status"]
        pI["hunger"] = 50
        pI["happiness"] = 80
        gI["day"] = choice(days)
        pI["school"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # STEM, lang, social, sport/arts/music, exam No., diploma, 4 field scores
        pI["job"] = [100, False, 0, 0, 0, 0, 0] # Job, HS diploma, Pay, 4 field experience
        print(f"\nHello {pI["name"]}, You are a {"boy" if pI["gender"] == "Male" else "girl"} born on {gI["day"]} {pI["birthDay"]:02d}/{pI["birthMonth"]:02d} (dd/mm)! ")
        print(f"Your family's current status is {getStatus(pI["status"])}. ")
        file = open(filePath, "x")
    else: 
        file = open(filePath, "w")
    file.write(f"{pI["name"]} {pI["gender"]} {pI["birthDay"]} {pI["birthMonth"]}\n")
    file.write(f"{pI["age"]} {pI["status"]} {pI["health"]} {pI["balance"]} {pI["hunger"]} {pI["happiness"]}\n")
    file.write(f"{"; ".join(pI["problems"])}\n")
    file.write(f"{gI["currentDay"]} {gI["currentMonth"]} {gI["year"]} {gI["day"]}\n")
    file.write(f"{" ".join([str(x) for x in pI["school"]])}\n")
    file.write(f"{"; ".join([str(x) for x in pI["job"]])}")

    print("Game saved")
    file.close()
    return pI, gI
