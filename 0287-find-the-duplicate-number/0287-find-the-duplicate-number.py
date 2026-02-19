class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(nlogn)
        # O(1)
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return nums[i]
        
        return -1
        

















        slow, fast = 0, 0
        # Find the circle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        finder = 0
        while finder != fast:
            finder = nums[finder]
            fast = nums[fast]

        return finder

        # Floyd Cycle Detection
        # slow = 0
        # fast = 0
        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break
        
        # slow = 0
        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[fast]

        # return slow

        # slow = nums[0]
        # fast = nums[0]
        
        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break
        
        # finder = nums[0]
        # while finder != slow:
        #     finder = nums[finder]
        #     slow = nums[slow]
        
        # return finder