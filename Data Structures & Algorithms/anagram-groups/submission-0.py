class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort = {}
        for i in strs: 
            if "".join(sorted(i)) not in sort:
                sort["".join(sorted(i))] = []
            sort["".join(sorted(i))].append(i)
        
        return list(sort.values())


        
         