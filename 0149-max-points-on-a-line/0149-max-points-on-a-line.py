class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # O(n^3)
        # O(1)
        n = len(points)
        if n <= 2:
            return n
        ans = 2
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                cnt = 2
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
                        cnt += 1
                ans = max(ans, cnt)

        return ans