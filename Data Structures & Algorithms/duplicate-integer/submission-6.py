class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        holder = set()
        len1 = len(nums)
        while len(nums) != 0:
            holder.add(nums.pop(0))
        len2 = len(holder)
        return len1 != len2