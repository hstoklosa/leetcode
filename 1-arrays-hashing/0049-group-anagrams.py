from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupsMap = dict()
        
        for s in strs:
            key = "".join(sorted(s))
            
            if (key not in groupsMap): 
                groupsMap[key] = []

            groupsMap[key].append(s)

        return list(groupsMap.values())