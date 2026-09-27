def is_valid(s):
    stack = []

    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:

        # Opening bracket
        if ch in "([{":
            stack.append(ch)

        # Closing bracket
        elif ch in ")]}":

            # No opening bracket available
            if not stack:
                return False

            # Top opening bracket doesn't match
            if stack.pop() != brackets[ch]:
                return False

    # Valid only if no unmatched opening brackets remain
    return len(stack) == 0


print(is_valid('[({})]'))
