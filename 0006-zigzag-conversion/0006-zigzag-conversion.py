class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # O(n^2)
        # O(n)
        if numRows == 1:
            return s
        rows = [""] * numRows
        cur_row = 0
        going_down = True
        
        for ch in s:
            rows[cur_row] += ch

            if cur_row == 0:
                going_down = True
            elif cur_row == numRows - 1:
                going_down = False
            
            if going_down:
                cur_row += 1
            else:
                cur_row -= 1

        return "".join(rows)