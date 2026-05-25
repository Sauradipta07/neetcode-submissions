class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charcount={}
        for i in s :
            charcount[i]=charcount.get(i,0)+1
        for j in t:
            charcount[j]=charcount.get(j,0)-1
        for k in charcount.values():
            if k !=0:
                return False
        return True
        