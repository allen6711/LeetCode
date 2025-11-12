class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}

        for i, num in enumerate(nums):
            dif = target - num
            if dif in num_index:
                return [num_index[dif], i]

            num_index[num] = i
        
        return False

        # num_index = {}

        # for i, num in enumerate(nums):
        #     diff = target - num
        #     if diff in num_index:
        #         return [num_index[diff], i]

        #     num_index[num] = i
        
        # return False