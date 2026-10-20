class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        path = []
        ans = set()
        n = len(digits)
        visited = [False] * n
        def backtrack():
            if len(path) == 3:
                if path[0] != 0  and path[2] % 2 == 0:
                    num = 100 * path[0] + 10 * path[1] + path[2]
                    ans.add(num)
                return
            
            for i in range(n):
                if visited[i]:
                    continue
                path.append(digits[i])
                visited[i] = True
                backtrack()
                path.pop()
                visited[i] = False
        
        backtrack()

        return sorted(ans)