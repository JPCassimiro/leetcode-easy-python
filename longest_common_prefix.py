class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if (len(strs) == 0 or strs == None):
            return ""
        
        ret = ""

        sorted_strs = sorted(strs)
        first_str = sorted_strs[0]
        last_str = sorted_strs[-1]
        for idx in range(min(len(first_str),len(last_str))):
            if(first_str[idx] != last_str[idx]):
                return ret
            ret += first_str[idx]

        return ret

       