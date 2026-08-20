class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strset=set()
        left=0
        result=0
        for right in range(len(s)):
            while s[right] in strset:
                strset.remove(s[left])
                left+=1
            strset.add(s[right])
            result=max(result,right-left+1)
        return result

            



