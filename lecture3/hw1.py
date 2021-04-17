"""
Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
https://en.wikipedia.org/wiki/Narcissistic_number
Examples:
- 9 is an Armstrong number, 9 = 9^1 = 9
- 10 is not: 10 != 1^2 + 0^2 = 1
- 153 is : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
Write a function that detects if a number is Armstrong number in functionaly style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions
### Example function signature and call
"""
from functools import reduce


def is_armstrong(number: int) -> bool:
    numbers_as_list = [int(x) for x in str(number)]
    mapped_numbers = [x ** len(numbers_as_list) for x in numbers_as_list]
    reduced_numbers = reduce(lambda x, y: x + y, mapped_numbers)
    return reduced_numbers == number


print(is_armstrong(153))
