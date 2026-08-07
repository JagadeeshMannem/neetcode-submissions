class Solution:
    def isValid(self, s: str) -> bool:
        stack = [];
        close = {')':'(', '}':'{', ']':'['}

        isValidPar = False

        for i in s:
            if i in close:
                if stack and stack[-1]==close[i]:
                    stack.pop()
                else:
                    return isValidPar
            else:
                stack.append(i)
        
        if len(stack) == 0:
            isValidPar = True

        return isValidPar