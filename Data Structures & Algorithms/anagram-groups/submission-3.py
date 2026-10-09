class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash where keys are sorted names
        keywords = {}
        fin = []
        
        for i in range(len(strs)):
            sword = tuple(sorted(strs[i]))
            if sword in keywords:
                keywords[sword].append(strs[i])
            else:
                keywords[sword] = [strs[i]]
        
        for key in keywords:
            fin.append(keywords[key])
        
        return fin


    

        