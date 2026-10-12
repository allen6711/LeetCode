class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # O(m+n)
        # O(min(m, n))
        nums1_set = set(nums1)
        ans = set()
        for num in nums2:
            if num in nums1_set:
                ans.add(num)
        
        return list(ans)