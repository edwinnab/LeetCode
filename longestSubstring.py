class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #declare two variables
        emptyStr ="" #abca
        maxLen = 0
        
        #traverse the whole string
        for i in range(len(s)):
            if s[i] in emptyStr:
                index = emptyStr.index(s[i]) #set the start position
                emptyStr = emptyStr[index+1:i]
            emptyStr += s[i]
            print(emptyStr)
            if maxLen < len(emptyStr):
                maxLen = len(emptyStr)
        return maxLen
