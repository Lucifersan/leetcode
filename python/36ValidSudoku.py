#horrible code holy crap
#...if it works it works...
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        contains = set() 
        for i in board:
            contains.clear()
            for x in i:
                if x in contains: return False
                if x != ".": contains.add(x)
        for i in range(9):
            contains.clear()
            for j in range(9):
                if board[j][i] in contains: return False
                if board[j][i] != ".": contains.add(board[j][i])
        contains1 = set()
        contains2 = set()
        contains3 = set()
        contains4 = set()
        contains5 = set()
        contains6 = set()
        contains7 = set()
        contains8 = set()
        contains9 = set()
        for i in range(9):
            for j in range(9):
                if i < 3:
                    if j < 3: 
                        if board[j][i] in contains1: return False
                        if board[j][i] != ".": contains1.add(board[j][i])
                    elif j < 6:
                        if board[j][i] in contains2: return False
                        if board[j][i] != ".": contains2.add(board[j][i])
                    elif j < 9:
                        if board[j][i] in contains3: return False
                        if board[j][i] != ".": contains3.add(board[j][i])
                elif i < 6:
                    if j < 3: 
                        if board[j][i] in contains4: return False
                        if board[j][i] != ".": contains4.add(board[j][i])
                    elif j < 6:
                        if board[j][i] in contains5: return False
                        if board[j][i] != ".": contains5.add(board[j][i])
                    elif j < 9:
                        if board[j][i] in contains6: return False
                        if board[j][i] != ".": contains6.add(board[j][i])
                elif i < 9:
                    if j < 3: 
                        if board[j][i] in contains7: return False
                        if board[j][i] != ".": contains7.add(board[j][i])
                    elif j < 6:
                        if board[j][i] in contains8: return False
                        if board[j][i] != ".": contains8.add(board[j][i])
                    elif j < 9:
                        if board[j][i] in contains9: return False
                        if board[j][i] != ".": contains9.add(board[j][i])
        return True

        