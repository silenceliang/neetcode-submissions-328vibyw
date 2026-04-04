class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(zip(position, speed), key=lambda x: -x[0])
        time = [(target-p)/s for p,s in pos_speed]
        stack = []
        for i in range(len(time)):
            if len(stack) == 0 or stack[-1] < time[i]:
                stack.append(time[i])

        return len(stack)