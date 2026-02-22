class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            max_sum_i = nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1]
            if max_sum_i < target:
                continue
            min_sum_i = nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]
            if min_sum_i > target:
                break
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                max_sum_ij = nums[i] + nums[j] + nums[n - 2] + nums[n - 1]
                if max_sum_ij < target:
                    continue
                min_sum_ij = nums[i] + nums[j] + nums[j + 1] + nums[j + 2]
                if min_sum_ij > target:
                    break
                
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return ans














        # O(n^4)
        # O(m)
        # n = len(nums)
        # ans = []
        # visited = set()
        
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             for l in range(k + 1, n):
        #                 if nums[i] + nums[j] + nums[k] + nums[l] == target:
        #                     quad = tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))
        #                     if quad not in visited:
        #                         visited.add(quad)
        #                         ans.append(list(quad))
        # return ans
        # O(n^3)
        # O(1)
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 3):
            # Skip duplicate i
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            # Prune by min/max possible sums with fixed i
            min_sum_i = nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]
            if min_sum_i > target:
                break    # i increases -> min_sum_i only grows
            max_sum_i = nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3]
            if max_sum_i < target:
                continue  # even the largest is too small
            for j in range(i + 1, n - 2):
                # Skip duplicate j under the same i
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                # Prune by min/max possible sums with fixed i, j
                min_sum_ij = nums[i] + nums[j] + nums[j + 1] + nums[j + 2]
                if min_sum_ij > target:
                    break
                max_sum_ij = nums[i] + nums[j] + nums[n - 1] + nums[n - 2]
                if max_sum_ij < target:
                    continue
                
                left, right = j + 1, n - 1
                need = target - nums[i] - nums[j]
                while left < right:
                    two = nums[left] + nums[right]
                    if two == need:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif two < need:
                        left += 1
                    else:
                        right -= 1
        return ans
