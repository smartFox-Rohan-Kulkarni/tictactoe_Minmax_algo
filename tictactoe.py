#Hi! I am a avid programmer named Rohan Kulkarni. 
#HOpe this Helps!!

#frame structure and board
#backtarck states
#states have parent,board ,utility, player,depth
#methods build game,check_gameover,

board=[["","",""],
       ["","","",],
       ["","",""]
       ]
ai="O"
me="X"
status={
        "Lost":0,
        "Won":0,
        "tie":0
    }
current_player=me
movesPlayed=0
class myBoard():
    def __init__(self, parent, board,turn):
        if parent==None:
            self.parent=self
            self.mydepth = 0
        else:
            self.parent = parent
            self.mydepth = parent.mydepth+1
        self.board = board

        self.turn=turn #t for ai f for human

    def gameOver(self):
        global movesPlayed
        movesPlayed=9
        if self.didWin()=='O':
            print("AI WON")
            status["Lost"]+=1
        elif self.didWin()=='X':
            print("You WON")
            status["Won"]+=1
        elif self.didWin()=="tie":
            print("oh MY its a TIE")
            status["tie"]+=1
        else:
            pass

    def bestmove(self):
        global current_player,me,ai
        bigNeg=-10000000000000000
        tmove=[0,0]
        if self.didWin()!=None:
            self.gameOver()
            return
        for i in range(0,3):
            for j in range(0, 3):
                if self.board[i][j]=="":
                    tboard=self.board
                    tboard[i][j]=ai
                    utility= self.minimax(tboard,False)
                    tboard[i][j]=""
                    if(utility >= bigNeg):
                        bigNeg=utility
                        tmove=[i,j]
                        print("in", tmove)


        self.board[tmove[0]][tmove[1]]=ai
        current_player=me
        self.printBoard()


    def printBoard(self):
        for i in range(0,3):
            for j in range(0,3):
                print("||",end="_")
                print(board[i][j],end="_")
            print("||")

    def equals3(self,a, b, c):
        if (a == b) and (b == c) and (a!=""):
            return True
        return False

    def didWin(self):
        winner = None

    #horizontal

        for i in range(0,3):
            if self.equals3(self.board[i][0], self.board[i][1], self.board[i][2]):
                winner = self.board[i][0]

     #Vertical
        for i in range(0,3):
            if self.equals3(self.board[0][i], self.board[1][i], self.board[2][i]):
                winner = self.board[0][i]

    #Diagonal
        if self.equals3(self.board[0][0], self.board[1][1], self.board[2][2]):
            winner = self.board[0][0]

        if self.equals3(self.board[2][0], self.board[1][1], self.board[0][2]):
            winner = self.board[2][0]

        openSpots = 0
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j] == '':
                    openSpots+=1
        #print("blocks" ,openSpots,winner)
        if ((winner == None) and (openSpots == 0)):
            #print("tititite")
            return "tie"
        else:
            return winner

    def minimax(self,board,isMaximizing):
        global current_player

        #minimax(board, depth, isMaximizing)
        scores = {
            "X": -10,
            "O": 10,
            "tie": 0
        }
        result = self.didWin()
        if (result != None):
            #print("res:",result)
            return scores[result]

        if (isMaximizing) :
            bigNeg = -10000000000000000
            for i in range(0, 3):
                for j in range(0, 3):
                    if board[i][j] == '':
                        print("i:",i,"j:",j)
                        board[i][j] = ai
                        current_player = me
                        utility = self.minimax(board,False)
                        board[i][j] = ''
                        print("max1:[",i,j,"]", utility, bigNeg)
                        bigNeg = max(utility, bigNeg)

            return bigNeg

        else:
            bigPos = 100000000000000000
            for i in range(0, 3):
                for j in range(0, 3):
                    if (board[i][j] == ''):
                        board[i][j] = me
                        current_player = ai
                        utility = self.minimax(board,True)
                        board[i][j] = ''
                        print("min1:[",i,j,"]", utility, bigPos)
                        bestScore = min(utility, bigPos)

            return bigPos

    def meMove(self):
        global current_player,me,ai
        choiceMaker={1:[0,0],
                     2:[0,1],
                     3:[0,2],
                     4:[1,0],
                     5:[1,1],
                     6:[1,2],
                     7:[2,0],
                     8:[2,1],
                     9: [2,2]
                     }

        if self.didWin() != None:
            self.gameOver()
            return

        pos=int(input("enter choice from 1 to 9:"))
        i=choiceMaker[pos]
        if self.board[i[0]][i[1]]=="":
            self.board[i[0]][i[1]]=me
            current_player=ai
        else:
            print("invalid")
        self.printBoard()
def refresh():
    global board
    board = [["", "", ""],
             ["", "", "", ],
             ["", "", ""]
             ]

def callmemain():
    global status,movesPlayed,current_player

    while True:
        ob = myBoard(None, board.copy(), True)
        ob.printBoard()
        movesPlayed=0
        #if input("first move me/ai")=="ai":
        #    current_player=ai
        #else:
        #    current_player = me
        while movesPlayed<=9:
            if current_player==ai:
                ob.bestmove()
                movesPlayed += 1
            else:
                ob.meMove()
                movesPlayed += 1
        phantom=input("Do You Wish To CONTINUE y/n")
        if phantom=='N' or phantom=='n':
            print(status)
            break
        else:
            refresh()
            current_player=me

callmemain()
