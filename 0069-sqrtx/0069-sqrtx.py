class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        
        while start + 1 < end:
            mid = (start + end) // 2

            if mid * mid <= x:
                start = mid

            else:
                end = mid

        if end * end <= x:
            return end
            
        if start * start <= x:
            return start




























        # if x == 0:
        #     return 0
        # left, right = 0, x
        # result = -1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if mid * mid == x:
        #         return mid
        #     elif mid * mid > x:
        #         result = mid
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return result - 1