class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)

            else:
                if num > heap[0]:
                    heapq.heapreplace(heap, num)

        return heap[0]














        # O(nlogn)
        # O(1)
        # nums.sort()
        # return nums[-k]
        # O(nlogk)
        # O(k)
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)   # O(logk)
            else:
                # heap[0] is the smallest among the current top-k elements
                if num > heap[0]:        # O(logk)
                    heapq.heapreplace(heap, num)  # pop + push in one operation
        
        return heap[0]


            
