def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    openP = 0
    for char in parens:
        if(char == "("):
            openP += 1
        elif(char == ")"):
            openP -= 1
            if(openP < 0):
                return False
    
    return openP == 0