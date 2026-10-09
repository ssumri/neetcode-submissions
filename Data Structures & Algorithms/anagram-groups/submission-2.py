class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # try hash map solution 
        # for each word in array
        ret = []
        hashWords = []
        for word in strs:
            wordi = {}
            
            # w is the key (character) while count will be the value that counts number of letters
            for count, w in enumerate(word):
                # if the key is already in the map, update value of count
                if w in wordi: 
                    wordi[w] = wordi[w] + 1
                else: # if not create a new key
                    wordi[w] = 1
            # add map to the list of maps
            hashWords.append(wordi)
        # all words are hashed and put into the key

        # edge case if theres only one/no value
        if len(hashWords) <= 1:
            return [strs]

        count = 0
        skipIndex = []
        while count < len(hashWords):
            #skips index of values already in arr
            if count in skipIndex: 
                count += 1
                continue

            sets = []
            sets.append(strs[count]) 
            skipIndex.append(count)
            # print("added starting to look for duplicates")

            for j in range(count + 1, len(hashWords)):
                if hashWords[count] == hashWords[j]:
                    sets.append(strs[j])
                    skipIndex.append(j)
                    # print("found match")
                    # hashWords.pop(i)
                j += 1

            # hashWords.pop(0)
            count += 1
            ret.append(sets)
            
        return ret    
        