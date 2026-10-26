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
        n = len(nums)
        left = 0
        # ans = 0
        for right in range(n):
            if nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                # ans += 1
        
        return left
        # Two Pointers, Swap with End
        # Exclusive right: right 指向尚未處理範圍的右邊界之外，因此使用 <，最後直接回傳 right
        # O(n)
        # O(1)
        n = len(nums)
        left, right = 0, n
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1
        
        return right