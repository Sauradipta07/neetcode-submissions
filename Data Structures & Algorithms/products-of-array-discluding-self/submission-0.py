class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        count=0
        for num in range(len(nums)):            
            if nums[num] == 0:
                count+=1
                continue
            product=product*nums[num]

        
        final=[]

        if count == 0:
            for num in range(len(nums)):
                final.append(int(product/nums[num]))

        elif count == 1:
            for num in range (len(nums)):
                if nums[num] == 0:
                    final.append(int(product))
                else:
                    final.append(0)
        else:
            for num in range (len(nums)):
                final.append(0)
            
        return final
        