class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        answer = []
        freq = Counter(nums)
        buckets = [[] for _ in range(n + 1)]

        for num, count in freq.items():
            buckets[count].append(num)
        
        for i in range(n, 0, -1):
            if not buckets[i]:
                continue
            
            for num in buckets[i]:
                answer.append(num)
                if len(answer) == k:
                    return answer
        
        return answer

        # freq = Counter(nums)
        # n = len(nums)
        # buckets = [[] for _ in range(n + 1)]
        # answer = []

        # for num, count in freq.items():
        #     buckets[count].append(num)
        
        # for i in range(n, 0, -1):
        #     if not buckets[i]:
        #         continue
            
        #     for num in buckets[i]:
        #         answer.append(num)
        #         if len(answer) == k:
        #             return answer
        
        # return answer
        
        # freq = Counter(nums)
        # n = len(nums)
        # result = []
        # buckets = [[] for _ in range(n + 1)]

        # for num, count in freq.items():
        #     buckets[count].append(num)
        
        # for count in range(n, 0, -1):
        #     if not buckets[count]:
        #         continue
            
        #     for num in buckets[count]:
        #         result.append(num)
        #         if len(result) == k:
        #             return result
        
        # return result

        
        # num_frequencies = Counter(nums)
        # min_heap = []
        # for num, freq in num_frequencies.items():
        #     heappush(min_heap, (freq, num))
        #     if len(min_heap) > k:
        #         heappop(min_heap)
        
        # top_k_frequent = [pair[1] for pair in min_heap]

        # return top_k_frequent
