class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # O((n+q)logn)
        # O(nlogn)
        # pairs[pos] = (value, original node index)
        pairs = sorted((nums[i], i) for i in range(n))
        values = [value for value, _ in pairs]

        # position[node] = the node's position after sorting
        position = [0] * n

        for pos, (_, original_node) in enumerate(pairs):
            position[original_node] = pos
        
        LOG = n.bit_length()
        # jump[pos][k] stores the farthest sorted position
        # reachable from pos after 2^k greedy jumps
        jump = [[0] * LOG for _ in range(n)]

        # Use two pointers to find the farthest position
        # reachable from each position in one step
        right = 0

        for left in range(n):
            right = max(right, left)

            while (
                right + 1 < n
                and values[right + 1] - values[left] <= maxDiff
            ):
                right += 1
            jump[left][0] = right
        
        # Build the binary lifting table
        for k in range(1, LOG):
            for i in range(n):
                middle = jump[i][k - 1]
                jump[i][k] = jump[middle][k - 1]
        
        answer = []

        for u, v in queries:
            left = position[u]
            target = position[v]

            # Since the graph is undirected, always process from left to right
            if left > target:
                left, target = target, left

            # The distance from a node to itself is zero
            if left == target:
                answer.append(0)
                continue
            
            current = left
            steps = 0

            # Take the largest possible jumps without reaching the target
            for k in range(LOG - 1, -1, -1):
                next_position = jump[current][k]

                if next_position < target:
                    current = next_position
                    steps += 1 << k

            # Check whether one final jump can reach the target
            if jump[current][0] >= target:
                answer.append(steps + 1)
            else:
                answer.append(-1)
        
        return answer
        
