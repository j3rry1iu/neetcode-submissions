class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSet = list(s)
        tSet = list(t)
        if sorted(sSet) == sorted(tSet): 
            return True
        else: 
            return False
        