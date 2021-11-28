#Code created by Aditya Patel
game_board=['-','-','-','-','-','-','-','-','-','-']#initialise a empty board globally so it can be accessible in all functions
available_choices=[1,2,3,4,5,6,7,8,9]# denotes the positions of the boxes which are still empty


#===================================================================================

def display():#displaying the tic tac toe game board
    print ('{} | {} | {}' .format(game_board[1],game_board[2],game_board[3]) )
    print('__|___|___')
    print( '{} | {} | {}' .format(game_board[4],game_board[5],game_board[6]) )
    print('__|___|___')
    print( '{} | {} | {}' .format(game_board[7],game_board[8],game_board[9]) )
    
#==================================================================================

def displayrules():#diplaying general information
    print('TIC TAC TOE on a 3x3 board')
    print('Board looks like:')#general layout of the board indicating indices of each box
    print('1 | 2 | 3 ')
    print('__|___|___')
    print('4 | 5 | 6 ')
    print('__|___|___')
    print('7 | 8 | 9 ')
    print('First input from user (X) and second input from computer(O) and so on...')
#================================================================================

def checkrows(board):#check if any of the rows is complete and the game is over
    #returning -1 indicates X won and returning 1 indicates O won
    if ( board[1]==board[2] and board[2]==board[3] and board[1]!='-' ):
        if(board[1]=='X'):
            return -1
        elif(board[1]=='O'):
            return 1

    if ( board[4]==board[5] and board[5]==board[6] and board[4]!='-' ):
        if(board[4]=='X'):
            return -1
        elif(board[4]=='O'):
            return 1
    if ( board[7]==board[8] and board[8]==board[9] and board[7]!='-' ):
        if(board[7]=='X'):
            return -1
        elif(board[7]=='O'):
            return 1
    return 0

#=======================================================================================
def checkcolumns(board):#check if any of the colomns is complete and the game is over
    #returning -1 indicates X won and returning 1 indicates O won
    if ( board[1]==board[4] and board[4]==board[7] and board[1]!='-' ):
        if(board[1]=='X'):
            return -1
        elif(board[1]=='O'):
            return 1
    if ( board[2]==board[5] and board[5]==board[8] and board[2]!='-' ):
        if(board[2]=='X'):
            return -1
        elif(board[2]=='O'):
            return 1
    if ( board[3]==board[6] and board[6]==board[9] and board[3]!='-' ):
        if(board[3]=='X'):
            return -1
        elif(board[3]=='O'):
            return 1
    return 0
#===================================================================================
def checkdiagonals(board):#check if any of the diagonal is complete and the game is over
    #returning -1 indicates X won and returning 1 indicates O won
    if(board[1]==board[5] and board[5]==board[9] and board[1]!='-' ):
        if(board[1]=='X'):
            return -1
        elif(board[1]=='O'):
            return 1
    if(board[3]==board[5] and board[5]==board[7] and board[3]!='-' ):
        if(board[3]=='X'):
            return -1
        elif(board[3]=='O'):
            return 1
    return 0
#=====================================================================================
def GameOver(board):# check if the game is over or it still needs to go on
    #returning -1 indicates X won and returning 1 indicates O won
    if (checkcolumns(board)==1 or checkrows(board)==1 or checkdiagonals(board)==1):
        return 1
    elif(checkcolumns(board)==-1 or checkrows(board)==-1 or checkdiagonals(board)==-1):
        return -1
#=====================================================================================
def draw(curr_board):#Checks for draw
    n=0
    for i in range(1,10):
        if curr_board[i]!='-':
            n=n+1
    if n==9:
        return True
    else:
        return False
#=====================================================================================

def minimax(curr_board,depth,isMaximising):
    wincheck=GameOver(curr_board) #check if player or computer has already won

    if(isMaximising):#maximising right now
        bScore=-1111111
        if(wincheck==1):
            return 1
        elif(wincheck==-1):         
            return -1
        elif draw(curr_board):
            # print("executes")
            return 0
        else:
            for i in range(1,10):
                if(curr_board[i]=='-'):
                    #make temporary move
                    curr_board[i]='O'
                    #score of the temporary move
                    temp_score=minimax(curr_board,depth+1,False)
                    #finding best score
                    bScore=max(temp_score,bScore)
                    #removing the  temporary move
                    curr_board[i]='-'
            return bScore#returns the best score
    else:#minimising rightnow
        #check if player or computer has already won
        if(wincheck==1):
            return 1
        elif(wincheck==-1):         
            return -1
        elif(len(available_choices)==0):
            # print("executes")
            return 0
        else:
            bScore=1111111

            for i in range(1,10):
                if(curr_board[i]=='-'):
                    #make a temporary move
                    curr_board[i]='X'
                    ##score of the temporary move
                    temp_score=minimax(curr_board,depth+1, True)
                    #finding best score 
                    bScore=min(temp_score,bScore)
                    #remove the temporary move
                    curr_board[i]='-'
            return bScore
#====================================================================================
def find_best_move(curr_board):#finds best move for computer using minimax algorithm
    best=-111111#randomnly initialising
    bestmove=-1

    for i in range(1,10):
        if(curr_board[i]=='-'):
            curr_board[i]='O'
            val=minimax(curr_board,0,False)
            #print(val)
            curr_board[i]='-'
            if val > best:
                bestmove=i#storing best move
                # print(val)
                best=val
    print("the computer chose {} index".format(bestmove))
    game_board[bestmove]='O'#assigning 'O' to what computer chose
    available_choices.remove(bestmove)# removing that box from availablle boxes

#========================================================================================
#-----------------
displayrules()
while True:
    #run infinite loop until the game gets over
    print('Available choice are {}'.format(available_choices))
    user=input("Enter a valid choice from available choices: ")#taking a valid input from the user
    while (available_choices.count(int(user)) ==0):
        #we entered an invalid choice
        #prompt user to give input again until he gives a valid input
        print('You entered a wrong input')
        user=input("Please enter a valid choice from available choices:")

    game_board[int(user)]='X'#updating the board after a valid input is entered
    available_choices.remove(int(user))#updating available choices
    display()#display the board
    if(GameOver(game_board)):#check if game is over
        print('Game Over!')
        print('Congratulations you won!')
        break
    if not available_choices:#check for draw
        print('It is a draw')
        break
    #check win
    print("Now computer's move")
    find_best_move(game_board)
    display()#display the board
    
    if(GameOver(game_board)):#same procedure repeated again
        print('Game Over!')
        print('Computer won!')
        print('Better luck next time')
        break
    if not available_choices:
        print('It is a draw')
        break
