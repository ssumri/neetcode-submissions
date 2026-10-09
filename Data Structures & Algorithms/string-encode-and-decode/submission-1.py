class Solution:

    def encode(self, strs: List[str]) -> str:
        finalstr = ''
        for i in range(len(strs)):
            finalstr += str(len(strs[i]))
            finalstr += '#'
            finalstr += strs[i]
        return finalstr

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # go beyond the hashtag
            i = j + 1
            strs.append(s[i:i+length])
            i += length
        return strs



