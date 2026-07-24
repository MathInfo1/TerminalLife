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

jobOptions = {
    1: ["Junior Engineer", False, 8, 0, 0],
    2: ["Junior Engineer", True, 11, 0, 0],
    3: ["Senior Engineer", True, 16, 0, 6400],
    4: ["Junior Language Job", False, 8, 1, 0],
    5: ["Junior Language Job", True, 10, 1, 0],
    6: ["Senior Language Job", True, 15, 1, 3200],
    7: ["Social Worker", False, 8, 2, 0],
    8: ["Junior Therapist", True, 10, 2, 0],
    9: ["Senior Therapist", True, 15, 2, 3200],
    10: ["Athlete", False, 13, 3, 0],
    11: ["Artist", False, 13, 3, 0],
    12: ["Musician", True, 15, 3, 0],
    13: ["Experienced Athlete", False, 14, 3, 6400],
    14: ["Experienced Artist", False, 14, 3, 6400],
    15: ["Experienced Musician", True, 16, 3, 6400]
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

def printJobOptions():
    print("Job No. | Job name | High school diploma required? | pay per hour | field no. | hours experience required")
    for jobName, jobDetails in jobOptions.items():
        editedDetails = jobDetails.copy()
        editedDetails[2] *= 2
        editedDetails[4] //= 2
        print(f"{jobName}: {"; ".join([str(x) for x in editedDetails])}")
