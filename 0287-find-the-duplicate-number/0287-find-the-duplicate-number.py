class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd Cycle Detection
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

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