class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map1 = {}
        map2 = {}

        len1 = len(s)
        len2 = len(t)

        for i in range(len1):
            if s[i] in map1:
                map1[s[i]] += 1
            else:
                map1[s[i]] = 1
         
        for i2 in range(len2):
            if t[i2] in map2:
                map2[t[i2]] += 1
            else:
                map2[t[i2]] = 1
        
        return map1 == map2
        
