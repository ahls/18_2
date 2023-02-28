def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    chars1 = str(num1)
    chars2 = str(num2)
    set1 = set(chars1)
    
    for n in set1:
        if chars1.count(n) != chars2.count(n):
            return False
    return True