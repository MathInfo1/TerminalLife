def valid(command, allowed):
    ctr = 0
    for i in allowed:
        if i in command: ctr += 1
    if ctr == 1: return True
    else: return False

def checkCommand(age, command):
    if age < 2:
        if valid(command, ["eat", "sleep", "play", "observe"]): return True
    elif age < 6:
        if valid(command, ["eat", "sleep", "play", "observe", "talk", "enroll", "attend"]): return True
    elif age < 13:
        if valid(command, ["eat", "sleep", "play", "study", "talk", "relax", "enroll", "attend", "entertain", "hobby", "wish"]): return True
    elif age < 18:
        if valid(command, ["eat", "sleep", "play", "study", "talk", "relax", "enroll", "attend", "entertain", "hobby", "work", "therapy", "wish"]): return True
    elif age < 65:
        if valid(command, ["eat", "sleep", "play", "talk", "relax", "enroll", "entertain", "hobby", "work", "therapy", "buy"]): return True
    
    # ["eat", "sleep", "play", "observe", "study", "talk", "enroll", "attend", "relax", "entertain", "hobby", "wish", "work", "therapy", "buy"]
    return False
