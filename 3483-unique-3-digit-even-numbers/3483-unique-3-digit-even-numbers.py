class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = set()
        n = len(digits)
        visited = [False] * n
        path = []

        def backtrack():
            if len(path) == 3:
                if path[2] % 2 == 0:
                    num = path[0] * 100 + path[1] * 10 + path[2]
                    ans.add(num)
                return
            
            for i in range(n):
                if visited[i]:
                    continue

                if len(path) == 0 and digits[i] == 0:
                    continue
                
                visited[i] = True
                path.append(digits[i])
                backtrack()
                path.pop()
                visited[i] = False

        backtrack()

        return len(ans)