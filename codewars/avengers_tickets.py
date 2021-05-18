def tickets(people):
    changeBack = {
        "25": 0,
        "50": 0,
        "100": 0
    }
    
    for i in people:
        if i == 25:
            changeBack["25"] += 1
        elif i == 50:
            changeBack["50"] += 1
            changeBack["25"] -= 1
            if changeBack["25"] < 0:
                return "NO"
        else:
            if changeBack["50"] >= 1 and changeBack["25"] >= 1:
                changeBack["50"] -= 1
                changeBack["25"] -= 1
            elif changeBack["25"] >= 3:
                changeBack["25"] -= 3
            else:
                return "NO"

    return "YES"