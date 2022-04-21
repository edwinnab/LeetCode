class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        #lets get the longest substring
        #initialize an empty string
        
        emptyStr = ""
        maxlen = 0
        
        #traverse the s
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                word = s[i:j] #allows us to print all the substrings
                print(word)
                if(word == word[::-1]):
                    if(maxlen < len(word)):
                        maxlen = len(word)
                        emptyStr=word
        return emptyStr
        '''
        #declare a string to hold the final result
        finalStr = ""
        
        #traverse the string
        for i in  range(len(s)):
            #check for odd palindromes and initialize a pointer
            odd = self.palindrome(s,i,i)
            #check for even, has two unique characters
            even = self.palindrome(s,i, i+1)
            
            finalStr = max(odd, even, finalStr, key=len)
            
        return finalStr
    #define an helper function for palindrome
    def palindrome(self, s, left, right):
        while(0 <= left and right < len(s)) and (s[left] == s[right]):
            #increment the right and decrement the left
            left -= 1
            right += 1
        return s[left+1:right]
        
