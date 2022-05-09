class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        '''BRUTE FORCE SOLUTION WITH O(n2) time complexity'''
        '''
        maxArea = 0
        
        #create nested loop, first loop with index i, inner loop with index j
        #outer loop starts at 0, and the inner loop starts at i+1
        
        for i in range(0, len(height)):
            for j in range(i+1, len(height)):
                #find the area area = max(maxArea, min(height[i], height[j]) * (j-i))
                area = (j-i) * min(height[i], height[j])
                maxArea = max(area, maxArea)
                
        return maxArea
        '''
        
        '''LINEAR TIME SOLUTION'''
        maxArea = 0
        #initialize the left and right pointers
        l, r = 0, len(height) -1 
        
        while l < r:
            area = (r-l) * min(height[l], height[r])
            maxArea = max(maxArea, area)
            
            #move the pointers
            if height[l] < height[r]:
                l += 1
            else:
                 r -= 1
        return maxArea
