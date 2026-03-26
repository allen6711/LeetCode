class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        start = 0
        tank = 0
        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start
        # O(n^2)
        # O(1)
        # n = len(gas)
        # for start in range(n):
        #     tank = 0
        #     completed = True

        #     for step in range(n):
        #         i = (start + step) % n
        #         tank += gas[i]
        #         tank -= cost[i]

        #         if tank < 0:
        #             completed = False
        #             break
        #     if completed:
        #         return start
        # return -1
        # O(n)
        # O(1)
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        start = 0
        tank = 0

        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start

            
