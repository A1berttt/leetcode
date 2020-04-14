class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_dict = dict()
        s_len = len(s)
        ret = 0
        i = 0
        j = 0
        while j < s_len:
            if s[j] in ch_dict:
                i = max(i, ch_dict[s[j]])
            ret = max(ret, j - i + 1)
            ch_dict[s[j]] = j + 1
            j += 1
        return ret
