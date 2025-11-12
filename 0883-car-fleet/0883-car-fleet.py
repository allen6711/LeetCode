class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        car_sort = sorted(zip(position, speed), key = lambda x: -x[0])
        fleets = 0

        for pos, spd in car_sort:
            time = (target - pos) / spd

            if not stack or time > stack[-1]:
                stack.append(time)
                fleets += 1
        
        return fleets

        # sort_car = sorted(zip(position, speed), key = lambda x: -x[0])
        # stack = []
        # fleets = 0
        # max_time = 0

        # for pos, spd in sort_car:
        #     time = (target - pos) / spd
        #     if not stack or time > max_time:
        #         stack.append(time)
        #         max_time = time
        #         fleets += 1
        
        # return fleets