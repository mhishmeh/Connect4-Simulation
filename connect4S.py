import random as rd


class Connect4:
    def __init__(self):
        "initialize needed attributes for game"
        # Key for numerical to X/O pieces:
        # 0 = empty space
        # 1 = X Space
        # -1 = O Space

        # 'self.board' will be used to display and manipulate the game board
        self.board = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]
        # 'self.over' will be used to tell if the game is over and that the game should end
        self.over = False
        # self.last is just the current player
        self.last = 1

    def __repr__(self):
        "this method is used so the print() for the class object will construct the desired board to the terminal"

        # 'game_display' will be a string that contains the game board and it is
        # formed by iterating over 'self.board' and adding appropriate spacing and lines
        game_display = ""

        for row in self.board:
            game_display += "|"
            for mark in row:
                # the piece is X
                if mark == 1:
                    game_display += "X" + "|"
                # the piece is O
                elif mark == -1:
                    game_display += "O" + "|"
                else:
                    # empty space
                    game_display += "-" + "|"
            game_display += "\n"
        return game_display

    def checkHorizontal(self, row, col, player):
        "check if the player has won horizontally based on the position and the player"
        # we can reference self.board with some shorthand 'brd'
        brd = self.board

        # the position given is filled by the player
        if brd[row][col] == player:
            matches = 1
            index = col
            # this while loop handles checking the spaces to the left of the given position
            while index > 0:
                if brd[row][index-1] == player:
                    matches += 1
                    index -= 1
                else:
                    break
            index = col
            # this while loop handles checking the spaces to the right of the given position
            while index < 6:
                if brd[row][index+1] == player:
                    matches += 1
                    index += 1
                else:
                    break
            # if there were four or more matches horizontally then return True for the player has won
            if matches >= 4:
                return True
            else:
                return False

        # the position given isn't filled by the player
        else:
            return False

    def checkVertical(self, row, col, player):
        "check if the player has won vertically"
        # we can reference self.board with some shorthand 'brd'
        brd = self.board
        # the position given is filled by the player
        if brd[row][col] == player:
            matches = 1
            index = row
            # this while loop handles checking the spaces above the given position
            while index > 0:
                if brd[index-1][col] == player:
                    matches += 1
                    index -= 1
                else:
                    break
            index = row
            # this while loop handles checking the spaces below the given position
            while index < 5:
                if brd[index+1][col] == player:
                    matches += 1
                    index += 1
                else:
                    break
            # if the player has 4 or more matches than return True for the player has won
            if matches >= 4:
                return True
            else:
                return False
        else:
            return False

    def checkDiagnonal(self, row, col, player):
        "check if the player has won diagonally"
        # we can reference self.board with some shorthand 'brd'
        brd = self.board
        # check if the position given is filled by the player
        if brd[row][col] == player:
            # theres two 'matches' variables as a player can win diagonally in two ways
            # one way is a ray traveling from the bottom left direction to the top right direction ('upperRightMathces')
            # the other way is a ray traveling from the top left direction to the bottom right direction ('upperLeftMathces')
            upperRightMatches = 1
            upperLeftMatches = 1

            # ro and cl are copies of arguments that will be manipulated in while loop
            ro = row
            cl = col

            # these next two while loops are for checking 'upperRightMatches'
            while ro > 0 and cl < 6:
                if brd[ro-1][cl+1] == player:
                    upperRightMatches += 1
                    ro -= 1
                    cl += 1
                else:
                    break
            # reset ro and cl
            ro = row
            cl = col
            while ro < 5 and cl > 0:
                if brd[ro+1][cl-1] == player:
                    upperRightMatches += 1
                    ro += 1
                    cl -= 1
                else:
                    break
            # reset ro and cl
            ro = row
            cl = col
            # these next 2 while loops are for checking 'upperLeftMatches'
            while ro > 0 and cl > 0:
                if brd[ro-1][cl-1] == player:
                    upperLeftMatches += 1
                    ro -= 1
                    cl -= 1
                else:
                    break
            # reset ro and cl
            ro = row
            cl = col
            while ro < 5 and cl < 6:
                if brd[ro+1][cl+1] == player:
                    upperLeftMatches += 1
                    ro += 1
                    cl += 1
                else:
                    break
        # if there was 4 or more matches in any diagonal direction then return true for the player has won
            if upperLeftMatches >= 4:
                return True
            elif upperRightMatches >= 4:
                return True
            else:
                return False
        # the position was not filled by the player
        else:
            return False

    def isGameTie(self):
        "Check if the game is a tie"
        Istie = True
        # we can reference self.board with some shorthand 'brd'
        brd = self.board

        # Note: since this function is only called after checking if
        # a player has won, it is true that if no player has won and
        # the board has no empty spaces then the game is a tie
        for row in brd:
            for mark in row:
                if mark == 0:
                    Istie = False
        if Istie:
            self.last = None
        return Istie

    def findRowIndice(self, column):
        "given a column find the space that a piece can be dropped in"
        row = 0
        # we can reference self.board with some shorthand 'brd'

        brd = self.board
        # note that if row is returned as -1 that means the column is filled
        while row < 6:
            if brd[row][column] in [-1, 1]:
                row -= 1
                return row
            elif brd[row][column] == 0 and row == 5:
                return row
            elif brd[row][column] == 0:
                row += 1

    def getAvailableMoves(self):
        "find all available moves based on self.board"
        moves = []
        for column in range(7):
            row = self.findRowIndice(column)
            if row != -1:
                moves.append([row, column])
        return moves

    def playGame(self):
        "Play human vs human game"
        while self.over == False:
            if self.last == 1:
                user = "X"
            else:
                user = "O"
            while True:
                print(" 1 2 3 4 5 6 7")
                print(self.__str__())
                print("{}'s turn: Enter a column number:".format(user))

                column = int(
                    input()) - 1
                if column not in [0, 1, 2, 3, 4, 5, 6]:
                    continue
                row = self.findRowIndice(column)
                if row != -1:
                    break
            # assign the chosen value to the players mark
            # note userInpt is the column for the chosen space
            self.board[row][column] = self.last
            plyer = 1
            end = False
            state = False

            # iterate twice to check for both players (X and O)
            for i in range(2):
                # use nested for loops to check every position of self.board for win
                for row in range(6):
                    for col in range(7):
                        if self.checkDiagnonal(row, col, plyer) or self.checkHorizontal(row, col, plyer) or self.checkVertical(row, col, plyer):
                            state = True
                            end = True
                        if end:
                            break
                    if end:
                        break
                if end:
                    break
                plyer = -1
            # check for tie if no win
            if state == False:
                if self.isGameTie():
                    state = True

            if state == True:
                self.over = True
                print(self.__str__())
                # if self.last = None then that means it was a tie
                if self.last == None:
                    print("The game was a tie!")
                    return 0
                else:
                    print("Won at ", row, col)
                    if plyer == 1:
                        print("X won the game!")
                    elif plyer == -1:
                        print("O won the game!")
                    return plyer
            # switch the players

            if self.last == 1:
                self.last = -1
            else:
                self.last = 1

    def playRandom(self):
        "play random versus random game"
        while self.over == False:
            move = rd.choice(self.getAvailableMoves())
            row = move[0]
            column = move[1]

            # assign the chosen value to the players mark
            # note userInpt is the column for the chosen space
            self.board[row][column] = self.last
            plyer = 1
            end = False
            state = False

            for i in range(2):
                for row in range(6):
                    for col in range(7):
                        if self.checkDiagnonal(row, col, plyer) or self.checkHorizontal(row, col, plyer) or self.checkVertical(row, col, plyer):
                            state = True
                            end = True
                        if end:
                            break
                    if end:
                        break
                if end:
                    break
                plyer = -1

            if state == False:
                if self.isGameTie():
                    state = True

            if state == True:
                self.over = True
                print(self.__str__())
                # if self.last = None then that means it was a tie
                if self.last == None:
                    print("The game was a tie!")
                    return 0
                else:
                    print("Won at ", row, col)
                    if plyer == 1:
                        print("X won the game!")
                    elif plyer == -1:
                        print("O won the game!")
                    return plyer
            # switch the players
            if self.over == False:
                print("self.last", self.last)
                print("row chosen and then column", row, column)

                print("gamestatus :", state)

                print(self.__str__())

            if self.last == 1:
                self.last = -1
            else:
                self.last = 1


board = Connect4()
board.playRandom()
