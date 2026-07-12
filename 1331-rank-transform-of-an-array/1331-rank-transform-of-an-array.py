class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # O(nlogn)
        # O(n)
        sorted_value = sorted(set(arr))
        rank = {}
        answer = []
        for index, value in enumerate(sorted_value):
            rank[value] = index + 1
        
        for value in arr:
            answer.append(rank[value])
        
        return answer