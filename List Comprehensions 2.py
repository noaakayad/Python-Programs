"""
DSC 20 Fall 2024 Homework 03
Name: Noa Wissam Omar, Akayad
PID: U10274660
Source: w3schools
"""
# Question 1.1
def operate_nums(lst):
    """
    ##############################################################
    # Here I start by verifying that 'lst' is a list with an assertion,
    Then if this condition is verified, I visit every elements of 'lst' and I
    verify that they are all integers with an assertion.
    
    Then if this condition is verified I return a comprehension list following
    the instruction of the question#
    ##############################################################

    >>> operate_nums([1, 2, 3, 's'])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> operate_nums([2, 3.1, -2, 0, 5])
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> operate_nums([2, 3, -2, 0, 5])
    [6, 6, -6, 0, 10]
    >>> operate_nums([])
    []
    >>> operate_nums([4, 4, 4])
    [12, 12, 12]
    >>> operate_nums([0, 1, 2, 3, 5])
    [0, 2, 6, 6, 10]
    """
    assert isinstance(lst, list)
    assert all(isinstance(i, int) for i in lst)
    
    time_2 = 2
    time_3 = 3
    return [i*time_2 if i%time_2 == 1 else i*time_3 for i in lst]

# Question 1.2
def string_lengths(text, nums):
    """
    ##############################################################
    # Here I first check if both 'text' and 'nums' are lists and if so I
    check they both have the same lenght, if so, for each element of these
    lists I see if they have the right type and if the strings aren't empty and
    if the integers are positive.
    
    If so, then I return the corresponding list comprehension.#
    ##############################################################

    >>> string_lengths(['a', 'b', 'c'], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['', 'abc'], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['a', 'b'], [-1, 5])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['abc', 'abcd', 'abcde'], [2, 5, 5])
    [True, False, False]
    
    >>> string_lengths(['hello', 'world'], [5, 5])
    [False, False]
    >>> string_lengths(['hello', 'data'], [1, 3])
    [True, True]
    >>> string_lengths(['sun', 'moon', 'stars'], [0, 3, 5])
    [True, True, False]
    """
    assert isinstance(text, list)
    assert isinstance(nums, list)
    assert len(text) == len(nums)
    assert all(isinstance(text[i], str) for i in range(len(text)))
    assert all(text[i] != '' for i in range(len(text)))
    assert all(isinstance(nums[i],int) and nums[i]>=0
               for i in range(len(text)))
    
    return [len(text[i]) > nums[i] for i in range(len(text))] 

# Question 1.3
def process_dict(input_dict):
    """
    ##############################################################
    # Here I first check that 'input_dict' is a dictionnary, if so then for
    each key and value of the dict, I check if they have the right type
    and if so I check for each word of the value if they are strings.
    
    If so, then I return for each key and value the lenght of the key +
    the sum of a list containing the lengths of every word in the value#
    ##############################################################
    
    >>> process_dict({1: ['a', 'b', 'c'], (1, 2): ['a']})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1, 2): ['a', 0], (2, ): ['b']})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1, 2): ['dsc', 'dsc20', 'dsc30'], (2,): \
    ['b']})
    [15, 2]
    
    >>> process_dict({(3, 4): ['hello', 'world'], (5,): ['yes']})
    [12, 4]
    >>> process_dict({(1,): ['one'], (2, 3): ['two', 'three']})
    [4, 10]
    >>> process_dict({(1, 2, 3): [], (4, 5): ['a', 'ab']})
    [3, 5]
    """
    assert isinstance(input_dict, dict)
    assert all(isinstance(key, tuple) for key in input_dict.keys())
    assert all(isinstance(value, list) for value in input_dict.values())
    assert all(isinstance(word, str) for value in input_dict.values()
               for word in value)
    
    return [len(key) + sum([len(word) for word in value])
            for key,value in input_dict.items()]

