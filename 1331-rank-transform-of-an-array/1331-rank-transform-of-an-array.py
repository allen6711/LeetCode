class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        rank_dict = {}

        for index, value in enumerate(sorted_arr):
            rank_dict[value] = index + 1
        
        answer = []
        for value in arr:
            answer.append(rank_dict[value])
        
        return answer













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