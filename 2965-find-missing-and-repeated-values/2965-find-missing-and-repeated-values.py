class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # O(n^2)
        # O(n^2)
        # m, n = len(grid), len(grid[0])
        # length = m * n
        # freq = [0] * (length + 1)
        # for row in grid:
        #     for num in row:
        #         freq[num] += 1

        # repeated = -1
        # missing = -1
        
        # for num in range(1, length + 1):
        #     if freq[num] == 2:
        #         repeated = num
        #     elif freq[num] == 0:
        #         missing = num
        
        # return [repeated, missing]
        # O(n^2)
        # O(1)
        n = len(grid)
        m = n * n
        total_m = (m*(m + 1)) // 2
        total_m2 = (m*(m + 1)*(2 * m + 1)) // 6
        actual_total_m = 0
        actual_total_m2 = 0
        for row in grid:
            for num in row:
                actual_total_m += num
                actual_total_m2 += num * num
        
        a_minus_b = total_m - actual_total_m
        a2_minus_b2 = total_m2 - actual_total_m2
        a_add_b = a2_minus_b2 // a_minus_b

        a = (a_minus_b + a_add_b) // 2
        b = a_add_b - a
        return [b, a]
        