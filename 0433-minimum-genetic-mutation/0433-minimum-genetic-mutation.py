class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)

        if endGene not in bank_set:
            return -1
        
        genes = ["A", "C", "G", "T"]

        q = deque([(startGene, 0)])
        visited = set([startGene])

        while q:
            cur, steps = q.popleft()
            if cur == endGene:
                return steps
            
            for i in range(len(cur)):
                for ch in genes:
                    if ch == cur[i]:
                        continue
                    
                    next_gene = cur[:i] + ch + cur[i + 1:]
                    if next_gene not in bank_set:
                        continue

                    if next_gene in visited:
                        continue
                    
                    visited.add(next_gene)
                    q.append((next_gene, steps + 1))
        
        return -1