def checkboard(board):
    winner = True
    exit = False

    for row in board:
        for item in row:
            if (item != 'x'):
                winner = False
        if (winner == True):
            exit = True
            break
        else:
            winner = True
    
    if (exit == True):
        return True
    
    winner = True
    for col in range(5):
        for row in board:
            if (row[col] != "x"):
                winner = False
        if (winner == True):
            exit = True
            break
        else:
            winner = True
    
    if (exit == True):
        return True
    else:
        return False

board1 = [['78','27','82','68','20'],['14','2','34','51','7'],['58','57','99','37','81'],['9','4','0','76','45'],['67','x','70','17','23']]
board2 = [['78','27','82','68','20'],['14','2','34','51','7'],['58','57','99','37','81'],['9','4','0','76','45'],['x','x','x','x','x']]
board3 = [['78','x','82','68','20'],['14','x','34','51','7'],['58','x','99','37','81'],['9','x','0','76','45'],['67','x','70','17','23']]

print(checkboard(board1))
print(checkboard(board2))
print(checkboard(board3))