# Question 2
def unusual_sort(indices, items):
    """
    ##############################################################
    # Here I check if 'indices' and 'items' have the type 'list', if so
    I verify that they have the same lenght, and if so I check for every
    indice in 'indices' of it is an int and if 'indices' only has numbers
    between 0 and n-1 and all these numbers are different between them;
    
    If so, I return a list containing tuples where each tuple has first the
    'indices[i]'-ith element of items because that allows us to sort items as
    'indices' demands it, then we add the original index which is 'indices[i]'
    and finally the new index which is i, for i in the range of the length of
    'items' or 'indices' as they have the same length at this point of
    the code.#
    ##############################################################

    >>> unusual_sort([0, 4, 2, 3, 1], \
        ["zero", "four", "two", "three", "one"])
    [('zero', 0, 0), ('one', 4, 1), ('two', 2, 2), \
('three', 3, 3), ('four', 1, 4)]

    >>> unusual_sort([0.0, 4.0, 2.0, 3.0, 1.0], \
    ["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort([0, 4, 2, 3, 0], \
        ["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort([0, 4, 2, 3], \
        ["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> unusual_sort([3, 1, 4, 2, 0], \
        ["zero", "one", "two", "three", "four"])
    [('three', 3, 0), ('one', 1, 1), ('four', 4, 2), \
('two', 2, 3), ('zero', 0, 4)]

    >>> unusual_sort([0, 1, 2, 3], \
        ["zero", "one", "two", "three"])
    [('zero', 0, 0), ('one', 1, 1), ('two', 2, 2), \
('three', 3, 3)]

    >>> unusual_sort([1, 0], \
        ["zero", "one"])
    [('one', 1, 0), ('zero', 0, 1)]
    """
    assert isinstance(indices, list)
    assert isinstance(items, list)
    assert len(items) == len(indices)
    assert all(isinstance(indices[i], int) for i in range(len(indices)))
    assert all(i in indices for i in range(len(indices)))
    
    return [(items[indices[i]], indices[i], i) for i in range(len(indices))]

# Question 3
def change_input(strange_list):
    """
    ##############################################################
    # Here I first check that 'strange_list' is a list, if so I
    check if the elements of strange_list are strings.
    
    Then I first put in a list of lists of char named 'list_letters' all the
    updated letters by using a list comprehension nested in another one where I
    first put the updated digits and the updated letters of each string from
    'strange_list' by looping over the letters in each string from strange_list
    and by looping over each string from 'strange_list'; so then I just need to
    join all the letters of each lists and return the corresponding list.#
    ##############################################################

    >>> change_input(["3.14IS PIE", "11My aGe iS"])
    ['6.28IS PIE', '22My AGE IS']
    >>> change_input(["go t6o sleep at ", \
        "5i like to start work before "])
    ['gO t12O slEEp At ', '10I lIkE tO stArt wOrk bEfOrE ']
    >>> change_input("11My aGe iS")
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> change_input(["C0unt d0wn: 9876543210"])
    ['C0Unt d0wn: 181614121086420']
    >>> change_input(["H4ppy", "B1rthd4y"])
    ['H8ppy', 'B2rthd8y']
    >>> change_input(["HELLO", "world"])
    ['HELLO', 'wOrld']
    """
    assert isinstance(strange_list, list)
    assert all(isinstance(i, str) for i in strange_list)
    
    time_2 = 2
    list_letters = [[str(time_2* int(letter)) if letter.isdigit() else
                    letter.upper() if letter in ['a', 'e', 'i', 'o', 'u']
                    else letter for letter in strange_list[i]]
                    for i in range(len(strange_list))]
    
    return [''.join(words) for words in list_letters]

