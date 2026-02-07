class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return -1
        max_speed = max(piles)
        left, right = 1, max_speed
        while left + 1 < right:
            mid = (left + right) // 2
            eating_time = self.countHours(piles, mid)
            if eating_time <= h:
                right = mid
            else:
                left = mid
        
        if self.countHours(piles, left) <= h:
            return left
        if self.countHours(piles, right) <= h:
            return right
        
        return -1
        
    def countHours(self, piles: List[int], k: int) -> int:
        hours = 0
        for num in piles:
            hours += math.ceil(num / k)
        
        return hours
















        # piles: [5, 6, 8]
        # h hours
        # eating speed: bananas/hr
        # hours in pile: ceil(pile/h)
        # as slow as she can: minimum k in h
        # k: 1,         2, 3, ..., 8
        # h: 19=sum(piles),        3
        # condition: smaller than h
    #     if not piles:
    #         return -1

    #     start, end = 1, max(piles)

    #     while start + 1 < end:
    #         mid = (start + end) // 2

    #         if self.countHours(piles, mid) <= h:
    #             end = mid
            
    #         else:
    #             start = mid
        
    #     # Test the smaller one first
    #     if self.countHours(piles, start) <= h:
    #         return start

    #     if self.countHours(piles, end) <= h:
    #         return end
        
    #     return -1


    # def countHours(self, piles, speed):
    #     hours = 0

    #     for pile in piles:
    #         hours += ceil(pile / speed)
        
    #     return hours



        # left, right = 1, int(1e9)
        # while left < right:
        #     mid = (left + right) // 2
        #     total_hours = 0
            
        #     for pile in piles:
        #         total_hours += (pile + mid - 1) // mid
            
        #     if total_hours <= h:
        #         right = mid
        #     else:
        #         left = mid + 1
        
        # return left