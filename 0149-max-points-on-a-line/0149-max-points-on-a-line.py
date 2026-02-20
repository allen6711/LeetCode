class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # # O(n^3)
        # # O(1)
        # n = len(points)
        # if n <= 2:
        #     return n
        # ans = 2
        # for i in range(n):
        #     x1, y1 = points[i]
        #     for j in range(i + 1, n):
        #         x2, y2 = points[j]
        #         cnt = 2
        #         for k in range(j + 1, n):
        #             x3, y3 = points[k]
        #             if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
        #                 cnt += 1
        #         ans = max(ans, cnt)

        # return ans
        # O(n^2)
        # O(1)
        n = len(points)
        if n <= 2:
            return n
        ans = 1

        for i in range(n):
            slopes = defaultdict(int)
            dup = 0
            local_max = 0

            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                if dx == 0 and dy == 0:
                    dup += 1
                    continue
                
                # Normalize slope as a reduced function (dy, dx)
                if dx == 0:
                    key = (1, 0)    # vertical line
                elif dy == 0:
                    key = (0, 1)    # horizontal line
                else:
                    g = gcd(abs(dy), abs(dx))
                    dy //= g
                    dx //= g

                    # Make dx positive for a unique representation
                    if dx < 0:
                        dx = -dx
                        dy = -dy
                    
                    key = (dy, dx)

                slopes[key] += 1
                local_max = max(local_max, slopes[key])
            
            # +1 counts the base point itself, +dup counts identical points
            ans = max(ans, local_max + 1 + dup)
        
        return ans
                    
        
