class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]
        cars.sort()
        stack = []
        stack.append(cars[-1])
        for i in range(len(cars)-2, -1, -1):
            stack.append(cars[i])
            p1, s1 = stack[-1]
            p2, s2 = stack[-2]
            if (target-p1)/s1 <= (target-p2)/s2:
                stack.pop()
        return len(stack)
            