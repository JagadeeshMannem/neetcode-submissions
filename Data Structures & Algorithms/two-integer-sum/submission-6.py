class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            #n is the value, not the index
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i