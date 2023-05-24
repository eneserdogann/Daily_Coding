def isValid(s):
    stack = []

    for i in range(0, len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stack.append(s[i])
        else:
            if s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif s[i] == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif s[i] == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

    if len(stack) == 0:
        return True
    else:
        return False

s = "(){}}{"
print(isValid(s))