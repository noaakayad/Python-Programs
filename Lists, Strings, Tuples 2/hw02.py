"""
DSC 20 Winter 2024 Homework 02
Name: Noa Wissam Omar AKAYAD
PID: U10274660
Source: w3schools, python documentation
"""

# Question 1
def name_mapping(given_names, preferred_names):
    """
    ##############################################################
    #Here, as the list of given names is at most as long as the
    list of preferred names, I do a 'for i in
    range(len(preferred_names)' for loop and I assume that when 'i'
    is exceed the length of 'given_names', we have seen every persons
    that want to use another name which makes me associate 'NO NAME PROVIDED'
    with a preferred name, otherwise, I associate a given name with it
    preferred name that I add to a list named 'fav_names' that is first empty.#
    ##############################################################

    >>> given_names = ['Amanda', 'Jeffrey', 'Richard']
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('Amanda', 'Mandy'), ('Jeffrey', 'Jeff'), ('Richard', 'Rick')]

    >>> given_names = ['Amanda', 'Jeffrey']
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('Amanda', 'Mandy'), ('Jeffrey', 'Jeff'), ('NO NAME PROVIDED', 'Rick')]

    >>> given_names = []
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('NO NAME PROVIDED', 'Mandy'), ('NO NAME PROVIDED', 'Jeff'), \
('NO NAME PROVIDED', 'Rick')]

    # Add at least 3 doctests below here #
    
    >>> given_names = ['Noa', 'Akayad']
    >>> preferred_names = ['Nou7a', 'Noa A.']
    >>> name_mapping(given_names, preferred_names)
    [('Noa', 'Nou7a'), ('Akayad', 'Noa A.')]

    >>> given_names = ['Noa']
    >>> preferred_names = ['Nou7a', 'Noa A.', 'N. Akayad']
    >>> name_mapping(given_names, preferred_names)
    [('Noa', 'Nou7a'), ('NO NAME PROVIDED', 'Noa A.'), \
('NO NAME PROVIDED', 'N. Akayad')]

    >>> given_names = ['Noa']
    >>> preferred_names = ['Nou7a']
    >>> name_mapping(given_names, preferred_names)
    [('Noa', 'Nou7a')]
    """
    
    if len(preferred_names) == 0 :
        return []
    
    fav_names = []
    
    for i in range(len(preferred_names)):
        if (len(given_names)-1) - i >= 0 :
            fav_names.append((given_names[i], preferred_names[i]))
        else :
            fav_names.append(('NO NAME PROVIDED', preferred_names[i]))
    
    return fav_names


# Question 2
def valid_pairs(keys, values):
    """
    ##############################################################
    # For this question, I see the type of every potential key,
    if the type is a immutable one (str, int, float, bool, tuple),
    then we can put it as a key of a dictionnary, and for it value,
    the type doesn't matter so we just need to associate the
    immutable key with it value. I use a list named 'pairs' that is first empty
    and I add all the valid pairs in it so I just need to return it at the end#
    ##############################################################

    >>> keys = ["fun", ["not so much"]]
    >>> values = [("learning",), 6]
    >>> valid_pairs(keys, values)
    [('fun', ('learning',)), ('not valid',)]

    >>> keys = [1, "fun", [2], (1,), {}]
    >>> values = [1, {}, (1,), "island", [2]]
    >>> valid_pairs(keys, values)
    [(1, 1), ('fun', {}), ('not valid',), ((1,), 'island'), ('not valid',)]

    >>> keys =[]
    >>> values =[]
    >>> valid_pairs(keys, values)
    []

    # Add at least 3 doctests below here #
    >>> keys = ['Noa', (1, 2, 3), [1, 2, 3], 'Akayad', {'key': 'value'}]
    >>> values = ['Awesome', (3, 2, 1), 'List', {'dic': 'value'}, 'Dictionary']
    >>> valid_pairs(keys, values)
    [('Noa', 'Awesome'), ((1, 2, 3), (3, 2, 1)), ('not valid',), ('Akayad', \
{'dic': 'value'}), ('not valid',)]

    >>> keys = ['123', 'Noa Akayad', 987, False, (2023, 'Noa')]
    >>> values = ['Numbers', 'Name', 'Integer', True, 'Tuple']
    >>> valid_pairs(keys, values)
    [('123', 'Numbers'), ('Noa Akayad', 'Name'), (987, 'Integer'), \
(False, True), ((2023, 'Noa'), 'Tuple')]

    >>> keys = [5.67, 'Noa', True, (1, 'Noa Akayad'), 2024]
    >>> values = [[5, 6, 7], 'True', False, 'Name', 'Year']
    >>> valid_pairs(keys, values)
    [(5.67, [5, 6, 7]), ('Noa', 'True'), (True, False), ((1, 'Noa Akayad'), \
'Name'), (2024, 'Year')]
    """
    
    pairs = []
    
    for i in range(len(keys)):
        if type(keys[i]) == int or type(keys[i]) == float or \
        type(keys[i]) == str or type(keys[i]) == tuple or \
        type(keys[i]) == int or type(keys[i]) == bool :
            pairs.append((keys[i], values[i]))
        else :
            pairs.append(('not valid',))
    
    return pairs

