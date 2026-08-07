class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]

        holder = {}

        for i in range(len(strs)):
            if tuple(sorted(strs[i])) in holder:
                holder[tuple(sorted(strs[i]))].append(strs[i])
            else:
                holder[tuple(sorted(strs[i]))] = [strs[i]]
        
        return list(holder.values())

            