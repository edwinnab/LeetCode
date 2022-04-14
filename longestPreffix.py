class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #initialize the longest common preffix to empty
        lcp = ""
        #check for the edge case
        if strs is None or len(strs == 0):
            return lcp
        #find the shortest string length in the array
        short = len(min(strs, key=len))
        
        for i in range(0, short):
            #get the current char from the first string
            current = strs[0][i]
            for j in range(0, len(strs)):
                #check if the char is found in all the other strings
                if strs[j][i] != current:
                    return lcp
            lcp += current
        return lcp
        
