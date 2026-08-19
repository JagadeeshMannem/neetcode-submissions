import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum = math.prod(nums)
        result = []

        if sum != 0:
            for i in range(len(nums)):
                result.append(int(sum/nums[i]))
        else:
            for i in range(len(nums)):
                if nums[i] == 0:
                    result.append(int(math.prod(nums[0:i]) * math.prod(nums[(i+1):len(nums)])))
                else:
                    result.append(0)
        
        return result
