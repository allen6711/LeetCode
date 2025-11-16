class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                box_index = (r // 3) * 3 + (c // 3)

                if val == ".":
                    continue
                
                if val in rows[r]:
                    return False
                if val in cols[c]:
                    return False
                if val in boxes[box_index]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)
        
        return True

        # rows = [set() for _ in range(9)]
        # cols = [set() for _ in range(9)]
        # boxes = [set() for _ in range(9)]

        # for r in range(9):
        #     for c in range(9):
                
        #         val = board[r][c]

        #         if val == ".":
        #             continue

        #         box_index = (r // 3) * 3 + (c // 3)

        #         if val in rows[r]:
        #             return False

        #         if val in cols[c]:
        #             return False
                
        #         if val in boxes[box_index]:
        #             return False
            
        #         rows[r].add(val)
        #         cols[c].add(val)
        #         boxes[box_index].add(val)
            
        # return True
        
        # rows = [set() for _ in range(9)]
        # cols = [set() for _ in range(9)]
        # boxes = [set() for _ in range(9)]

        # for r in range(9):
        #     for c in range(9):
        #         ch = board[r][c]
                
        #         if ch == ".":
        #             continue
                
        #         b = (r // 3) * 3 + (c // 3)
        #         if ch in rows[r] or ch in cols[c] or ch in boxes[b]:
        #             return False
                
        #         rows[r].add(ch)
        #         cols[c].add(ch)
        #         boxes[b].add(ch)
        
        # return True