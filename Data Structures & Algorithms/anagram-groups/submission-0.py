class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            arr=[0]*26
            for j in i:
                arr[ord(j)-ord('a')] += 1
            key=tuple(arr)
            if key not in anagrams:
                anagrams[key]=[]
            anagrams[key].append(i)
        return list(anagrams.values())

                
        
        