class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        # O(n)
        # O(n)
        n = len(maxHeights)

        left = [0] * n
        stack = []

        # left
        for i in range(n):
            while stack and maxHeights[stack[-1]] > maxHeights[i]:
                stack.pop()
            
            if stack:
                j = stack[-1]
                left[i] = left[j] + (i - j) * maxHeights[i]
            else:
                left[i] = (i + 1) * maxHeights[i]
            
            stack.append(i)
        
        # right
        right = [0] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and maxHeights[stack[-1]] > maxHeights[i]:
                stack.pop()
            
            if stack:
                j = stack[-1]
                right[i] = right[j] + (j - i) * maxHeights[i]
            else:
                right[i] = (n - i) * maxHeights[i]

            stack.append(i)
        
        ans = 0

        for i in range(n):
            ans = max(ans, left[i] + right[i] - maxHeights[i])
        
        return ans
        # O(n^2)
        # O(1)
        n = len(maxHeights)
        ans = 0

        for peak in range(n):
            total = maxHeights[peak]

            # to left
            current = maxHeights[peak]

            for i in range(peak - 1, -1, -1):
                current = min(current, maxHeights[i])
                total += current
            
            # to right
            current = maxHeights[peak]

            for i in range(peak + 1, n):
                current = min(current, maxHeights[i])
                total += current
            
            ans = max(ans, total)
        
        return ans