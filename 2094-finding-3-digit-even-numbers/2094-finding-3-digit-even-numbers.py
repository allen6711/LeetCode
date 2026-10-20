class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        # O(n(n-1)(n-2) + KlogK) 最多是K=450種數字(9*10*5)
        # O(n^3)
        # O(n+K)
        # O(n)
        # path = []
        # ans = set()   # O(K)
        # n = len(digits)
        # visited = [False] * n   # O(n)
        # def backtrack():
        #     if len(path) == 3:
        #         if path[0] != 0  and path[2] % 2 == 0:
        #             num = 100 * path[0] + 10 * path[1] + path[2]
        #             ans.add(num)
        #         return
            
        #     for i in range(n):
        #         if visited[i]:
        #             continue
        #         path.append(digits[i])
        #         visited[i] = True
        #         backtrack()
        #         path.pop()
        #         visited[i] = False
        
        # backtrack()

        # return sorted(ans)
        # Brute Force + Hash Set
        # O(n^3)
        # O(K) = O(1)
        ans = set()
        n = len(digits)
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    
                    if digits[k] % 2 != 0:
                        continue
                    
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    ans.add(num)

        return sorted(ans)