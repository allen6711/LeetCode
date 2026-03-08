class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort meetings by start date
        intervals.sort(key=lambda x: x[0])

        # Min-heap of end times
        heap = []
        heapq.heappush(heap, (intervals[0][1]))

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            # If the earliest ending meeting ends before this one starts, reuse the room
            if heap[0] <= start:
                heapq.heappop(heap)
            
            heapq.heappush(heap, end)
        
        return len(heap)


















        meeting_delta = []
        for start, end in intervals:
            meeting_delta.append((start, 1))
            meeting_delta.append((end, -1))

        meeting_delta.sort()
        cur = ans = 0

        for _, delta in meeting_delta:
            cur += delta
            if cur > ans:
                ans = cur
        
        return ans
            