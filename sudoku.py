class Solution:
    def get_box_id(self, r, c) -> int:
            return ((r//3)*3 + c//3)
        
     
    def isValid(self,box,row,col,num) -> bool:
        if num in box or num in row or num in col:
            return False
        else:
            return True



    def solve(self, board, boxes, rows, cols, r, c) -> bool:
        if r == len(board) or c == len(board):
            return True
        if board[r][c] == ".":
            for num in range(1, 10):
                box_id=self.get_box_id(r,c)
                box=boxes[box_id]
                row=rows[r]
                col=cols[c]
                if self.isValid(box, row, col, str(num)):
                    board[r][c]=str(num)
                    boxes[box_id][str(num)]=True
                    cols[c][str(num)]=True
                    rows[r][str(num)]=True
                    if c == len(board) - 1:
                        if self.solve(board, boxes, rows, cols, r+1, 0):
                            return True
                    else:
                        if self.solve(board, boxes, rows, cols, r, c + 1):
                            return True
                    del box[str(num)]
                    del row[str(num)]
                    del col[str(num)]
                    board[r][c]="."
        else:
            if c == len(board) - 1:
                if self.solve(board, boxes, rows, cols, r+1, 0):
                    return True
            else:
                if self.solve(board, boxes, rows, cols, r, c + 1):
                    return True

        return False
        
    def solveSudoku(self, board: List[List[str]]) -> None:
       
        rows=[{} for _ in range(len(board))]
        cols=[{} for _ in range(len(board))]
        boxes=[{} for _ in range(len(board))]
        
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c]!='.':
                    val=board[r][c]
                    box_id=self.get_box_id(r,c)
                    boxes[box_id][val]=True
                    rows[r][val]=True
                    cols[c][val]=True
                    
        self.solve(board,boxes,rows,cols,0,0)
       
