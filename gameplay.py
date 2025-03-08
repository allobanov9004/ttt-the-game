from random import randrange

def player_turn(field: list, crosses: list):
    turn = int(input("enter number: "))
    if turn in field:
        crosses.append(field.pop(field.index(turn)))



def pc_turn(field: list, circles: list):
    circles.append(field.pop(randrange(len(field))-1))



def win_condition(ttt: list) -> bool: 
    if ttt.count(1)+ttt.count(2)+ttt.count(3) == 3 or ttt.count(4)+ttt.count(5)+ttt.count(6) == 3 or ttt.count(7)+ttt.count(8)+ttt.count(9) == 3:
        return True
    elif ttt.count(1)+ttt.count(4)+ttt.count(7) == 3 or ttt.count(2)+ttt.count(5)+ttt.count(8) == 3 or ttt.count(3)+ttt.count(6)+ttt.count(9) == 3:
        return True
    elif ttt.count(1)+ttt.count(5)+ttt.count(9) == 3 or ttt.count(3)+ttt.count(5)+ttt.count(7) == 3:
        return True
    else:
        return False