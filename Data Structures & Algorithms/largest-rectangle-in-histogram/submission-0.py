class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonic stack -> for each bar, calculate until reaching maximum gird
        # O(heights.length) * O(heights.length)
        # optimize?
        # stack in increasing order
        # if enounter lower one, calculate the area size
        # update start idx: low long the x-axis is
        # stack: [start index, height]
        N = len(heights)
        maximum = 0
        stack = []
        for i in range(N):
            start = i
            while len(stack) > 0 and stack[-1][1] > heights[i]:
                prev_start, prev_h = stack.pop()
                area = prev_h * (i - prev_start)
                maximum = max(maximum, area)
                start = prev_start

            stack.append((start, heights[i]))
        
        # the rest keeps in increasing order
        while stack:
            prev_start, prev_h = stack.pop()
            area = prev_h * (N - prev_start)
            maximum = max(maximum, area)

        return maximum