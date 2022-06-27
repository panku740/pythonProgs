def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = defaultdict(list)
        for i in strs:
            #print(i,sorted(i))
            ky = ''.join(sorted(i))
            
            l[ky].append(i)

        return list(l.values())

""" Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]"""