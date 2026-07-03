class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        max_cost = 0

        for u, v, cost in edges:
            # offline nodes cannot be used in a valid path
            if not online[u] or not online[v]:
                continue

            graph[u].append((v, cost))
            max_cost = max(max_cost, cost)

        def can(score: int) -> bool:
            dist = [math.inf] * n
            dist[0] = 0

            heap = [(0, 0)]  # (total_cost, node)

            while heap:
                curr_cost, node = heapq.heappop(heap)

                if curr_cost > dist[node]:
                    continue

                if curr_cost > k:
                    return False

                if node == n - 1:
                    return True

                for nei, edge_cost in graph[node]:
                    if edge_cost < score:
                        continue

                    new_cost = curr_cost + edge_cost

                    if new_cost < dist[nei] and new_cost <= k:
                        dist[nei] = new_cost
                        heapq.heappush(heap, (new_cost, nei))

            return False

        left, right = 0, max_cost
        answer = -1

        while left <= right:
            mid = (left + right) // 2

            if can(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer