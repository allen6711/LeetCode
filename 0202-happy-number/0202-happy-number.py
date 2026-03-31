class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.get_help(n)
        while slow != fast and fast != 1:
            slow = self.get_help(slow)
            fast = self.get_help(self.get_help(fast))

        return fast == 1
    def get_help(self, num: int) -> int:
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        
        return total








        # O(logn)
        # O(logn)
        # visited = set()
        # while n != 1:
        #     if n in visited:
        #         return False
        #     visited.add(n)
        #     n = self.get_next(n)

        # return True
        # O(logn)
        # O(1)
        slow = n
        fast = self.get_next(n)
        while fast != 1 and slow != fast:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))
        
        return fast == 1
    
    def get_next(self, num: int) -> int:
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        
        return total