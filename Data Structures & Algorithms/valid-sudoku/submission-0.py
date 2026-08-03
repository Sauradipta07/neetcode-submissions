class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set()for num in range(9)]
        columns=[set()for num in range(9)]
        submat=[set()for num in range(9)]

        for i in range(9):
            for j in range(9):
                val=board[i][j]
                if val == ".":
                    continue

                if val in rows[i]:
                    return False
                rows[i].add(val)

                if val in columns[j]:
                    return False
                columns[j].add(val)
                idx=(i//3)*3+(j//3)

                if val in submat[idx]:
                    return False
                submat[idx].add(val)
        return True
                
        