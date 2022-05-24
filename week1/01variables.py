def add_one(x):
    """
    get a x and return x plus 1
    :return: int
    """
    return x + 1

def get_average(x , y):
    """
    return the average of x and y
    :param x: int
    :param y: int
    :return: float
    """
    return (x + y)/2

def get_diffence(x , y):
    """
    return the difference of x and y
    :param x: int
    :param y: int
    :return: int
    """
    return x - y


def exercise1(x, y):
    print(x + y)
    print(x - y)
    print((x + y)/2)


exercise1(1, 2)




def is_odd_or_not(x):
    """
    if x is odd, print 'odd' else print 'even'
    :param x:
    :return:
    """
    if x % 2 == 1:
        print("odd")
    else:
        print("even")


def both_odd(a , b):
    if a % 2 == 1 and b % 2 == 1:
        print("both")
    else:
        print("not")


both_odd(1, 4)




x = 1
y = 2

tmp = x
x = y
y = tmp

print(x, y)

print("the value of y is:", y)


def print_numbers_from_zero_to_x(x):
    for number in range (0, x+1):
        if number != 7:
            print(number)

# print_numbers_from_zero_to_x(10)



def fun(x):
    for n in range(0, x+1):
        if n % 2 == 1 and n<5:
            print("?")
        else:
            print(n)

fun(7)


a = "ss\ne"
print(a)

a =123
print("the value is %d" % a)
print("the value is %d" % 14)


info = ["name", 1.68, 74, 24]
string_format = "name is %s, with height %.2f and weight %.2f and age %d"
print(string_format %(info[0], info[1], info[2], info[3]))

list = [1, 2, "str", True]
for element in list:
    print(element)

def list_less_than(x):
    """
    return a list containing elements from 0 to x
    :param x: largest value
    :return: list
    """
    res = []
    for number in range(0, x+1):
        res.append(number)
    return res


print(list_less_than(4))

def print_element_(list):
    """
    print every element in the list one by one
    :param list:
    :return:
    """
    for i in range(0, len(list)):
        print(list[i])


def print_element_reverse(lst):
    """
    Print element in reverse order.
    :param lst:
    :return:
    """
    for i in range(0, len(lst)):
        print(lst[len(lst)-1-i])

print_element_reverse([1, 245, "styi", "\"slk\""])


























