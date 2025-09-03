class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = self.build_graph(words)

        if not graph:
            return ""

        return self.topological_sort(graph)

    def build_graph(self, words):
        graph = {}

        # to create node dict with neighbor
        for word in words:
            for c in word:
                # avoid duplicate
                if c not in graph:
                    graph[c] = set()

        # add edges (neighbor)
        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break
                if j == min(len(words[i]), len(words[i + 1])) - 1:
                    if len(words[i]) > len(words[i + 1]):
                        return None
        
        return graph
    
    def topological_sort(self, graph):
        indegree = {
            node: 0
            for node in graph
        }

        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1

        queue = [node for node in graph if indegree[node] == 0]
        heapify(queue)
        order = ""

        while queue:
            node = heappop(queue)
            order += node

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heappush(queue, neighbor)

        return order if len(order) == len(graph) else ""