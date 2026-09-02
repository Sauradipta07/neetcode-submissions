class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]
        st=[]
        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        cars.sort(reverse=True)
        for position, speed in cars:
            time=((target-position)/(speed))
            if not st or time>st[-1]:
                st.append(time)
        return len(st)

