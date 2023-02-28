def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    words = phrase.split(' ')
    index = 0
    for word in words:
        words[index]=word.capitalize()
        index+=1
    return ' '.join(words)
    