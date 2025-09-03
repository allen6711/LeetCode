class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        graph = self.build_graph(sequences)
        topo_order = self.topological_sort(graph)

        return topo_order == nums

    def build_graph(self, sequences):
        graph = defaultdict(list)

        for seq in sequences:
            for char in seq:
                graph[char] = set()
        
        for seq in sequences:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])
        
        return graph
    
    def get_indegree(self, graph):
        indegrees = {
            node: 0
            for node in graph
        }

        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
        
        return indegrees

    def topological_sort(self, graph):
        indegrees = self.get_indegree(graph)

        topo_order = []
        queue = [node for node in graph if indegrees[node] == 0]

        while queue:
            if len(queue) > 1:
                return False

            node = queue.pop()
            topo_order.append(node)

            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(topo_order) == len(graph):
            return topo_order
        
        return None
        