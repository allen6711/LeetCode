class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Binary search on the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left = 0
        right = m - 1
        while left < right:
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













        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B = B, A
            m, n = n, m
        
        half = (m + n + 1) // 2
        low, high = 0, m
        while low <= high:
            i = (low  + high) // 2
            j = half - i

            # Consider edge
            A_left = -math.inf if i == 0 else A[i - 1]
            A_right = math.inf if i == m else A[i]
            B_left = -math.inf if j == 0 else B[j - 1]
            B_right = math.inf if j == n else B[j]
            
            if A_left <= B_right and A_right >= B_left:
                if (m + n) % 2 == 1:
                    return float(max(A_left, B_left))
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2.0

            if A_left > B_right:
                high = i - 1
            else:
                low = i + 1














        # A, B = nums1, nums2
        # m, n = len(A), len(B)
        # if m > n:
        #     A, B = B, A
        #     m, n = n, m
        
        # half = (m + n + 1) // 2
        # lo, hi = 0, m
        # while lo <= hi:
        #     i = (lo + hi) // 2
        #     j = half - i

        #     A_left = -math.inf if i == 0 else A[i - 1]
        #     A_right = math.inf if i == m else A[i]
        #     B_left = -math.inf if j == 0 else B[j - 1]
        #     B_right = math.inf if j == n else B[j]

        #     if A_left <= B_right and A_right >= B_left:
        #         if (m + n) % 2 == 1:
        #             return float(max(A_left, B_left))
        #         return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            
        #     if A_left > B_right:
        #         hi = i - 1
        #     else:
        #         lo = i + 1