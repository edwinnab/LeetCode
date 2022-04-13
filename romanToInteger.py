class Solution:
    def romanToInt(self, s: str) -> int:
        #define a dict to hold the roman key:value
        dict = {"I":1, "V":5, "X":10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        #variable to hold the total
        p = 0
        total = 0
        n = len(s)
        #split the roman string
        # example s="III", "I, I, I"
        #then get the value
        
        
        for char in range(n-1, -1, -1): 
            #check if the current value is greter than the previous value
            #add it to the total, otherwise do a subtraction
            if (dict[s[char]] >= p):
                total += dict[s[char]]
            else:
                total -= dict[s[char]]
            p = dict[s[char]]
        print(total)
        return total
    
        
