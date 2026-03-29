class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # O(n^2)
        # O(n)
        # if numRows == 1:
        #     return s
        # rows = [""] * numRows
        # cur_row = 0
        # going_down = True
        
        # for ch in s:
        #     rows[cur_row] += ch

        #     if cur_row == 0:
        #         going_down = True
        #     elif cur_row == numRows - 1:
        #         going_down = False
            
        #     if going_down:
        #         cur_row += 1
        #     else:
        #         cur_row -= 1

        # return "".join(rows)
        # O(n)
        # O(n)
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [[] for _ in range(numRows)]
        cur_row = 0
        direction = 1  # 1 means moving down, -1 means moving up
        for ch in s:
            rows[cur_row].append(ch)

            if cur_row == 0:
                direction = 1
            elif cur_row == numRows - 1:
                direction = -1

            cur_row += direction

        return "".join("".join(row) for row in rows)