# Question 3
def dict_of_names(name_tuples):
    """
    ##############################################################
    # Here I create an empty dictionnary 'fav_names'. The method is the
    following one:
    
    If the name isn't yet in 'd', then we create a new key value to 'fav_names'
    using the first element of the tuple as a key and the second element as a
    value.
    
    Else, we just update the list by adding the second element of the tuple.#
    ##############################################################

    >>> dict_of_names([('Richard', 'Rick'),
    ... ('Roxanne', 'Rose'), ('Roxanne', 'Ann'),
    ... ('Richard', 'Ricky'), ('Roxanne', 'Roxie'),
    ... ('Mitchell', 'Mitch')])
    {'Richard': ['Rick', 'Ricky'], 'Roxanne': ['Rose', 'Ann', 'Roxie'], \
'Mitchell': ['Mitch']}

    >>> dict_of_names([('Melissa', 'Lisa'),
    ... ('Isabel', 'Bella'), ('NO NAME PROVIDED', 'Faith')])
    {'Melissa': ['Lisa'], 'Isabel': ['Bella'], \
'NO NAME PROVIDED': ['Faith']}

    >>> dict_of_names([('NO NAME PROVIDED', 'Derrick'), \
    ('NO NAME PROVIDED', 'Jacob')])
    {'NO NAME PROVIDED': ['Derrick', 'Jacob']}

    # Add at least 3 doctests below here #
    >>> dict_of_names([('Noa', 'Nou7a'),
    ... ('Akayad', 'Akay'), ('Noa', 'N.A.'), 
    ... ('Akayad', 'Aka'), ('Noa', 'Noa A.')])
    {'Noa': ['Nou7a', 'N.A.', 'Noa A.'], 'Akayad': ['Akay', 'Aka']}

    >>> dict_of_names([('Mohamed', 'Momo'), 
    ... ('Saad', 'S'), ('Mohamed', 'Mo'), 
    ... ('Saad', 'Saad Jaafari')])
    {'Mohamed': ['Momo', 'Mo'], 'Saad': ['S', 'Saad Jaafari']}

    >>> dict_of_names([('Noa Akayad', 'Noa'), 
    ... ('Mohamed Saad', 'Mohamed'), ('Noa Akayad', 'Nou7a')])
    {'Noa Akayad': ['Noa', 'Nou7a'], 'Mohamed Saad': ['Mohamed']}
    """
    
    fav_names = {}
    
    for t in name_tuples :
        if t[0] not in fav_names :
            fav_names[t[0]] = [t[1]]
        else :
            fav_names[t[0]].append(t[1])
    
    return fav_names


# Question 4.1
def contractor_payment(suggestions):
    """
    ##############################################################
    # I create a dictionnary named 'contractors_label' having the keys
    '1', '2', and '3' and O as a value, and 3 counters 'avg1', 'avg2', and
    'avg3' that first are the sum of the pay for every corresponding contractor
    thanks to a for loop that visit every list of 'suggestions'.
    
    After that we just need to associate to each key the corresponding avg
    divided by the length of 'suggestions' rounded with 2 decimals #
    ##############################################################

    >>> contractor_payment([[10, 20, 30], [0, 20, 10]])
    {'1': 5.0, '2': 20.0, '3': 20.0}

    >>> contractor_payment([[10, 20, 30], [30, 20, 10], [5, 10, 15]])
    {'1': 15.0, '2': 16.67, '3': 18.33}

    >>> contractor_payment([[-5, -10, -4], [-20, 15, 40]])
    {'1': -12.5, '2': 2.5, '3': 18.0}

    # Add at least 3 doctests below here #
    >>> contractor_payment([[100, 200, 300], [100, 200, 300], [100, 200, 300]])
    {'1': 100.0, '2': 200.0, '3': 300.0}

    >>> contractor_payment([[50, 75, 125], [25, 50, 100], [100, 150, 200]])
    {'1': 58.33, '2': 91.67, '3': 141.67}

    >>> contractor_payment([[5, 10, 15], [0, 0, 0], [5, 10, 15], [10, 20, 30]])
    {'1': 5.0, '2': 10.0, '3': 15.0}
    """
    
    contractors_label = {'1' : 0, '2' : 0, '3' : 0}
    rounded_decimal = 2
    third_element = 2
    
    avg1 = 0
    avg2 = 0
    avg3 = 0
    
    for lst in suggestions :
        avg1 += lst[0]
        avg2 += lst[1]
        avg3 += lst[third_element]
    
    contractors_label['1'] = round(avg1 / len(suggestions),rounded_decimal)
    contractors_label['2'] = round(avg2 / len(suggestions),rounded_decimal)
    contractors_label['3'] = round(avg3 / len(suggestions),rounded_decimal)
    
    return contractors_label
    

