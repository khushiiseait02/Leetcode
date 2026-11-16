class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        dict={}
        left=0
        right=0
        maxi=0
        while right<n:
            if s[right] in dict:
                left=max(left,dict[s[right]]+1)

            maxi=max(maxi,right-left+1)
            dict[s[right]]=right
            right+=1
        return maxi