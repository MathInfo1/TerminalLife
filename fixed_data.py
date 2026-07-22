monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
foodMenu = {
    1: [2, 5, 5], 
    2: [5, 10, 5],
    3: [4, 10, 10], 
    4: [10, 15, 15],
    5: [15, 10, 20], 
    6: [25, 15, 25]
}

def sleepLimit(age):
    if age < 1: return 12, 9
    if age < 3: return 10, 8.5
    if age < 6: return 9, 7.5
    if age < 13: return 7.5, 5
    return 7, 4

def getStatus(index):
    return ["Poor", "Lower Class", "Middle Class", "Upper Class", "Super Rich"][index - 1]

def printMenu():
    print("Menu number | Name | Price | Hunger Points | Happiness Points")
    print("Menu 1: Fast-Food, $2, 5, 5")
    print("Menu 2: Fast-Food, $5, 10, 5")
    print("Menu 3: Home-meal, $4, 10, 10")
    print("Menu 4: Home-meal, $10, 15, 15")
    print("Menu 5: Restaurant, $15, 10, 20")
    print("Menu 6: Restaurant, $25, 15, 25")
