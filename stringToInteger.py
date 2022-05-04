class Solution:
    def myAtoi(self, s: str) -> int:
        
        MAX_INT = 2**31 -1
        MIN_INT = -2**31
        
        
        i=0
        res = 0
        negative = 1
        
        #whitespaces
        while i < len(s) and s[i] == " ":
            i += 1
        #check for +, - symbols
        
        if i < len(s) and s[i] == "-":
            i += 1
            negative = -1
        elif i < len(s) and s[i] == "+":
            i += 1
        
        #check for digits
        checker = set('0123456789')
        while i < len(s) and s[i] in checker:
            res = res*10 + int(s[i])
            i += 1
            
        #check for the Max and the Min
        
        res = res * negative
        if res < 0:
            return max(res, MIN_INT)
        return min(res, MAX_INT)
            
