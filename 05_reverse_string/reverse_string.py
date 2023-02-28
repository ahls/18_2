def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reversedList = list(phrase)
    reversedList.reverse()
    return "".join(reversedList)