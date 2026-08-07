class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        temp = ""
        largest = ""  

        while right < len(s):
            temp = s[left:right]

            while s[right] in temp:
                left += 1
                temp = s[left:right]
            
            right += 1
            temp = s[left:right]

            if len(temp) > len(largest):
                largest = temp
            
            


        return len(largest)