# Recursive solution of RPN in Python 3 
# Author Shwetank Kumar
def rpn(exp):
    n = len(exp)
    p = 0
    op = ['+','-','*','/','^']
    if n == 1:
        return exp
    for i in range(n):
        k = n-i-1
        if exp[k]=='(':
            p+=1
        elif exp[k] == ')':
            p-=1
        if p==0 and exp[k] in op:
            part1 = exp[:k]
            optr = exp[k]
            part2= exp[k+1:]
            return rpn(part1)+rpn(part2) + optr
    if exp[0] == '(' and exp[n-1]==')':
        return rpn(exp[1:-1])

t = int(input())
for i in range(t):
    print(rpn(input()))
    
            
            
        
        
     3
