class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_list = ['^']
        for letter in s:
            s_list.append(letter)
        s_list.append('$')
        new_s = '#'.join(s_list)

        n = len(new_s)
        P = [0] * n
        C = 0
        R = 0
        for i in range(1, n - 1):
            i_mirror = 2 * C - i
            if (R > i):
                P[i] = min(R - i, P[i_mirror])
            else:
                P[i] = 0
            while(new_s[i + P[i] + 1] == new_s[i - P[i] - 1]):
                P[i] += 1
            i += 1

            if R < i + P[i]:
                C = i
                R = P[i]
        max_len = 1
        cen = 1
        for i in range(1, n - 1):
            if P[i] > max_len:
                max_len = P[i]
                cen = i

        start = (cen - max_len) // 2
        end = start + max_len
        return s[start: end]
