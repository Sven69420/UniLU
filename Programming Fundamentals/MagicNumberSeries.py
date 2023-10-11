def is_magic_sequence(s):
    """checks to see if the integers read the same forwards and backwards"""
    if abs(s) == abs(s)[::-1]:
        return True
    else:
        return False

