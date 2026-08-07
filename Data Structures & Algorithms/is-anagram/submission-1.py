class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counterS = {}
        counterT = {}

        for i in range(len(t)):
            if s[i] in counterS:
                counterS[s[i]] += 1
            else:
                counterS[s[i]] = 1
            if t[i] in counterT:
                counterT[t[i]] += 1
            else:
                counterT[t[i]] = 1
        
        return counterS == counterT 
