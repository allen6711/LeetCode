class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_value = sorted(set(arr))
        rank = {}
        answer = []
        for index, value in enumerate(sorted_value):
            if value not in rank:
                rank[value] = index + 1
        
        for value in arr:
            answer.append(rank[value])
        
        return answer


