def func(numerator, denominator):
    if denominator == 0:
        return []
    whole = numerator // denominator
    rest = numerator - whole * denominator
    return [whole] + func(denominator, rest)