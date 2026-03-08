class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # O(nlogn)
        nums.sort()
        return nums[-k]