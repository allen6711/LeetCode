class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(n^2)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] == nums[j]:
        #             return True
        
        # return False

        # O(n)
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)

        return False

        # visited = set()
        # for num in nums:
        #     if num in visited:
        #         return True
        #     visited.add(num)
        
        # return False
        # visited = set()

        # for num in nums:
        #     if num in visited:
        #         return True
        #     visited.add(num)

        # return False
        
        # visited = set()

        # for num in nums:
        #     if num in visited:
        #         return True
            
        #     visited.add(num)
        
        # return False
        
        # num_set = set()

        # for num in nums:
        #     if num in num_set:
        #         return True
            
        #     num_set.add(num)
        
        # return False

        # visited = set()

        # for num in nums:
        #     if num in visited:
        #         return True
            
        #     visited.add(num)
        
        # return False

        # visited = set()

        # for num in nums:
        #     if num in visited:
        #         return True
        #     visited.add(num)

        # return False