# Question 4.2
def new_pay(hours):
    """
    ##############################################################
    # Here I start by creating the int 'penalty_bonus' which equals to -10.
    
    First case : a negative number of hours occurs in the values, then we add
    the key 'Pay' to the dictionnary and the value becomes 'Penalty'
    
    Other case : there no negative numbers occur in the values. then we
    calculate the number 'bonus' with the formula and by accessing the values
    with hours['i'] where 'i' is the pay for contractor 'i'.
    Finally we update the dictionnary, regarding the value of 'bonus' and we
    return 'bonus'
    #
    ##############################################################

    >>> case1 = {'1': 200, '2': 138, '3': 172}
    >>> round(new_pay(case1), 2)
    0.51
    >>> case1
    {'1': 200, '2': 138, '3': 172, 'pay': 'Bonus'}

    >>> case2 = {'1': 130, '2': 84, '3': -14}
    >>> new_pay(case2)
    -10
    >>> case2
    {'1': 130, '2': 84, '3': -14, 'pay': 'Penalty'}

    >>> case3 = {'1': 42, '2': 96, '3': 63}
    >>> round(new_pay(case3), 1)
    -2.4
    >>> case3
    {'1': 42, '2': 96, '3': 63, 'pay': 'Penalty'}

    # Add at least 3 doctests below here #
    >>> case4 = {'1': 180, '2': 150, '3': 120}
    >>> round(new_pay(case4), 2)
    -0.55
    >>> case4
    {'1': 180, '2': 150, '3': 120, 'pay': 'Penalty'}

    >>> case5 = {'1': 300, '2': 0, '3': 200}
    >>> new_pay(case5)
    0.0
    >>> case5
    {'1': 300, '2': 0, '3': 200, 'pay': 'No'}

    >>> case6 = {'1': -300, '2': 0, '3': 200}
    >>> round(new_pay(case6), 1)
    -10
    >>> case6
    {'1': -300, '2': 0, '3': 200, 'pay': 'Penalty'}
    """
    
    penalty_bonus = -10
    
    for value in list(hours.values()) :
        if value < 0 :
            hours['pay'] = 'Penalty'
            return penalty_bonus
    
    bonus = 0.01 * hours['1'] + 0.015 * hours['2'] + min(0.02 * \
            abs(100 - hours['3']), 0.025 * hours['3']) - 5
    
    if bonus > 0 :
        hours['pay'] = 'Bonus'
    elif bonus == 0 :
        hours['pay'] = 'No'
    else :
        hours['pay'] = 'Penalty'
    
    return bonus

