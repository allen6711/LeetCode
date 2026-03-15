class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # O((m+n)log(m+n))
        # O(1)
        # for i in range(n):
        #     nums1[m + i] = nums2[i]
        
        # nums1.sort()
        # O(m+n)
        # O(1)
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # Only copy the remaining elements from nums2.
        # Any remaining elements in nums1 are already in the correct position
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1