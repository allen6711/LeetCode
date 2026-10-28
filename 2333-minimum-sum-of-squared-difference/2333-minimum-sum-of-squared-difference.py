class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diff) <= k:
            return 0
        
        max_diff = max(diff)
        count = [0] * (max_diff + 1)

        for d in diff:
            count[d] += 1
        
        for d in range(max_diff, 0, -1):
            if k == 0:
                break
            
            operations = min(k, count[d])

            count[d] -= operations
            count[d - 1] += operations
            k -= operations
        
        ans = 0
        for d in range(max_diff + 1):
            ans += d * d * count[d]
        
        return ans