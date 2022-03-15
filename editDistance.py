class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #variable to rep the length of the words
        x = len(word1)
        y = len(word2)
        
        # empty strings, 
        if (x == 0 and y == 0):
            return 0
        # one string is empty while the other is not
        #word1 = " " word2 = "ggsfd" len(word2)
        if (x == 0 and y > 0):
            return y
        #word = "ggsfd" word2 = " "
        if(x > 0 and y == 0):
            return x
        
        arr = [[0 for k in range(y+1)] for l in range(x+1)]
        for i in range(1, x+1):
            arr[i][0] = i
        for j in range(1,y+1):
            arr[0][j] = j
            
        #last char different
        for i in range(1, x+1):
            for j in range(1, y+1):
                if(word1[i-1] == word2[j-1]):
                    count = 0
                else:
                    count = 1
                arr[i][j] = min(arr[i-1][j] + 1, arr[i][j-1] + 1, arr[i-1][j-1] + count)
        return arr[x][y]
