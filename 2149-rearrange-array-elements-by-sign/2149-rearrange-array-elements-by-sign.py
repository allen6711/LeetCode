class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # O(n)
        # O(n)
        # pos = []
        # neg = []
        # for num in nums:
        #     if num > 0:
        #         pos.append(num)
        #     else:
        #         neg.append(num)
        # ans = []
        # for i in range(len(pos)):
        #     ans.append(pos[i])
        #     ans.append(neg[i])
            
        # return ans
        # O(n)
        # O(n)
        n = len(nums)
        ans = [0] * n
        pos = 0
        neg = 1
        for num in nums:
            if num > 0:
                ans[pos] = num
                pos += 2
            else:
                ans[neg] = num
                neg += 2
        return ans
