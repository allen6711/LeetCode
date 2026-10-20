class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        ans = set()
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    
                    if digits[k] % 2 == 0:
                        num = 100 * digits[i] + 10 * digits[j] + digits[k]
                        ans.add(num)
        
        return len(ans)


















        # O(n*2^n)
        # O(n)
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