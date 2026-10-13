class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        num_set = set(nums)
        for i in range(n + 1):
            if i not in num_set:
                return i
        
        return -1













        # O(nlogn)
        # O(1)
        # nums.sort()
        # for i, num in enumerate(nums):
        #     if i != num:
        #         return i
        # return len(nums)
        # O(n)
        # O(n)
        # num_set = set(nums)
        # n = len(nums)
        # for num in range(n + 1):
        #     if num not in num_set:
        #         return num
        # return -1
        # O(n)
        # O(1)
        ## Sum
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual
        ## XOR
        # n = len(nums)
        # x = n
        # for i, num in enumerate(nums):
        #     x ^= i
        #     x ^= num
        # return x
        

     