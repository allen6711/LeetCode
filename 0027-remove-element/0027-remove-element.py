class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # O(n)
        # O(n)
        # temp = []
        # for num in nums:
        #     if num != val:
        #         temp.append(num)
        # for i in range(len(temp)):
        #     nums[i] = temp[i]
        
        # return len(temp)
        # O(n)
        # O(1)
        write = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        return write

        