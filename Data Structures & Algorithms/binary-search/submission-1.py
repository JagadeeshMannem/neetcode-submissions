class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            # Calculate the true midpoint index
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Target is in the right half, shift the left pointer
                left = mid + 1
            else:
                # Target is in the left half, shift the right pointer
                right = mid - 1
                
        return -1