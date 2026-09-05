class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def side_sum(x: int, length: int) -> int:
            # x - 1, x - 2, ...
            if x - 1 > length:
                return (x - 1 + (x - length)) * length // 2
            # x - 1, x - 2, 1, 1, 1
            else:
                return (x - 1 + 1) * (x - 1) // 2 + (length - (x - 1))
            
        def can_build(x) -> bool:
            left = side_sum(x, index)
            right = side_sum(x, n - index - 1)

            total = left + x + right
            
            return total <= maxSum

        left, right = 1, maxSum
        while left <= right:
            mid = (left + right) // 2
            if can_build(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right