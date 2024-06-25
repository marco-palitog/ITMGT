def relationship_status(from_member, to_member, social_graph):

    follower = False
    followed = False
    
    from_member_following = social_graph.get(from_member).get("following")
    to_member_following = social_graph.get(to_member).get("following")
    if to_member in from_member_following:
        follower = True
    if from_member in to_member_following:
        followed = True

    if follower and followed:
        return("friends")
    elif follower:
        return("follower")
    elif followed:
        return("followed by")
    else:
        return("no relationship")
                                           
def tic_tac_toe(board):
    #row checker
    for row in range(len(board)):
        X_count = 0
        O_count = 0
        for col in range(len(board)):
            if board[row][col] == "X":
                X_count += 1
            elif board[row][col] == "O":
                O_count += 1
        if X_count == len(board):
            return("X")
        elif O_count == len(board):
            return("O")

    #column checker
    for col in range(len(board)):
        X_count = 0
        O_count = 0
        for row in range(len(board)):
            if board[row][col] == "X":
                X_count += 1
            elif board[row][col] == "O":
                O_count += 1
        if X_count == len(board):
            return("X")
        elif O_count == len(board):
            return("O")

    #diagonal checker 1
    X_count = 0
    O_count = 0
    for row in range(len(board)):
        if board[row][row] == "X":
            X_count += 1
        elif board[row][row] == "O":
            O_count += 1
    if X_count == len(board):
        return("X")
    elif O_count == len(board):
        return("O")

    #diagonal checker 2
    X_count = 0
    O_count = 0
    for row in range(len(board)):
        if board[row][len(board)-1-row] == "X":
            X_count += 1
        elif board[row][len(board)-1-row] == "O":
            O_count += 1
    if X_count == len(board):
        return("X")
    elif O_count == len(board):
        return("O")

    return("NO WINNER")

def eta(first_stop, second_stop, route_map):
    eta = 0
    leg = 0
    #locate origin stop
    for stops in range(len(route_map)):
        if first_stop == list(route_map.keys())[stops][0]:
            leg = stops
            
    #enforce circular motion of travel
    while True:
        eta += list(route_map.values())[leg].get("travel_time_mins")
        if second_stop == list(route_map.keys())[leg][1]:
            return(eta)
        if leg >= (len(route_map) - 1):
            leg = 0
        else:
            leg += 1
    