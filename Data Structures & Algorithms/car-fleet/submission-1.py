class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(zip(position, speed), key=lambda x: -x[0])
        time = [(target-p)/s for p,s in pos_speed]
        stack = []
        for t in time:
            if len(stack) == 0 or stack[-1] < t:
                stack.append(t)

        return len(stack)