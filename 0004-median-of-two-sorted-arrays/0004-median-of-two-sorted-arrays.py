class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Binary search on the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left = 0
        right = m
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1

            nums1_left = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            nums1_right = float('inf') if partition1 == m else nums1[partition1]

            nums2_left = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            nums2_right = float('inf') if partition2 == n else nums2[partition2]

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m + n) % 2 == 1:
                    return max(nums1_left, nums2_left)
                
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            
            elif nums1_left > nums2_right:
                right = partition1 - 1
            
            else:
                left = partition1 + 1