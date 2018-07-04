def checkio(field):
    for row in field:
        if row[0]==row[1]==row[2] and row[0]!=".":
            if(row[0]=='X'):
                return "X"
            else:
                return "O"
    queue_1,queue_2,queue_3 = zip(*field)
    if queue_1.count("X")==3 or queue_2.count("X")==3 or queue_3.count("X")==3:
        return "X"
    elif queue_1.count("O")==3 or queue_2.count("O")==3 or queue_3.count("O")==3:
        return "O"
    if queue_1[0]==queue_2[1]==queue_3[2] and queue_1[0]!=".":
        if queue_1[0]=="X":
            return "X"
        else:
            return "O"
    if queue_1[2]==queue_2[1]==queue_3[0] and queue_1[2]!=".":
        if queue_1[2]=="X":
            return "X"
        else:
            return "O"
    return "D"


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
