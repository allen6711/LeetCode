class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        current = 1
        longest = 1
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                current = 1
            longest = max(longest, current)
        return longest









        # O(nlogn)
        # O(1)
        if not nums:
            return 0
        nums.sort()
        longest = 1
        current = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1
        return max(longest, current)














        # O(n)
        # O(n)
        s = set(nums)
        best = 0
        for num in s:
            if num - 1 in s:
                continue    # not a sequence start
            num2 = num
            while num2 in s:
                num2 += 1
            
            best = max(best, num2 - num)  # length
            
        return best