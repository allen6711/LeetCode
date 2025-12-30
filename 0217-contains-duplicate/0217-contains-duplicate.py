class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
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