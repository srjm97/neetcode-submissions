class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if len(s) != len(t):
            return False
        n = len(s)
        for i in range(n):
            freq[s[i]] = freq.get(s[i], 0) + 1
            freq[t[i]] = freq.get(t[i], 0) - 1
        for key in freq.keys():
            if freq[key] != 0:
                return False
        return True