class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        nums = [0] * length
        df = self.Difference(nums)
        
        for update in updates:
            i = update[0]
            j = update[1]
            val = update[2]
            df.increment(i, j, val)
        
        return df.result()

    class Difference:
        def __init__(self, nums: List[int]):
            assert len(nums) > 0
            self.diff = [0] * len(nums)

            self.diff[0] = nums[0]
            for i in range(1, len(nums)):
                self.diff[i] = nums[i] - nums[i - 1]
        
        def increment(self, i: int, j: int, val: int):
            self.diff[i] += val
            if j + 1 < len(self.diff):
                self.diff[j + 1] -= val
        
        def result(self) -> list[int]:
            res = [0] * len(self.diff)
            res[0] = self.diff[0]

            for i in range(1, len(self.diff)):
                res[i] = res[i - 1] + self.diff[i]
            
            return res