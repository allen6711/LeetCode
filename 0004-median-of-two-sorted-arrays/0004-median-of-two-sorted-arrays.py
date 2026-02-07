class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B = B, A
            m, n = n, m
        
        half = (m + n + 1) // 2
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i

            A_left = -math.inf if i == 0 else A[i - 1]
            A_right = math.inf if i == m else A[i]
            B_left = -math.inf if j == 0 else B[j - 1]
            B_right = math.inf if j == n else B[j]

            if A_left <= B_right and A_right >= B_left:
                if (m + n) % 2 == 1:
                    return float(max(A_left, B_left))
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            
            if A_left > B_right:
                hi = i - 1
            else:
                lo = i + 1