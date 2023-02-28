def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    returnDict = dict()
    for a in phrase:
        char = a.lower()
        if char in "aeiou":
            if char not in returnDict:
                returnDict[char] = 1
            else:
                returnDict[char] +=1
    return returnDict