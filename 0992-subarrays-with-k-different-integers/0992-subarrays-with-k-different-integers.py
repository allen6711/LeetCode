class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # O(n^2)
        # O(n)
        # n = len(nums)
        # ans = 0
        # for i in range(n):
        #     count = {}
        #     distinct = 0
        #     for j in range(i, n):
        #         x = nums[j]
        #         if x in count:
        #             count[x] += 1
        #         else:
        #             count[x] = 1
        #             distinct += 1
                
        #         if distinct == k:
        #             ans += 1
        #         elif distinct > k:
        #             break
        # return ans
        # O(n)
        # O(n)
        def at_most(k_limit: int) -> int:
            if k_limit < 0:
                return 0
            
            left = 0
            count = {}
            distinct = 0
            total_le = 0

            for right in range(len(nums)):
                x = nums[right]
                if x in count:
                    count[x] += 1
                else:
                    count[x] = 1
                    distinct += 1
                
                while distinct > k_limit:
                    left_num = nums[left]
                    count[left_num] -= 1
                    if count[left_num] == 0:
                        del count[left_num]
                        distinct -= 1
                    left += 1
                # All subarrays ending at 'right' with start in [left...right] are valid
                total_le += (right - left + 1)
            return total_le
        
        return at_most(k) - at_most(k - 1)

