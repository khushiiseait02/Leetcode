class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            substr = haystack[i : i + len(needle)]

            if substr == needle:
                return i

        return -1