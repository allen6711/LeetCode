class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # O(nlog(max(piled)))
        # O(1)
        left = 1
        right = max(piles)
        def can_eat(speed: int) -> bool:
            total_hours = 0
            for pile in piles:
                hour = ceil(pile / speed)
                # hour = (pile + speed - 1) // speed
                total_hours += hour
                if total_hours > h:
                    return False
                
            return True
        
        while left <= right:
            mid = (left + right) // 2
            if can_eat(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left