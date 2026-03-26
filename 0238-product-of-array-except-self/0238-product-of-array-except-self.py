class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        product_prefix = 1
        for i in range(n):
            ans[i] = product_prefix
            product_prefix *= nums[i]
        
        product_postfix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= product_postfix
            product_postfix *= nums[i]
        
        return ans
















        # O(n^2)
        # O(n)
        # n = len(nums)
        # answer = []
        # for i in range(n):
        #     product = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         product *= nums[j]
        #     answer.append(product)
        
        # return answer
        # O(n)
        # O(n)
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        
        return answer