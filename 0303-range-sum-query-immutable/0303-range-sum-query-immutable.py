class NumArray:

    def __init__(self, nums: List[int]):
        self.numArr = nums
        self.total = 0

    def sumRange(self, left: int, right: int) -> int:
        self.total = 0
        for i in range(left, right + 1):
            self.total += self.numArr[i]
        
        return self.total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)