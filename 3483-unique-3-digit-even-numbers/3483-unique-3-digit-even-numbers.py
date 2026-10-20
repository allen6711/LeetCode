class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # Enumeration + Frequency Counting
        # O(n) + O(K) = O(n)
        # O(K) = O(1)
        count = [0] * 10
        for digit in digits:
            count[digit] += 1
        
        ans = 0

        for num in range(100, 1000, 2):
            required = [0] * 10
            x = num

            for _ in range(3):
                required[x % 10] += 1
                x //= 10
            
            if all(required[d] <= count[d] for d in range(10)):
                ans += 1
        
        return ans

        # Brute Force
        # O(n^3)
        # O(K) = O(1)
        # n = len(digits)
        # ans = set()
        # for i in range(n):
        #     if digits[i] == 0:
        #         continue
        #     for j in range(n):
        #         if j == i:
        #             continue
        #         for k in range(n):
        #             if k == i or k == j:
        #                 continue
                    
        #             if digits[k] % 2 == 0:
        #                 num = 100 * digits[i] + 10 * digits[j] + digits[k]
        #                 ans.add(num)
        
        # return len(ans)
        # O(n^3)
        # O(n) -> 因為visited
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