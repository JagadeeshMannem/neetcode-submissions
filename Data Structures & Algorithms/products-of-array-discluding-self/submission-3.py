import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        holder = []
        
        for i in range(len(nums)):
                leftSet = nums[:i]
                leftProd = math.prod(leftSet)

                rightSet = nums[(i+1):]
                rightProd = math.prod(rightSet)

                holder.append(leftProd * rightProd)

        return holder