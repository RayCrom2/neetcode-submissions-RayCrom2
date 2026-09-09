from collections import defaultdict
class Solution:
    # def columnIsValid(self, column: List[]) -> bool:
    def rowIsValid(self, row: List[str]) -> bool:
        count = defaultdict(int)
        for ch in row:
            if (ch != '.'):
                if (count[ch] == 1):
                    return False
                count[ch] = 1
        return True
    def columnOrBoxIsValid(self, group: str) -> bool:
        count = defaultdict(int)
        for ch in group:
            if (ch != '.'):
                if (count[ch] == 1):
                    return False
                count[ch] = 1
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [""] * 9
        boxes = [""] * 9
        
        for rowIdx in range(len(board)):
            if (not self.rowIsValid(board[rowIdx])):
                return False;
            for i in range(9):
                columns[i] += board[rowIdx][i]
                boxIdx = 3 * (rowIdx // 3) + (i // 3)
                boxes[boxIdx] += board[rowIdx][i]
        for column in columns:
            if (not self.columnOrBoxIsValid(column)):
                return False
        for box in boxes:
            if (not self.columnOrBoxIsValid(box)):
                return False
        return True
        