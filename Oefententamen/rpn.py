stack = []

for i in input().split():
    if i is '*':
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
    elif i is '/':
        b = stack.pop()
        a = stack.pop()
        stack.append(a / b)
    elif i is '+':
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)
    elif i is '-':
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
    else:
        stack.append(float(i))

print("{0:.3f}".format(stack.pop()))
