class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(n)
        # O(1)
        n = len(numbers)
        left, right = 0, n - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        