class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        '''
    Every time processing a non-dot character, must add it to three sets:
	1.	The set for its row
	2.	The set for its column
	3.	The set for its 3×3 block
        '''
        #rows = []
        #for i in range(9):
        #   rows.append(set())
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]# nine 3*3 blocks
        for i in range(9):#brute force
            for j in range(9):
                c = board[i][j]
                if c == ".":
                    continue#skip inner for loop round
                boxIdx = (i // 3) * 3 + (j // 3)
                if c in rows[i] or c in cols[j] or c in boxes[boxIdx]:
                    return False
                rows[i].add(c)
                cols[j].add(c)
                boxes[boxIdx].add(c)
        return True