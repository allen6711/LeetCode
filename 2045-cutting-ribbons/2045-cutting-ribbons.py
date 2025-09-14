class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        # [9, 5, 7], k = 3
        # end                start
        # 9 8 7 6 5 4 3 .... 1  # 
        # 1 1 2 2 3 4 6 .... 21 # k
        if not ribbons:
            return 0

        start, end = 1, max(ribbons)

        while start + 1 < end:
            mid = (start + end) // 2

            if self.get_pieces(ribbons, mid) >= k:
                start = mid
            
            else:
                end = mid
        
        # # If end never moves until the while loop finishes
        if self.get_pieces(ribbons, end) >= k:
            return end

        if self.get_pieces(ribbons, start) >= k:
            return start
        
        return 0

    def get_pieces(self, ribbons, length) -> int:
        pieces = 0

        for ribbon in ribbons:
            pieces += ribbon // length
        
        return pieces
        