def change_input_even_more(strange_list):
    """
    ##############################################################
    # Here I first check that 'strange_list' is a list, if so I
    check if the elements of strange_list are strings.
    
    Then I create a list of lists of int 'list_nums' that contains all the
    updated digits by casting string to int and int to string
    for each string from 'strange_list' by using a nested list comprehension
    where I loop over the letters of each string from 'strange_list' and by
    looping over the strings of 'strange_list'
    
    Then I do the same with the letters in the list 'list_letters'
    
    Thus I join all the char of each list in 'list_nums' and in 'list_letters'
    
    And thus, I return a list containing the sum of the elements of the 2 lists
    at the same index beginning the sum with the elements of 'list_letters'#
    ##############################################################
    
    >>> change_input_even_more(["3.14IS PIE", "11My aGe iS"])
    ['.IS PIE628', 'My AGE IS22']
    >>> change_input_even_more(["go t6o sleep at ", \
    "5i like to start work before "])
    ['gO tO slEEp At 12', 'I lIkE tO stArt wOrk bEfOrE 10']
    >>> change_input_even_more("11My aGe iS")
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> change_input_even_more(["T4ke t2o tabl3ts", "M0rning"])
    ['TkE tO tAblts846', 'MrnIng0']
    >>> change_input_even_more(["123", "hello", "world5"])
    ['246', 'hEllO', 'wOrld10']
    >>> change_input_even_more(["n3xt l3v3l", "g4me"])
    ['nxt lvl666', 'gmE8']
    """
    assert isinstance(strange_list, list)
    assert all(isinstance(i, str) for i in strange_list)
    
    time_2 = 2
    list_nums = [[str(time_2*int(i)) for i in words if i.isdigit()]
                 for words in strange_list]
    
    list_letters = [[i.upper() if i in ['a','e','i','o','u']
                     else i for i in words if not i.isdigit()]
                    for words in strange_list]
    
    list_nums = [''.join(nums) for nums in list_nums]
    
    list_letters = [''.join(letters) for letters in list_letters]
    
    return [list_letters[i] + list_nums[i] for i in range(len(list_nums))]

def cheapest_gas(gas_stations, mileage):
    """
    ##############################################################
    # Here I first check that mileage is an integer.
    
    Then I see if mileage is a positive integer
    
    Then I see if 'gas_station' is a dictionnary
    
    If so, I verify that the leys are strings, and values are lists of tuple
    and that the tuples have either integers or float and have a length of 2.
    
    
    Then I create the list of tuples 'reachable_stations' that contains
    the name of a station and its price only if the station is reachable. To
    create this list, I used a nested list comprehension where I loop over
    the keys and values of 'gas_stations' and over the elements of each list of
    the values.
    
    Then I create a list of strings 'stations_name' having the name of the
    reachable stations by looping over the tuples of 'reachable_stations' and
    taking the first element of every tuple.
    
    And I do the same with the prices with the prices of reachable stations
    with the list 'stations_price'
    
    And thus, I return the name of the station who has the lowest price by
    finding the index of the min of 'station_price' with the function
    'stations_price.index(min(stations_price))' and by returning the string
    of 'stations_name' at the corresponding index.#
    ##############################################################
    >>> gas_stations = { \
        'Shell': [(20, 5.2), (30, 5.3), (50, 5.6), (80, 5.3)], \
        'Chevron': [(10, 5.8), (60, 5.7)], \
        'Arco': [(20, 5.3), (10, 5.4)] \
    }
    >>> cheapest_gas(gas_stations, 10)
    'Arco'
    >>> cheapest_gas(gas_stations, 20)
    'Shell'
    
    >>> gas_stations2 = { \
        'Total': [(15, 5.5), (35, 5.4), (55, 5.2)], \
        'Exxon': [(25, 5.6), (45, 5.5)], \
        'BP': [(10, 5.7), (30, 5.5), (50, 5.3)] \
    }
    >>> cheapest_gas(gas_stations2, 10)
    'BP'
    >>> cheapest_gas(gas_stations2, 25)
    'Total'
    >>> cheapest_gas(gas_stations2, 40)
    'Total'
    """
    assert isinstance(mileage, int)
    assert mileage > 0
    assert isinstance(gas_stations, dict)
    assert all(isinstance(key, str) and isinstance(value, list) for key,value
               in gas_stations.items())
    assert all(isinstance(value[i], tuple) for value in gas_stations.values()
               for i in range(len(value)))
    assert all(len(value[i]) == 2 for value in gas_stations.values()
               for i in range(len(value)))
    assert all(isinstance(value[i][0], float) or isinstance(value[i][0], int)
               and
               isinstance(value[i][1], float) or isinstance(value[i][1], int)
               for value in gas_stations.values() for i in range(len(value)))
    
    reachable_stations = [(key, value[i][1]) for key, value in
                          gas_stations.items() for i in range(len(value))
                          if value[i][0] <= mileage]
    
    stations_name = [t[0] for t in reachable_stations]
    stations_price = [t[1] for t in reachable_stations]
    
    return stations_name[stations_price.index(min(stations_price))]

