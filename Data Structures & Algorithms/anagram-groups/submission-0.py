class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps={}
        for i in strs:
            sot="".join(sorted(i))
            if sot in grps:
                grps[sot].append(i)
            if sot not in grps:
                grps[sot]=[i]
        return list(grps.values())
