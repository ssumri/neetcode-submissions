class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        columns = {}
        rows = {}
        boxes = {}
        counter = 0
        offset = 0
        for i in range(len(board)):
            rows[i] = []

            for j in range(len(board[i])):
                if (i % 3 == 0) and (j % 3 == 0):
                    boxes[counter] = []
                    counter += 1
                
                if board[i][j] != '.' and board[i][j] in boxes[offset + int(j/3) + int(i/3)]:
                    return False
                if i == 0:
                    columns[j] = []
                
                if board[i][j] != '.' and board[i][j] in columns[j]:
                    return False
                
                if board[i][j] != '.' and board[i][j] in rows[i]:
                    return False
                boxes[offset + int(j/3) + int(i/3)].append(board[i][j])
                columns[j].append(board[i][j])
                rows[i].append(board[i][j])
            
            #check boxes at every 3
            if i == 2 or i == 5 or i == 8:
                offset += 2

        

        return True 

        