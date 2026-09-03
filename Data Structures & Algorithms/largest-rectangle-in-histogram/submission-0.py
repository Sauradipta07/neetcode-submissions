class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        st = []
        max_area = 0
        n = len(heights)

        for i in range(n):

            while st and heights[i] < heights[st[-1]]:
                topid = st.pop()

                if not st:
                    width = i
                else:
                    width = i - st[-1] - 1

                max_area = max(max_area, width * heights[topid])

            st.append(i)

        # Process remaining bars
        while st:
            topid = st.pop()

            if not st:
                width = n
            else:
                width = n - st[-1] - 1

            max_area = max(max_area, heights[topid] * width)

        return max_area