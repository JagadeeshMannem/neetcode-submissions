class Solution:
    def topKValues(self, valueList: List[int], k: int) -> List[int]:
        valueList.sort(reverse = True)
        return valueList[:k]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        holder = {}

        numsLen = len(nums)
        for i in range(numsLen):
            if nums[i] in holder.keys():
                holder[nums[i]] += 1
            else:
                holder[nums[i]] = 1
        
        topK = self.topKValues(list(holder.values()), k)

        sol = []

        sol = [keyH for keyH, valueH in holder.items() if valueH in topK]

        return sol