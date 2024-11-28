"""
DSC 20 Fall 2024 Lab 05
Name: Noa Wissam Omar Akayad
PID: U10274660
"""

# PRE-DEFINED FUNCTIONS
def identity(x):
    return x

def squared(x):
    return x**2

def cubed(x):
    return x**3

def root(x):
    return round(x ** 0.5, 2)

# Question 1
def vector_op(lst, func):
    """
    Applies function to each element in the list
    --
    Parameters:
        lst: list of numbers
        func: a function to be applied
    --
    Returns:
        List of transformed numbers

    >>> lst = [1, 2, 3]
    >>> vector_op(lst, squared)
    [1, 4, 9]
    >>> lst = [1, 2, 3, 5]
    >>> vector_op(lst, lambda x: -x)
    [-1, -2, -3, -5]
    >>> vector_op(lst, identity)
    [1, 2, 3, 5]
    >>> lst = [10, 20, 30]
    >>> vector_op(lst, cubed)
    [1000, 8000, 27000]
    """
    # YOUR CODE GOES HERE #
    return [func(x) for x in lst]

# Question 2
def matrix_op(lsts, func):
    """
    Applies function to each element in the 2D list
    --
    Parameters:
        lsts: list of lists of numbers
        func: a function to be applied
    --
    Returns:
        List of lists of transformed numbers

    >>> lsts = [[1,2], [3,4]]
    >>> matrix_op(lsts, squared)
    [[1, 4], [9, 16]]
    >>> lsts = [[10, 20], [30, 40]]
    >>> matrix_op(lsts, lambda x: x / 10)
    [[1.0, 2.0], [3.0, 4.0]]
    >>> lsts = [[5,15], [25,35]]
    >>> matrix_op(lsts, identity)
    [[5, 15], [25, 35]]
    """
    # YOUR CODE GOES HERE #
    return [vector_op(l, func) for l in lsts]

# Question 3
def hop_hop(lst, func):
    """
    Applies function to each element in list twice
    --
    Parameters:
        lst: list of numbers
        func: a function to be applied
    --
    Returns:
        List of transformed numbers

    >>> lst = [1,2,3]
    >>> hop_hop(lst, squared)
    [1, 16, 81]
    >>> lst = [5,6,7,8]
    >>> hop_hop(lst, lambda x:x+1)
    [7, 8, 9, 10]
    >>> lst = [10,20,30]
    >>> hop_hop(lst, cubed)
    [1000000000, 512000000000, 19683000000000]
    """
    # YOUR CODE GOES HERE #
    return [func(func(x)) for x in lst]

# Question 4
def hop_many(lst, func, iterations):
    """
    Applies function to each element in list specified number of times
    --
    Parameters:
        lst: list of numbers
        func: a function to be applied
        iterations: number of times to perform operation
    --
    Returns:
        List of transformed numbers

    >>> lst = [1,2,3]
    >>> hop_many(lst, squared, 2)
    [1, 16, 81]
    >>> hop_many(lst, squared, 3)
    [1, 256, 6561]
    >>> hop_many(lst, identity, 100)
    [1, 2, 3]
    >>> hop_many(lst, lambda x: x - 1, 4)
    [-3, -2, -1]
    """
    # YOUR CODE GOES HERE #
    new_lst = lst[:]
    
    for i in range(iterations) :
        new_lst = [func(x) for x in new_lst]
    
    return new_lst

# Question 5
def grades_stats(input_lst, choice):
    """
    Calculates mean, median, or both stats for input list. `choice` is 
    1 for median, 2 for mean, and any other for both stats.
    --
    Parameters:
        input_lst: list of integers
        choice: positive integer representing each stat
    --
    Returns:
        Stats of the input list

    >>> lst = [3, 2, 1]
    >>> grades_stats(lst, 1)
    2
    >>> grades_stats(lst, 2)
    2.0
    >>> grades_stats(lst, 0)
    (2, 2.0)
    >>> lst = [1, 2, 4]
    >>> grades_stats(lst, 2)
    2.33
    >>> grades_stats(lst, -1)
    (2, 2.33)
    """
    def find_median(): # Calculate median
        # YOUR CODE GOES HERE #
        input_lst.sort()
        if len(input_lst) % 2 == 0 :
            return (input_lst[len(input_lst)//2] +
                    input_lst[(len(input_lst)//2) - 1])/2
        else :
            return input_lst[len(input_lst)//2]

    def find_mean(): # Calculate mean
        # YOUR CODE GOES HERE #
        return round((sum(input_lst))/(len(input_lst)), 2)

    if choice == 1 :
        return find_median()
    elif choice == 2 :
        return find_mean()
    else :
        return (find_median(), find_mean())

# Question 6
def calculate_final_price(original_price, category, season):
    """
    Calculates price of item after discount.
    --
    Parameters:
        original_price: number representing price of item
        category: string category of item that category discount is based on
        season: string season that seasonal discount is based on
    --
    Returns:
        The final price of item after applying potential discounts
    
    >>> calculate_final_price(120, 'electronics', 'Spring')
    108.0
    >>> calculate_final_price(45, 'clothing', 'Winter')
    30.6
    >>> calculate_final_price(100, 'appliance', 'Spring')
    100
    """
    def apply_category_discount(op):
        if category == "electronics" :
            return op*(1 - 10/100)
        elif category == "clothing" :
            return op*(1 - 20/100)
        elif category == "home" :
            return op*(1 - 5/100)
        else :
            return op
    
    def apply_seasonal_discount(op):
        if season == "Winter" :
            return op*(1 - 15/100)
        elif season == "Summer" :
            return op*(1 - 10/100)
        elif season == "Fall" :
            return op*(1 - 5/100)
        else :
            return op
    
    original_price = apply_category_discount(original_price)
    original_price = apply_seasonal_discount(original_price)
    return round(original_price,2)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)