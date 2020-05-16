class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        if not heights:
            return 0

        stack = []
        area = 0
        i = 0
        heights.append(0)

        while i<len(heights):
            if not stack or heights[stack[-1]]<heights[i]:
                stack.append(i)
            else:

                while stack and heights[stack[-1]]>heights[i]:
                    top = stack.pop()

                    if not stack:
                        width = i
                    else:
                        width = i-stack[-1]-1
                    area = max(area, width*heights[top])
                stack.append(i)
            i+=1

        return area
