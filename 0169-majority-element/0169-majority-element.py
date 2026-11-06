class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(n)
        # O(n)
        # n = len(nums)
        # maj = n // 2
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1
        #     if count[num] > maj:
        #         return num
        
        # return -1
        # O(n)
        # O(1)
        # Boyer-Moore Voting Algorithm
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate