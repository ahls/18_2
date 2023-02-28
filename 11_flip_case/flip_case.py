def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    returnList = []
    for char in phrase:
        if(to_swap.lower() == char):
            returnList.append(char.upper())
        elif(to_swap.upper() == char):
            returnList.append(char.lower())
        else:
            returnList.append(char)
            
    return "".join(returnList)