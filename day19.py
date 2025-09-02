def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()  
    
    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):  
           
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
               
                stack.append(int(a / b))
    
    return stack[0]

expr = "2 1 + 3 *"
print(evaluate_postfix(expr))
