class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]

        holder = {}

        for i in range(len(strs)):
            if tuple(sorted(strs[i])) in holder:
                holder[tuple(sorted(strs[i]))].append(i)
            else:
                holder[tuple(sorted(strs[i]))] = [i]
        
        sol = []
        
        for key in holder:
            sol.append([strs[i] for i in range(len(strs)) if i in holder[key]])

        return sol

            