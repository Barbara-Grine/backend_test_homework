def is_correct_bracket_seq(s):

    stack = []
    for i in s:
        if i in '([{':
            stack.append(i)
        elif i in ')]}':
            if len(stack) == 0:
                return False
            else:
                top = stack.pop()
                if top != '(' and i == ')':
                    return False
                if top != '[' and i == ']':
                    return False
                if top != '{' and i == '}':
                    return False
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    sequence = input()
    print(is_correct_bracket_seq(sequence))
