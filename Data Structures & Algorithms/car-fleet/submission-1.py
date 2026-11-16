class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)  # closest to target first
        stack = []

        for p, s in pair:
            stack.append((target - p) / s)  # time to reach target
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # catches the fleet ahead, so merge

        return len(stack)