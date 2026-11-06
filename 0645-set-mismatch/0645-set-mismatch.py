class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # O(n)
        # O(1)
        duplicate = -1
        missing = -1
        n = len(nums)

        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                duplicate = abs(num)
            else:
                nums[index] *= -1
        
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1
        
        return [duplicate, missing]

# 因为题目里的数字是从 1 到 n，而数组索引是从 0 开始的，这中间有一个 1 的偏移。
# 算法的核心思路是：把数字 x 映射到索引 x - 1 上。当数字 x 出现时，就把 nums[x - 1] 变成负数，相当于给索引 x - 1 打了个“已访问”的标记。
# 如果遍历结束后，发现索引 i 上的元素依然是正数（nums[i] > 0），就说明没有任何数字映射到索引 i。
# 既然索引 i 没有被标记过，根据 x - 1 = i 这个映射关系反推，缺失的那个数字自然就是 i + 1 了。

        # o(n)
        # O(n)
        visited = set()
        duplicate = -1
        n = len(nums)

        for num in nums:
            if num in visited:
                duplicate = num
            else:
                visited.add(num)
        
        for num in range(1, n + 1):
            if num not in visited:
                return [duplicate, num]
        
        return []

