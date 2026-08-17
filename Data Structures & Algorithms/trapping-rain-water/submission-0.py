class Solution:
    def trap(self, height: List[int]) -> int:
        result=0
        stack=[]
        for i in range(len(height)):
            while stack and height[stack[-1]]<height[i]:
                pop_height=height[stack.pop()]

                if not stack:
                    break;
                distance=i-stack[-1]-1
                water=min(height[stack[-1]],height[i])
                water-=pop_height
                result+=distance*water
            stack.append(i)
        return result
        