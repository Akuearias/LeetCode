def Valid(s: str) -> bool:
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    return True

if __name__ == "__main__":
    print(Valid("(()))(()"))