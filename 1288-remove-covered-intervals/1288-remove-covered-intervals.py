class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        max_end = 0
        for start, end in intervals:
            if end > max_end:
                max_end = end
                count += 1
        
        return count












        # O(nlogn)
        # O(1)
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        max_end = 0

        for start, end in intervals:
            if end > max_end:
                max_end = end
                count += 1
        
        return count
