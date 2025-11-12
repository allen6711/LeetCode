class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sort_car = sorted(zip(position, speed), key = lambda x: -x[0])
        stack = []
        fleets = 0
        max_time = 0

        for pos, spd in sort_car:
            time = (target - pos) / spd
            if not stack or time > max_time:
                stack.append(time)
                max_time = time
                fleets += 1
        
        return fleets