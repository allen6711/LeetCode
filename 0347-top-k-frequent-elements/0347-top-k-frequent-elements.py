class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n)
        # O(n)
        # Hash Map, Buckets Sort
        count = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)
        
        ans = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                ans.append(num)

                if len(ans) == k:
                    return ans

        return ans
        # O(n+ulog(k))
        # O(u+k)
        # Min Heap (Priority Queue)
        count = Counter(nums)
        heap = []

        for num, freq in count.items():    # O(u)
            heapq.heappush(heap, (freq, num))    # O(logH), H: number of elements in the Heap
                                                 # O(logH) = O(logk)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]