# Question 5
def potential_ideas_for_business(items):
    """
    ##############################################################
    # Here, I create an empty list 'unique_items' and I visit each item of each
    list in 'items'; if isn't in 'lst' yet, then I add it in.
    
    And I return the sorted 'lst'#
    ##############################################################

    >>> items = {'supplier 1': ['Tea', 'Peaches'], \
    'supplier 2': ['Peaches', 'Apples', 'Cups']}
    >>> potential_ideas_for_business(items)
    ['Apples', 'Cups', 'Peaches', 'Tea']

    >>> items = {'supplier 1': ['Flour', 'Eggs', 'Chocolate', 'Milk'], \
    'supplier 2': ['Milk', 'Eggs', 'Vanilla', 'Butter'], \
    'supplier 3': ['Butter', 'Sugar']}
    >>> potential_ideas_for_business(items)
    ['Butter', 'Chocolate', 'Eggs', 'Flour', 'Milk', 'Sugar', 'Vanilla']

    >>> items = {'supplier 1': [], 'supplier 2': []}
    >>> potential_ideas_for_business(items)
    []
    
    # Add at least 3 doctests below here #
    >>> items = {'supplier 1': ['Noa Cookies', 'Akayad Spices'], \
    'supplier 2': ['Noa Cookies', 'Mohamed Coffee', 'Saad Snacks']}
    >>> potential_ideas_for_business(items)
    ['Akayad Spices', 'Mohamed Coffee', 'Noa Cookies', 'Saad Snacks']

    >>> items = {'supplier 1': ['Noa Cereals', 'Akayad Herbs'], \
    'supplier 2': ['Noa Cereals', 'Akayad Herbs', 'Mohamed Tea']}
    >>> potential_ideas_for_business(items)
    ['Akayad Herbs', 'Mohamed Tea', 'Noa Cereals']

    >>> items = {'supplier 1': ['Noa Tea'], \
    'supplier 2': ['Noa Tea', 'Akayad Spices'], \
    'supplier 3': ['Noa Tea', 'Akayad Spices', 'Mohamed Spices']}
    >>> potential_ideas_for_business(items)
    ['Akayad Spices', 'Mohamed Spices', 'Noa Tea']
    """
    
    unique_items = []
    
    for list_items in list(items.values()) :
        for item in list_items :
            if item not in unique_items :
                unique_items.append(item)
    
    return sorted(unique_items)

# Question 6.1
def count_lines_1(filepath):
    """
    ##############################################################
    # In this function, I take each line of the text and while this line isn't
    after the last one of the text (equals to '') then I increment a counter.
    After that, I return this counter#
    ##############################################################

    >>> count_lines_1('files/test1.txt')
    6
    >>> count_lines_1('files/test2.txt')
    24

    # Add at least 3 doctests below here #
    >>> count_lines_1('files/ings1.txt')
    3
    >>> count_lines_1('files/offices1.txt')
    3
    >>> count_lines_1('files/offices2.txt')
    4
    """
    with open(filepath) as reader :
        count = 0
        line = reader.readline()
        while line != '' :
            count += 1
            line = reader.readline()
        return count


# Question 6.2
def count_lines_2(filepath):
    """
    ##############################################################
    # Here I put the whole text in a string named 'text' and I
    split this string in a list named 'list-lines'. Thus, I just need
    to return the length of this list#
    ##############################################################

    >>> count_lines_2('files/test1.txt')
    6
    >>> count_lines_2('files/test2.txt')
    24

    # Add at least 3 doctests below here #
    >>> count_lines_2('files/ings1.txt')
    3
    >>> count_lines_2('files/offices1.txt')
    3
    >>> count_lines_2('files/offices2.txt')
    4
    """
    
    with open(filepath) as reader :
        text = reader.read()
        list_lines = text.split('\n')
        return len(list_lines) 
    

# Question 6.3
def count_lines_3(filepath):
    """
    ##############################################################
    # Here I do the same method as in the previous function but instead
    of creat a list that represents the splited string returned by read(),
    I use the list directly created by readlines(), and I return the length
    of this list. #
    ##############################################################

    >>> count_lines_3('files/test1.txt')
    6
    >>> count_lines_3('files/test2.txt')
    24

    # Add at least 3 doctests below here #
    >>> count_lines_3('files/ings1.txt')
    3
    >>> count_lines_3('files/offices1.txt')
    3
    >>> count_lines_3('files/offices2.txt')
    4
    """
    with open(filepath) as reader :
        return len(reader.readlines())


# Question 7
def collected_items(filepath):
    """
    ##############################################################
    # I create an empty list named 'items' and then I visit every line in the
    file thanks to the function readlines().
    For each line, I create the list 'words' that contains all the words in the
    line thanks to the function split(',').
    Then I remove all extra spaces in 'words' and I add in 'items' the third
    word of words as the word at this index represents items.
    ANd finally I return 'items'#
    ##############################################################

    >>> collected_items('files/ings1.txt')
    ['ice-cream', 'boba tea', 'fish']
    >>> collected_items('files/ings2.txt')
    ['shovel', 'headphones', 'bird', 'brownies']
    >>> collected_items('files/empty_trip.txt')
    []

    # Add at least 3 doctests below here #
    
    # I have created the following files so I can test easily my function#
    >>> collected_items('files/quest7doctest1.txt')  
    ['big tasty', 'big tasty', 'chwaya dsardine', 'bowl']
    >>> collected_items('files/quest7doctest2.txt')  
    ['burger', 'big tasty', 'chwaya dsardine', 'bowl']
    >>> collected_items('files/quest7doctest3.txt')  
    ['meal1', 'meal2', 'meal3', 'meal4', 'meal5', 'meal6', 'meal7', 'meal8']
    """
    items = []
    index_item = 2
    with open(filepath) as reader :
        lines = reader.readlines()
        
        for line in lines :
            words = line.split(',')
            for i in range(len(words)) :
                words[i] = words[i].strip()
            
            items.append(words[index_item])
        
        return items


