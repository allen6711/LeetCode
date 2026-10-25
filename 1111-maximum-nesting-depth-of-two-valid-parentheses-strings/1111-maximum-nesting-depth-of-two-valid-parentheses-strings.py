class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        # Greedy + Depth Parith
        # O(n)
        # O(n)
        depth = 0
        ans = []

        for char in seq:
            if char == "(":
                depth += 1
                ans.append(depth % 2)
            else:
                ans.append(depth % 2)
                depth -= 1
        
        return ans