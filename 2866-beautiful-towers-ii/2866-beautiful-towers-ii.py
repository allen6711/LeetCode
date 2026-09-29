class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        max_sum = 0
        n = len(maxHeights)
        left = [0] * n
        stack = []
        for i in range(n):
            while stack and maxHeights[stack[-1]] > maxHeights[i]:
                stack.pop()
            
            # Only
            if stack:
                j = stack[-1]
                left[i] = left[j] + maxHeights[i] * (i - j)
            
            # 左邊全部比當筆高(All elements on the left are higher than the current one)
            else:
                left[i] = maxHeights[i] * (i + 1)
            stack.append(i)
        
        right = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and maxHeights[stack[-1]] > maxHeights[i]:
                stack.pop()
            
            if stack:
                j = stack[-1]
                right[i] = right[j] + maxHeights[i] * (j - i)
            
            else:
                right[i] = maxHeights[i] * (n - i)
            stack.append(i)
        
        for i in range(n):
            max_sum = max(max_sum, left[i] + right[i] - maxHeights[i])
        
        return max_sum

















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