# Question 8
def case_letters(filepath):
    """
    ##############################################################
    # Here I open the file in a writing mode and I create the counters
    'upper' and 'lower'.
    
    After that I see every letter of the name of the file :
    First case : the letter is upper, thus I increment 'upper'
    Second case : the letter isn't upper, if this letter is an
    alphabetic character then I increment 'lower'.
    
    Finally, we just need to write first 'upper' thanks to the function write()
    and 'lower' in another line#
    ##############################################################

    >>> case_letters('files/AlErNaTiNg.txt')
    >>> with open('files/AlErNaTiNg.txt', 'r') as outfile1:
    ...    print(outfile1.read().strip())
    5
    13
    >>> case_letters('files/another_test.txt')
    >>> with open('files/another_test.txt', 'r') as outfile2:
    ...    print(outfile2.read().strip())
    0
    19
    
    # Add at least 3 doctests below here #
    >>> case_letters('files/another_test_noa.txt')
    >>> with open('files/another_test_noa.txt', 'r') as outfile3:
    ...    print(outfile3.read().strip())
    0
    22
    >>> case_letters('files/another_test_noaA.txt')
    >>> with open('files/another_test_noaA.txt', 'r') as outfile4:
    ...    print(outfile4.read().strip())
    1
    22
    >>> case_letters('files/another_test_UPPER_NOA.txt')
    >>> with open('files/another_test_UPPER_NOA.txt', 'r') as outfile5:
    ...    print(outfile5.read().strip())
    8
    19
    """
    
    with open(filepath, 'w') as writer :
        upper = 0
        lower = 0
        for i in filepath :
            if i.isupper():
                upper += 1
            if not i.isupper() and i.isalpha() :
                lower += 1
        
        writer.write(str(upper) +'\n')
        writer.write(str(lower) +'\n')
        
        return None

# Question 9
def map_office(filepath):
    """
    ##############################################################
    # Here, I start by creating 5 variables that represent the number
    of the first and the last room of each floor.
    
    After that I first use a 'with open' statement as a reader to the read
    the file filepath and access his numbers.
    And I use a nested 'with open' statement as a writer to write in 
    the file 'floors' and depending on the numbers of 'filepath' I write
    in 'floors' the regarding text.
    
    Also I have created the variable 'valid_num_sum' that sum every
    'room' that is has a valid number, and I return this int
    ##############################################################

    >>> map_office('files/offices1.txt')
    259
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    ground floor
    not a valid office number
    second floor

    >>> map_office('files/offices2.txt')
    734
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    third floor and above
    not a valid office number
    second floor
    ground floor
    
    
    # Add at least 3 doctests below here #
    
    # I have created the following files so I can test easily my function#
    
    >>> map_office('files/offices3.txt')
    0
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    not a valid office number
    not a valid office number
    not a valid office number
    not a valid office number
    
    >>> map_office('files/offices5.txt')
    1001
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    ground floor
    ground floor
    second floor
    third floor and above
    third floor and above
    """
    
    with open(filepath, 'r') as reader :
        with open('files/floors.txt', 'w') as writer :
            
            ground_floor_end = 199
            second_floor_begin = 200
            second_floor_end = 299
            third_floor = 300
            valid_num_sum = 0
            
            nums = reader.readlines()
            
            for room in nums :
                room = room.strip()
                if int(room) < 1 :
                    writer.write('not a valid office number\n')
                elif 1<=int(room)<=ground_floor_end :
                    valid_num_sum += int(room)
                    writer.write('ground floor\n')
                elif second_floor_begin<=int(room)<=second_floor_end :
                    valid_num_sum += int(room)
                    writer.write('second floor\n')
                elif int(room) >= third_floor :
                    valid_num_sum += int(room)
                    writer.write('third floor and above\n')
            
            return valid_num_sum
