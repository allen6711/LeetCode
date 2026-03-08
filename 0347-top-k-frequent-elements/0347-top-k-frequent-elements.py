class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count_num = Counter(nums)
        for num, freq in count_num.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                if freq > heap[0][0]:
                    heapq.heapreplace(heap, (freq, num))
        
        return [num for freq, num in heap]














        # O(n+mlogk)
        # O(m)
        counts = Counter(nums)
        
        heap = []  # (freq, num)
        for num, freq in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            
            else:
                # Keep the k highest frequencies in the heap
                if freq > heap[0][0]:
                    heapq.heapreplace(heap, (freq, num))
        
        return [num for freq, num in heap]