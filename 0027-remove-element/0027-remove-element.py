class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left = 0
        ans = 0
        for right in range(n):
            if nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                ans += 1
        
        return ans












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