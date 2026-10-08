class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # O(nlogn)
        # O(1)
        left = max(nums)
        right = sum(nums)

        def can_split(max_sum: int) -> bool:
            current_sum = 0
            count = 1
            for num in nums:
                if current_sum + num > max_sum:
                    current_sum = num
                    count += 1
                else:
                    current_sum += num
            
            return count <= k
        
        while left <= right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left