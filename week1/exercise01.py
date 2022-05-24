def print_element_with_step(lst, step_size):
    """
    Print element in the list with given step.

    Example:
    1. print_element_with_step([0, 1, 2, 3, 4], 2)
        0
        2
        4
    2 print_element_with_step([0, 1, 2, 3, 4], 1)
        0
        1
        2
        3
        4
    :param lst:
    :param step_size:
    :return:
    """
    i = 0
    while i < len(lst):
        print(lst[i])
        i = i + step_size

    for i in range(0, len(lst), step_size):
        print(lst[i])


def fib_sequence(size_of_seq):
    """
    Return a fib sequence of size size_of_seq.
    A fib sequence is defined as following:

    fib = [fib0, fib1, fib2 ..., fibn]
    fib0 = 1
    fib1 = 1
    fib2 = fib0 + fib1 = 2
    fib3 = fib2 + fib1 = 2 + 1 = 3
    ...
    fibn = fibn-1 + fibn-2

    Example:
    1. fib_sequence(1)
    return [1]
    2. fib_sequence(3)
    return [1, 1, 2]
    3. fib_sequence(5):
    return [1, 1, 2, 3, 5]

    :param size_of_seq:
    :return:
    """
    if size_of_seq == 1:
        return [1]
    elif size_of_seq == 2:
        return [1, 1]

    lst = [1, 1]
    current_size = 2
    while current_size < size_of_seq:
        next_value = lst[len(lst)-1] + lst[len(lst)-2]
        lst.append(next_value)
        current_size += 1
    # Exit: current_size  >=  size_of_seq
    return lst


print(fib_sequence(5))
print(fib_sequence(2))
print(fib_sequence(1))
print(fib_sequence(8))

# print_element_with_step([1, 2, 3, 4, 5], 2)