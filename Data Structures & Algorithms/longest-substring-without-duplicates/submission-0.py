class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        window_len = len(s)
        longSub = ""
        temp = ""

        while right < window_len:
            temp = s[left:right]
            
            while s[right] in temp:
                left += 1
                temp = s[left:right] 
            
            right += 1
            temp = s[left:right]
            
            if len(temp) > len(longSub):
                longSub = temp
            
        
        return len(longSub)