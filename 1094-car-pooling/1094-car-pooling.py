class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        nums = [0] * 1001
        df = self.Difference(nums)
        for trip in trips:
            i = trip[1]
            # passengers get off at stop trip[2]
            # meaning the interval passengers are on the car is [trip[1], trip[2] - 1]
            j = trip[2] - 1
            val = trip[0]
            df.increment(i, j, val)
        
        res = df.result()

        for num in res:
            if num > capacity:
                return False
        
        return True
    
    class Difference:
        def __init__(self, nums: list[int]):
            assert len(nums) > 0
            self.diff = [0] * len(nums)
            self.diff[0] = nums[0]
            for i in range(1, len(self.diff)):
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