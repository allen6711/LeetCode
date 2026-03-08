class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counts = Counter(s)
        max_counts = max(counts.values())

        if max_counts > (n + 1) // 2:
            return ""
        
        heap = [(-cnt, ch) for ch, cnt in counts.items()]
        heapq.heapify(heap)
        ans = []

        while len(heap) >= 2:
            cnt1, ch1 = heapq.heappop(heap)
            cnt2, ch2 = heapq.heappop(heap)

            ans.append(ch1)
            ans.append(ch2)

            cnt1 += 1
            cnt2 += 1

            if cnt1 < 0:
                heapq.heappush(heap, (cnt1, ch1))
            if cnt2 < 0:
                heapq.heappush(heap, (cnt2, ch2))
            
        if heap:
            cnt, ch = heapq.heappop(heap)
            if -cnt > 1:
                return ""
            if ans and ans[-1] == ch:
                return ""
            
            ans.append(ch)
        
        return "".join(ans)














        # O(nlogk)
        # O(k+n)
        n = len(s)
        counts = Counter(s)
        max_count = max(counts.values())

        # Feasibility check
        if max_count > (n + 1) // 2:
            return ""
        
        # Max-heap using negative counts
        heap = [(-cnt, ch) for ch, cnt in counts.items()]
        heapq.heapify(heap)
        res = []

        while len(heap) >= 2:
            cnt1, ch1 = heapq.heappop(heap)  # most frequent
            cnt2, ch2 = heapq.heappop(heap)  # second most frequent

            # Append two different characters
            res.append(ch1)
            res.append(ch2)

            # Decrease counts (since cnt is negative, add 1)
            cnt1 += 1
            cnt2 += 1

            if cnt1 < 0:
                heapq.heappush(heap, (cnt1, ch1))
            if cnt2 < 0:
                heapq.heappush(heap, (cnt2, ch2))
        
        # If one char remains
        if heap:
            cnt, ch = heapq.heappop(heap)   # cnt is negative
            if -cnt > 1:
                return ""
            # Ensure no adjacent duplicate
            if res and res[-1] == ch:
                return ""
            res.append(ch)

        
        return "".join(res)
