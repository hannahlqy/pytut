def larger_remainder(x, y, z):
    """
    Return true if the remainder of the first integer when dived by remainder is larger than the remainder of the second
    number when divided by the third integer. Return False otherwise.
    :param x:
    :param y:
    :param z:
    :return:
    """
    return x % z > y % z


def nth_digit(number, n):
    """
    The first param is an arbitrary integer. The second param is an integer that specifies a digit in the first parameter.
    This function returns that digit.

    nth_digit(123, 0) returns 3,
    nth_digit(123, 1) returns 2,
    nth_digit(123, 2) returns 1.

    :param number:
    :param n:
    :return:
    """
    # a = str(number)
    # return int(a[len(a)-n])
    return number // 10 ** n % 10


print(type(nth_digit(123456, 2)))


def remove_vowels(input_str):
    """
    Return a new str that is identical to the input str excpet that the vowels have been removed.
    Vowels are a,e,i,o,u.
    :param str:
    :return:
    """


def convert_to_upper(list_of_strs):
    """
    Convert the list of strs in the given list to uppercase.

    x = ['a', 'b']
    convert_to_upper(x) returns None
    x becomes = ['A', 'B']4

    :param list_of_strs:
    :return:
    """

