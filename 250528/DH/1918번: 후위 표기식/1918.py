x = input().strip()
stack = []
result = []

def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return 0

for token in x:
    if token.isalpha():
        result.append(token)
    elif token == '(':
        stack.append(token)
    elif token == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()
    else:
        while stack and precedence(stack[-1]) >= precedence(token):
            result.append(stack.pop())
        stack.append(token)

while stack:
    result.append(stack.pop())

print(''.join(result))
