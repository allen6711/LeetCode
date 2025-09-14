class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])
        if m == 0 or n == 0:
            return 0
        
        # Right position
        start, end = y, n - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if self.checkColumn(image, mid):
                # the last position of elements fitting condition
                start = mid

            else:
                end = mid
        
        right = end if self.checkColumn(image, end) else start

        # Left position
        start, end = 0, y
        
        while start + 1 < end:
            mid = (start + end) // 2

            if self.checkColumn(image, mid):
                # the first position of elements fitting condition
                end = mid
            
            else:
                start = mid
        
        left = start if self.checkColumn(image, start) else end

        # Up position
        start, end  = 0, x

        while start + 1 < end:
            mid = (start + end) // 2

            if self.checkRow(image, mid):
                # the first position of elements fitting condition
                end = mid
            
            else:
                start = mid
        
        up = start if self.checkRow(image, start) else end

        # Down position
        start, end = x, m - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if self.checkRow(image, mid):
                # the last position of elements fitting condition
                start = mid

            else:
                end = mid
        
        down = end if self.checkRow(image, end) else start

        return (right - left + 1) * (down - up + 1)

    
    def checkColumn(self, image, col) -> bool:
        for i in range(len(image)):
            if image[i][col] == "1":
                return True
        
        return False
    
    def checkRow(self, image, row) -> bool:
        for j in range(len(image[0])):
            if image[row][j] == "1":
                return True
        
        return False