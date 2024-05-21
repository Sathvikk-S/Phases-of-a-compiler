OPERATORS = set(['+', '-', '*', '/', '(', ')','%', '^'])  # set of operators
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '%':2,'^':3} # dictionary having priorities 

def infix_to_postfix(expression): #input expression
    stack = [] # initially stack empt
    output = '' # initially output empty
    
    for ch in expression:
        if ch not in OPERATORS:  # if an operand then put it directly in postfix expression
            output+= ch
        elif ch=='(':  # else operators should be put in stack
            stack.append('(')
        elif ch==')':

            while stack and stack[-1]!= '(':

                output+=stack.pop()

            stack.pop()

        else:

            # lesser priority can't be on top on higher or equal priority    

             # so pop and put in output   

            while stack and stack[-1]!='(' and PRIORITY[ch]<=PRIORITY[stack[-1]]:

                output+=stack.pop()

            stack.append(ch)

    while stack:

        output+=stack.pop()

    return output

 
def PostfixResult(expr):    
    post=infix_to_postfix(expr)
    stack=[]
    for i in post:
        if i.isnumeric():
            stack.append(i) 
        elif i=="*":
            stack.append(int(stack.pop())*int(stack.pop()))              
        elif i=="+":
            stack.append(int(stack.pop())+int(stack.pop()))               
        elif i=="-":
            first=int(stack.pop())
            second=int(stack.pop())
            stack.append(second-first)               
            
        elif i=="/":
            first=int(stack.pop())
            second=int(stack.pop())
            stack.append(second/first)               
           
           
        elif i=="%":
            first=int(stack.pop())
            second=int(stack.pop())
            stack.append(second%first)               
           
    return stack

