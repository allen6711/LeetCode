class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)

        # 題目要求建立這個變數
        velqoradin = nums

        prefix_gcd = []
        max_so_far = 0

        # Step 1: 建立 prefixGcd
        for num in velqoradin:
            max_so_far = max(max_so_far, num)
            prefix_gcd.append(gcd(num, max_so_far))

        # Step 2: 排序
        prefix_gcd.sort()

        # Step 3: 最小值與最大值配對
        left = 0
        right = n - 1
        answer = 0

        while left < right:
            answer += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1

        return answer