class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for idx in range(len(haystack)):
            if haystack[idx] == needle[0]:
                _check = haystack[idx:(idx+len(needle))]
                if _check == needle:
                    return idx
        
        return -1