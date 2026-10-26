class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # O(n^2) -> O(nlogn + n^2)
        # O(1)
        n = len(nums)
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(ans - target):
                    ans = total

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total

        return ans
        # O(n^3)
        # O(1)
        # n = len(nums)
        # best_sum = nums[0] + nums[1] + nums[2]
        # best_diff = abs(best_sum - target)

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             total = nums[i] + nums[j] + nums[k]
        #             diff = abs(total - target)
        #             if diff < best_diff:
        #                 best_sum = total
        #                 best_diff = diff
        # return best_sum