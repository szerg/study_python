
def receive_input(m):
    """primeste coord de la tastatura si le valideaza; trb sa compare cu pozitiile libere de pe boardul dat de matricea m"""
    
    while True:
        coord = input("Enter the coordinates: ")
        coord_list = coord.split()
        try:
            row = int(coord_list[0])
            col = int(coord_list[1])
        except (IndexError,ValueError) as e:
            print("You should enter numbers!")
            continue
        if row not in [1,2,3] or col not in [1,2,3]:
            print("Coordinates should be from 1 to 3!")
            continue
        if m[2-(col-1)][row-1]!=' ':
            print("This cell is occupied! Choose another one!")
            continue
        #returneaza coordonatele, asa cum le vede matricea
        return 2-(col-1),row-1

def print_matrix(m):
    """Printeaza matricea m intr-un anume format; stim ca va fi 3x3"""
    print('---------')
    step=3
    for i in range(3):
        print("|",end=" ")
        for j in range(3):  
            print(m[i][j],end=" ")
        print("|")
    print('---------')

def create_matrix(inp):
    """Face o matrice dintr-un input 3*3 de strings"""
    m=[]
    for i in range(3):
        m.append([])
        for j in range(3):
            m[i].append(inp[i*3+j])
    return m

def board_valid(inp):
    """vede daca boardul este valid, daca nr de x difera de  nr de  0 doar cu 1; inp e un  sir de chars"""
    nr_x=nr_y=0
    for i in inp:
        if i=='X':
            nr_x+=1
        if i=='O':
            nr_y+=1
    return abs(nr_x-nr_y)<=1


def three_of_a_kind(m):
    """Calculeaza daca exista 3 la rand de X sau O; gen daca ai 3 de X sau  de O si printeaza cine castiga"""
    got_three = False

    X_win=False
    O_win=False
    X_win_condition=['X','X','X']
    O_win_condition=['O','O','O']
    # rows
    for a in range(3):
        if m[a][:] == X_win_condition:
            X_win=True
        elif m[a][:] == O_win_condition:
            O_win = True
    # columns
    for a in range(3):
        col = []
        for b in range(3):
            col.append(m[b][a])
        if col == X_win_condition:
            X_win=True
        elif col == O_win_condition:
            O_win = True
    
    # fwd diag
    diag=[]
    for a in range(3):
        diag.append(m[a][a])
    if diag == X_win_condition:
        X_win=True
    elif diag == O_win_condition:
        O_win = True 
    
    # rev  diag
    rdiag=[]
    for a in range(3):
        rdiag.append(m[2-a][a])
    if rdiag == X_win_condition:
        X_win=True
    elif rdiag == O_win_condition:
        O_win = True 
    
    if X_win and O_win:
        print('Impossible')
        got_three = False
    elif X_win:
        print('X wins')
        got_three = True
    elif O_win:
        print('O wins')
        got_three = True
    elif ' ' in m[0] or ' ' in m[1] or ' ' in m[2]:
        #print('Game not finished')
        got_three = False
    else:
        print('Draw')
        got_three = True
    return got_three
    
    
# init empty matrix:
m=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
# both pplayers
players = ['X','O']
# start with X
to_move = 0


# actual game
print_matrix(m)
while not three_of_a_kind(m):
    # receive input
    row,col = receive_input(m)
    # change board
    m[row][col] = players[to_move]
    # show  board
    print_matrix(m)
    # swap players
    to_move = (to_move+1)%2
