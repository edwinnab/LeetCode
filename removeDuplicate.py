"""
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #empty stack
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] +=1
            else:
                stack.append([char, 1])
            if stack and stack[-1][1] == k:
                stack.pop()
        return ''.join([char[0]*char[1] for char in stack])        
         
