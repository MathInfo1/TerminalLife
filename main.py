from fixed_data import *
from random import randint, choice, random
from time import sleep
from store_data import loadFile, saveGame
from control_commands import checkCommand

filePath, pI, gI = loadFile()

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
        if gI["year"] > 1: pI["age"] += 1
    if gI["currentDay"] == 1 and gI["currentMonth"] == 1: 
        majorChange = True
        gI["year"] += 1
    if majorChange: print(f"Year {gI["year"]}, Age: {pI["age"]}")
    print(f"{gI["currentDay"]:02d}/{gI["currentMonth"]:02d} ({gI["day"]})")

def printProfile():
    print(f"{pI["name"]}, {pI["gender"]}, {pI["age"]} years old")
    print(f"Birthday: {pI["birthDay"]}/{pI["birthMonth"]}")
    print(f"(Family) Status: {pI["status"]}, Current Balance: {pI["balance"]}")
    print(f"{"Currently no health problems! " if pI["problems"] == [""] else pI["problems"]}")
    print(f"Hunger: {pI["hunger"]}, Happiness: {pI["happiness"]}")
    print()

def askCommand():
    global command, timeSlept, hour
    command = input(f"Hour {hour}: ").lower()
    while not checkCommand(pI["age"], command) and not "profile" in command: 
        command = input(f"Hour {hour}: ").lower()
    if "profile" in command: 
        if command.removeprefix("profile").strip():
            try: print(pI[command.removeprefix("profil").strip()])
            except KeyError: printProfile()
        else: printProfile()
        askCommand()
    if command == "sleep": timeSlept += 0.5
    elif command.startswith("eat"): eat()
    elif command in ["observe", "relax", "talk", "entertain", "play"]: 
        if random() < 0.5: pI["happiness"] = min(100, pI["happiness"] + randint(1, 3))
    elif command.startswith("study"):
        field = command.removeprefix("study").strip()
        while not (field.isnumeric() and int(field) >= 0 and int(field) <= 4):
            field = input("Which field (0: STEM, 1: Lang, 2: Social, 3: Sports/Art/Music)")
        pI["school"][int(field)] += 1
    elif command.startswith("attend"):
        activity = command.removeprefix("attend").strip()
        while not activity in ["school", "exam"]:
            activity = input("What do you want to attend (school / exam): ").lower()
        if activity == "school":
            field = randint(0, 3)
            if random() > 0.25: 
                print(f"You just had class in {["STEM", "Language", "Social", "Sports/Art/Music"][field]} and you paid attention. ")
                pI["school"][field] += 1
            else:
                print(f"You didn't pay attention in {["STEM", "Language", "Social", "Sports/Art/Music"][field]} now...")
        if activity == "exam":
            if pI["school"][4] >= min(192, (pI["age"] - 5) * 16):
                print("You reached the limit of tests you can take. Wait till your next birthday :)")
                askCommand()
                return
            if hour >= 8 and hour <= 14 and gI["day"] in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
                field = pI["school"][4] % 4
                hour += 1
                if pI["school"][field] >= 30:
                    pI["school"][field] -= 30
                    print(f"You passed the exam with the grade: A!")
                    if pI["school"][4] >= 8 * 16: pI["school"][5] += 4
                elif pI["school"][field] >= 22:
                    pI["school"][field] -= 22
                    print(f"You passed the exam with the grade: B!")
                    if pI["school"][4] >= 8 * 16: pI["school"][5] += 3
                elif pI["school"][field] >= 15:
                    pI["school"][field] -= 15
                    print(f"You passed the exam with the grade: C")
                    if pI["school"][4] >= 8 * 16: pI["school"][5] += 2
                elif pI["school"][field] >= 9:
                    pI["school"][field] -= 9
                    print(f"You passed the exam with the grade: D")
                    if pI["school"][4] >= 8 * 16: pI["school"][5] += 1
                else:
                    pI["school"][field] = pI["school"][field] // 3
                    print(f"You failed the exam since you didn't learn enough. ")
                pI["school"][4] += 1
                if pI["school"][4] == 12 * 16: 
                    if pI["school"][5] > 64: print(f"Congratulations, you got your high school diploma with {pI["school"][5]}/256 points! ")
                    else: print(f"You failed too many exams and couldn't get your high school diploma with {pI["school"][5]}/256 points. ")
            else: 
                print("Exams can be started on weekdays between 9am and 2pm. They take 1.5h each. ")
                askCommand()
                return
    elif command == "enroll":
        pass
    elif command == "hobby":
        pass
    elif command == "wish":
        pass
    elif command == "work":
        pass
    elif command == "therapy":
        pass
    elif command == "buy":
        pass


    # TODO: ["enroll", "attend", "hobby", "wish", "work", "therapy", "buy"]

def eat():
    if command == "eat menu":
        printMenu()
    food = command.removeprefix("eat").strip()
    if pI["balance"] < foodMenu[1][0]:
        print(f"Sorry, you have only ${pI["balance"]} and can't buy any food. Enter a different command. ")
        askCommand()
        return
    while not food.isnumeric() or int(food) < 1 or int(food) > 6 or pI["balance"] < foodMenu[int(food)][0]:
        food = input("Which menu would you like to eat (1-6): ")
    pI["hunger"] = min(100, pI["hunger"] + foodMenu[int(food)][1])
    pI["happiness"] = min(100, pI["happiness"] + foodMenu[int(food)][2])
    pI["balance"] -= foodMenu[int(food)][0]
printProfile()
while True:
    startDay()
    hour = 7 # Normal value: 0
    timeSlept = 0
    pI["hunger"] -= 5 # Normal value: 20
    if pI["age"] < 18: pI["balance"] += pI["status"] * 6
    sleepLimit1, sleepLimit2 = sleepLimit(pI["age"])
    while hour < 11: # Normal value: 24
        askCommand()
        hour += 0.5

    if timeSlept < sleepLimit2: 
        pI["health"] -= randint(1, randint(3, 5))
        pI["happiness"] -= randint(1, 5)
        if random() < 0.02: pI["problems"].append("sleep deprived")
    elif timeSlept < sleepLimit1:
        pI["health"] -= randint(0, randint(1, 3))
        pI["happiness"] -= randint(1, randint(2, 5))

    nextDay()
    saveGame(filePath, pI, gI)
