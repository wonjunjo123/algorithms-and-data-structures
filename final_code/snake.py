def createBoard():
    board = {}
    for x in range(1,101):
        x_moves = list(range(x, x+7))
        x_moves = [y if y <= 100 else x for y in x_moves]
        board[x] = x_moves
    return board

def add_snakes(board):
    '''
    By inspection, the snakes are at 98->78, 95->75, 92->73, 87->24, 62->19, 64->60, 56->53, 47->26, 49->11, 16->6\
    Add these snakes by changing the board!
    '''
    snakeStart = [98,95,92,87,62,64,56,47,49,16]
    snakeEnd = [78,75,73,24,19,60,53,26,11,6]
    snakes = dict(zip(snakeStart, snakeEnd))

    for square in board:
        for item in board[square]:
            if item in snakes:
                i = board[square].index(item)
                board[square][i] = snakes[item]
    return board
    
def add_ladders(board):
    '''
b    By inspection, the ladders are at 1->38, 4->14, 9->31, 28->84, 36->44, 21->42, 51->67, 71->91, 80->100
    Add these ladders by changing the board!
    (Ignore the 1->38 ladder!)
    '''
    ladderStart = [4,9,28,36,21,51,71,80]
    ladderEnd = [14,31,84,44,42,67,91,100]
    ladders = dict(zip(ladderStart, ladderEnd))

    for square in board:
        for item in board[square]:
            if item in ladders:
                i = board[square].index(item)
                board[square][i] = ladders[item]
    return board

    
def fastestWin(board, goal = 100):
    '''
    This method should compute and display the minimum number of turns it takes to win the standard game.
    Then it should display the moves for each turn.
    '''
    # use BFS SSSP algorithm

    start = 1
    # Set up
    dist = dict()
    pred = dict()
    for n in board:
        if n == 1:
            dist[n] = 0
        else:
            dist[n] = 99999999 # imitate infinity
        pred[n] = None

    queue = list()
    queue.append(start)
    while len(queue) > 0:
        x = queue.pop(0)
        for toVertex in board[x]: # board[x] returns the adjacency list at square number x
            if dist[toVertex] > dist[x] + 1:
                dist[toVertex] = dist[x] + 1
                pred[toVertex] = x
                queue.append(toVertex)

    # now that we have the table updated
    directions = list()
    thing = goal
    while True:
        directions.insert(0, thing)
        if thing == 1:
            break
        thing = pred[thing]
        
    
    
    
    print("Turns for fastest win:", "Infinite")
    
    print("Moves for fastest win:")
    moves = directions
    for i in range(len(moves)-1):
        move_string = str(moves[i]) + "->" + str(moves[i+1])
        print("Turn",i+1,move_string)
    


def fastestModifiedWin(board):
    '''
    This method should compute and display the minimum number of turns it takes to win the modified game.
    Then it should display the moves for each turn.
    '''
    #Implement
    print("Turns for fastest win:", "Infinite")
    
    print("Moves for fastest win:")
    moves = [1, 7, 20, 34, 100]
    for i in range(len(moves)-1):
        move_string = str(moves[i]) + "->" + str(moves[i+1])
        print("Turn",i+1,move_string)
    
def main():
    board = createBoard()

    add_snakes(board)
    add_ladders(board)
    
    #comment these out once you fix the board
    print(board[1][2]) #Where do you end up if you roll a 2 while on spot 1?
    print(board[1][3]) #Where do you end up if you roll a 3 while on spot 1?
    print(board[97][1]) #Where do you end up if you roll a 1 while on spot 97?
    fastestWin(board)
#   fastestModifiedWin(board)

if __name__ == "__main__":
    main()
