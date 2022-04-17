class Solution:
    def isValid(self, s: str) -> bool:
        
        '''
        #Brute force solution
        if "()" in s:
            return True
        elif "[]" in s:
            return True
        elif "{}" in s:
            return True
        else:
            return False
        '''
        
        # using a dict and stack 
        #declare a dict
        
        if len(s) % 2 != 0:
            return False
        
        dict = {"(":")", "{":"}", "[":"]"}
        stack = []
        
        #traverse the string
        for char in s:
            if char in dict.keys():
                stack.append(char)
            else:
                if stack == []:
                    return False
                ans = stack.pop()
                print(ans)
                if char != dict[ans]:
                    return False
        return stack == []
    
        
       
        
