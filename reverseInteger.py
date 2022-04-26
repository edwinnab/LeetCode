class Solution:
    def reverse(self, x: int) -> int:
        #convert the integer into a string
        #sorts it's absolute zero
        y = str(abs(x))
        print(y)
        #strip the string, this remove all the leading spaces
        y = y.strip()
        #reverse the string
        y = y[::-1]
        
        #convert the str to int and store the result in a new variable
        ans = int(y)
        
        #check if the ans is in the given range
        if ans >= 2**31 -1 or ans <= -2** 31:
            return 0
        elif x < 0:
            return -1 * ans
        else:
            return ans
        
        
        
