def isBalanced(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '{' or s[i] == '[' or s[i] == '(':
            stack.append(s[i])
        else:
            if not stack:
                return 'NO'
            elif (s[i] == '}' and stack[-1] != '{'
                  or s[i] == ']' and stack[-1] != '['
                  or s[i] == ')' and stack[-1] != '('):
                return 'NO'
            else:
                stack.pop()

    return 'YES' if not stack else 'NO'