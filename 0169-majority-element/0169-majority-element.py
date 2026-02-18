class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(n)
        freq = defaultdict(int)
        threshold = len(nums) // 2
        for num in nums:
            freq[num] += 1
            if freq[num] > threshold:
                return num
        
        return -1

















        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count += 1

            elif num == candidate:
                count += 1

            else:
                count -= 1
        
        return candidate