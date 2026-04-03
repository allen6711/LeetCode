class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.get_next(n)
        while fast != 1 and slow != fast:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))
        
        return fast == 1


    def get_next(self, n: int) -> int:
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        
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