def cheapest_average_gas(gas_stations, mileage):
    """
    ##############################################################
    # I create first a list of list of float 'valid_stations_prices' having the
    price of the reachable stations by looping over the tuples of gas_stations
    and taking the second element of every tuple in the values of gas_stations
    
    Then I create a list of list of double named 'mean_stations_prices' that
    contains the mean of the prices of the reachable stations by looping over
    the lists of 'valid_stations_prices'. If a list from valid_stations_prices
    has no element, then I put the float 'inf' in 'mean_stations_prices'
    
    So then, I just need to return the key from 'gas_stations' at the same
    index as the one who has the minimum mean in 'mean_stations_prices'
    as there is one mean for every station and the means are listed in the
    same order as the name of the stations.
    ##############################################################
    
    >>> gas_stations = { \
        'Shell': [(20, 5.2), (30, 5.3), (50, 5.6), (80, 5.3)], \
        'Chevron': [(10, 5.8), (60, 5.7)], \
        'Arco': [(20, 5.1), (10, 5.4)] \
    }
    >>> cheapest_average_gas(gas_stations, 10)
    'Arco'
    >>> cheapest_average_gas(gas_stations, 20)
    'Shell'
    
    >>> gas_stations2 = { \
        'Total': [(15, 5.5), (35, 5.4), (55, 5.2)], \
        'Exxon': [(25, 5.6), (45, 5.5)], \
        'BP': [(10, 5.7), (30, 5.5), (50, 5.3)] \
    }
    >>> cheapest_average_gas(gas_stations2, 10)
    'BP'
    >>> cheapest_average_gas(gas_stations2, 25)
    'Total'
    >>> cheapest_average_gas(gas_stations2, 40)
    'Total'
    """
    valid_stations_prices = [[value[i][1] for i in range(len(value))
                              if value[i][0] <= mileage]
                             for value in gas_stations.values()]
    mean_stations_prices = [sum(prices)/len(prices) if len(prices) != 0
                            else float('inf')
                            for prices in valid_stations_prices]
    
    return list(gas_stations.keys())[mean_stations_prices.
                                     index(min(mean_stations_prices))]

def new_orders(orders, action, dish_name, amount):
    """
    ##############################################################
    # I first check that orders is a dictionary.

    Then I verify that each key in orders is a string and each value is an
    integer that is zero or greater.

    Next, I check that action is a string.

    Then I check that dish_name is a string.

    and then, I verify that amount is an integer.
    
    
    After that, I return a dictionnary comprehension where for each key,
    if the key is 'dish_name' then I update the corresponding value
    according to 'action'; otherwise, I just put the corresponding
    value ad the value of the key.
    ##############################################################
    
    >>> orders = {'pizza': 10, 'burger': 5}
    >>> new_orders(orders, 'add', 'pizza', 5)
    {'pizza': 15, 'burger': 5}

    >>> new_orders(orders, 'remove', 'burger', 3)
    {'pizza': 10, 'burger': 2}

    >>> new_orders(orders, 'remove', 'pizza', 15)
    {'pizza': 0, 'burger': 5}

    >>> new_orders([], 'remove', 'burger', 3)
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> new_orders({'pizza': 10, 'burger': 5}, 'remove', 'burger', 6)
    {'pizza': 10, 'burger': 0}

    >>> new_orders({'pizza': 20, 'sushi': 15}, 'remove', 'sushi', 5)
    {'pizza': 20, 'sushi': 10}

    >>> new_orders({'pasta': 7, 'burger': 5}, 'remove', 'pasta', 10)
    {'pasta': 0, 'burger': 5}
    """
    assert isinstance(orders, dict)
    assert all(isinstance(key, str) and isinstance(value, int) and value >= 0
               for key, value in orders.items())
    assert isinstance(action, str)
    assert isinstance(dish_name, str)
    assert isinstance(amount, int)
    
    return {key : value + amount if action == 'add' and key == dish_name
            else value - amount if key == dish_name  and value-amount >= 0
            else 0 if key == dish_name else value
            for key, value in orders.items()}