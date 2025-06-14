# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def update(sign):
            n2,n1=stack.pop(),stack.pop()
            if sign=="+": return n1+n2
            if sign=="-": return n1-n2
            if sign=="*": return n1*n2
            if sign=="/": return int(n1/n2)
			
        stack=[]
        
        for n in tokens:
            if n.isdigit() or len(n)>1:
                stack.append(int(n))
            else:
                stack.append(update(n))
        return stack.pop()