class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sub=set(nums)
        longest=0
        for num in sub:
            if num-1 not in sub:
                current = num
                count=1                
                while current+1 in sub:
                    count+=1
                    current+=1
                longest=max(longest,count)
        return longest