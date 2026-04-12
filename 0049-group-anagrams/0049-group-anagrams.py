class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        
        for s in strs:
            freq=[0]*26
            for ch in s:
                freq[ord(ch)-ord('a')]+=1
            res[tuple(freq)].append(s)
        
        return list(res.values())

