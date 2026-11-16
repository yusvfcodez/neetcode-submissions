class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  # closest to target first
        fleets = 0
        slowest_time = 0  # time of the fleet ahead

        for pos, spd in cars:
            time = (target - pos) / spd
            if time > slowest_time:  # can't catch the fleet ahead
                fleets += 1
                slowest_time = time

        return fleets