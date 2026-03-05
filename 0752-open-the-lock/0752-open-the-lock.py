class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # O(10^4)
        # O(10^4)
        dead = set(deadends)
        
        # If the start is blocked, we cannot move at all
        if "0000" in dead:
            return -1
        
        q = deque([("0000", 0)])
        visited = set("0000")

        while q:
            state, steps = q.popleft()
            if state == target:
                return steps
            
            for i in range(4):
                digit = int(state[i])

                for move in (-1, 1):
                    new_digit = (digit + move) % 10
                    neighbor = state[:i] + str(new_digit) + state[i + 1:]
                    
                    if neighbor in dead:
                        continue
                    if neighbor in visited:
                        continue
                    
                    visited.add(neighbor)
                    q.append((neighbor, steps + 1))
        return -1
