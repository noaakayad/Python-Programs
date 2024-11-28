"""
DSC 20 Fall 2024 Lab 01
Name: Noa Wissam Omar AKAYAD
PID: U10274660
"""

# Question 1
def team_member_age(ages):
    """
    Checks whether at least one team member is 23 or older.
    ---
    Parameters: 
        lst: a list of positive integers, might be empty
    ---
    Returns:
        True if at least one driver is 23 or older,
        False otherwise

    >>> team_member_age([19, 22, 21])
    False
    >>> team_member_age([19, 23, 15, 27])
    True
    >>> team_member_age([])
    False
    >>> team_member_age([45, 22, 18, 24])
    True
    >>> team_member_age([22, 18, 21])
    False
    >>> team_member_age([23])  
    True
    """
    
    over_23 = 0
    
    for i in ages :
        if i >= 23 :
            over_23 = over_23 + 1
    
    return over_23 > 0

# Question 2
def counter_23_and_over(ages):
    """
    Counts how many people aged 23 or older are in the given list. 
    ---
    Parameters: 
        lst: a list of positive integers, might be empty
    ---
    Returns:
        The number of people whose age is 23 or older.

    >>> counter_23_and_over([])
    0
    >>> counter_23_and_over([12, 15])
    0
    >>> counter_23_and_over([12, 23, 34])
    2
    >>> counter_23_and_over([40, 15, 22])
    1
    """
    
    over_23 = 0
    
    for i in ages :
        if i >= 23 :
            over_23 = over_23 + 1
    
    return over_23

# Question 3
def company_name_one(first_name, last_name):
    """
    Concatenates the string parameters into the output string. 
    ---
    Parameters:
        first_name: first name, as a string
        last_name: last name, as a string
    ---
    Returns:
        A new string with the company's name. 

    >>> company_name_one("Marina", "Langlois")
    'Company name is Langlois a'
    >>> company_name_one("Marina", "")
    'Company name is  a'
    >>> company_name_one("THE", "best")
    'Company name is best E'
    >>> company_name_one("Noa", "Akayad")
    'Company name is Akayad a'
    """
    
    return "Company name is " + last_name + " " + first_name[-1]

# Question 4
def company_name_two(names):
    """
    Creates the name for the team by putting together first and last
    characters of each name. Adds a space if the input only has one      
    character. 
    ---
    Parameters:
        names: list of names, as strings
    ---
    Returns:
        Team name as a string

    >>> names = ["Marina", "J", "Mike"]
    >>> company_name_two(names)
    'MaJ Me'

    >>> names = ["Sheldon", "Leonard", "Raj", "Howard"]
    >>> company_name_two(names)
    'SnLdRjHd'

    >>> names = ["Y", "J", "B"]
    >>> company_name_two(names)
    'Y J B '
    """
    
    name = ""
    
    for i in names :
        if len(i) == 1 :
            name = name + i + " "
        else :
            name = name + i[0] + i[-1]
    
    return name

# Question 5.1
def new_slogan_concat(words, separator):
    """
    Creates a slogan from the words, adding a separator between them. 
    ---
    Parameters:
        words: list of words, as strings
        separator: single character 
    ---
    Returns:
        A slogan as a string

    >>> words = ["Come", "and", "see"]
    >>> new_slogan_concat(words, " ")
    'Come and see'

    >>> words = ["Work", "hard", "nap", "harder"]
    >>> new_slogan_concat(words, ".")
    'Work.hard.nap.harder'
    
    >>> words = []
    >>> new_slogan_concat(words, " ")
    ''
    >>> new_slogan_concat(["Hello", "world"], ", ")
    'Hello, world'
    >>> new_slogan_concat(["single"], "-")
    'single'
    >>> new_slogan_concat([], "-")  
    ''
    """
    
    if len(words) == 0 :
        return ""
    else :
        slogan = ""
        
        for i in words[:-1] :
            slogan = slogan + i + separator
        
        slogan = slogan + words[-1]
        
    return slogan

# Question 5.2
def new_slogan_join(words, separator):
    """
    Creates a slogan from the words, adding a separator between them. 
    ---
    Parameters:
        words: list of words, as strings
        separator: single character 
    ---
    Returns:
        A slogan as a string

    >>> words = ["Come", "and", "see"]
    >>> new_slogan_join(words, " ")
    'Come and see'

    >>> words = ["Work", "hard", "nap", "harder"]
    >>> new_slogan_join(words, ".")
    'Work.hard.nap.harder'
    
    >>> words = []
    >>> new_slogan_concat(words, " ")
    ''
    """
    
    slogan = separator.join(words)
    
    return slogan


# Question 6.1
def idea_simple_drawing(symbol, repeat):
    """
    Creates a string of symbols 
    ---
    Parameters:
        symbol: a single character
        repeat: positive integer
    ---
    Returns:
        A string of symbols repeated a given number of times.

    >>> idea_simple_drawing("-", 4)
    '----'
    >>> idea_simple_drawing("+", 5)
    '+++++'
    >>> idea_simple_drawing("", 2)
    ''
    >>> idea_simple_drawing("#", 0)  
    ''
    >>> idea_simple_drawing("#", 3)
    '###'
    >>> idea_simple_drawing("ab", 3)  
    'ababab'
    >>> idea_simple_drawing(" ", 5)  
    '     '
    """
    
    return symbol * repeat

# Question 6.2
def idea_longer_drawing(symbols, repeats):
    """
    Creates a string of symbols
    ---
    Parameters:
        symbols: a list of single characters
        repeat: a list of positive integers, has the same length
        as symbols list
    ---
    Returns:
        A string of symbols repeated a corresponding number of
        times.

    >>> idea_longer_drawing(['-', '+'], [4, 5])
    '----+++++'
    >>> idea_longer_drawing(['dsc', '20'], [1, 5])
    'dsc2020202020'
    >>> idea_longer_drawing([], [])
    ''
    """
    
    draw = ""
    
    for i in range(len(symbols)) :
        draw = draw + symbols[i] * repeats[i]
        
    return draw

# Question 7.1
def average_rating(ratings):
    """
    Finds average where numbers lower than 3.75 get a value of a 0.

    Args:
        ratings: list of integers ranging from 1 to 5

    Returns:
        The average of the ratings rounded to the second decimal place
    
    >>> average_rating([5, 5, 5])
    5.0
    >>> average_rating([5, 5, 4])
    4.67
    >>> average_rating([4, 2, 1])
    1.33
    >>> average_rating_lists([])
    -1
    >>> average_rating([5, 4, 3, 2, 1])
    1.8
    >>> average_rating([1, 1, 1, 1, 5])
    1.0
    >>> average_rating([5, 5, 5, 5, 5])
    5.0
    """
    
    if len(ratings) == 0 :
        return -1
    else :
        average = 0
        
        for i in ratings :
            if i < 3.75 :
                continue
            else :
                average = average + i
        
        average = average/len(ratings)
        
        return round(average, 2)

# Question 7.2
def average_rating_lists(ratings):
    """
    Finds the highest average among the inner lists.
    --
    Parameters:
        ratings: a list of list(s) of numbers ranging from 1 to 5
    --
    Returns:
        The highest average rounded to two decimal places.
    
    >>> ratings = [[1, 5, 5], [5, 5, 5]]
    >>> average_rating_lists(ratings)
    5.0

    >>> ratings = [[2.56, 4.76, 3.12], [3.1, 4.5, 5], [1.4, 4.54]]
    >>> average_rating_lists(ratings)
    3.17

    >>> average_rating_lists([])
    -1
    """
    
    if len(ratings) == 0 :
        return -1
    else : 
        averages = []
        
        for rates in ratings :
            averages.append(average_rating(rates))
        
        return round(max(averages), 2)

def average_rating_lists_index(ratings):
    """
    Finds the index of the list with the highest average. If there are 
    multiple lists with the same average, return the index of the list 
    that occurs first.
    –
    Parameters:
        ratings: a list of list(s) of numbers ranging from 1 to 10
    --
    Returns:
        The index of the list with the highest average

    >>> ratings = [[1, 5, 5], [5, 5, 5]]
    >>> average_rating_lists_index(ratings)
    1

    >>> ratings = [[2.56, 4.76, 3.12], [1.4, 4.54], [3.1, 4.5, 5]]
    >>> average_rating_lists_index(ratings)
    2

    >>> average_rating_lists_index([])
    -1
    """
    if len(ratings) == 0 :
        return -1
    else : 
        averages = []
        
        for rates in ratings :
            averages.append(round(average_rating(rates), 2))
        
        return averages.index(max(averages))
    
def average_rating_lists_names(ratings, names):
    """
    >>> ratings = [[1, 5, 5], [5, 5, 5]]
    >>> names = ["team1", "team2"]
    >>> average_rating_lists_names(ratings, names)
    'team2'

    >>> ratings = [[2.56, 4.76, 3.12], [1.4, 4.54], [3.1, 4.5, 5]]
    >>> names = ["team1", "team2", "team3"]
    >>> average_rating_lists_names(ratings, names)
    'team3'

    >>> average_rating_lists_names([], [])
    ''
    """
    if len(ratings) == 0 :
        return ""
    else : 
        averages = []
        
        for rates in ratings :
            averages.append(round(average_rating(rates), 2))
        
        return names[averages.index(max(averages))]
    
def new_password(text, number, boolean):
    """
    Creates a password based on the given parameters: text is reversed,
    numbers becomes either even or odd,
    boolean value is flipped
    ---
    Parameters:
    text: a string
    number: an integer
    boolean: a boolean value 
    ---
    Returns:
    Password by concatenating altered components.

    >>> new_password(3, "is", True)
    'ERROR!'
    >>> new_password("paint", "is", False)
    'ERROR!'
    >>> new_password("paint", 40, 20)
    'ERROR!'
    >>> new_password("paint", 18, False)
    'tniap19True'
    >>> new_password("paint", 21, True)
    'tniap42False'
    """
    
    if (type(text) != str) or (type(number) != int) or (type(boolean) != bool) :
        return "ERROR!"
    else :
        reversed_text = ""
        
        for i in range(len(text)-1, -1, -1):
            reversed_text = reversed_text + text[i]
        
        if number%2 != 0 :
            number = number * 2
        else :
            number = number + 1
        
        return reversed_text + str(number) + str(not(boolean))
    
def colors_with_5(all_colors):
    """
    >>> all_colors = ["brown", "red", "green"]
    >>> colors_with_5(all_colors)
    ['brown', 'green']
    >>> all_colors = []
    >>> colors_with_5(all_colors)
    []
    >>> all_colors = ["red", "blue", "orange", "teal"]
    >>> colors_with_5(all_colors)
    []
    """

    colors = []
    
    for color in all_colors :
        if len(color) == 5 :
            colors.append(color)
    
    return colors

def total_for_painting(prices):
    """
    Calculates the total price of paintings given a string of integers.
    --
    Parameters:
        prices: a string of integers
    --
    Returns:
        An integer representing the total of the integers
    >>> prices = "10 20 30 3"
    >>> total_for_painting(prices)
    63

    >>> prices = "1 2 3"
    >>> total_for_painting(prices)
    6

    >>> prices = ""
    >>> total_for_painting(prices)
    0
    """
    
    unity = 1
    current = 0
    numbers = []
    
    for i in range(len(prices) - 1, -1, -1) :
        if prices[i] != " " :
            current = current + int(prices[i]) * unity
            unity = unity * 10
        else :
            numbers.append(current)
            unity = 1
            current = 0
        if i == 0 :
            numbers.append(current)
    
    return sum(numbers)

def test_function():
    assert total_for_painting("10 20 30 3") == 63, "Should be 63"
    assert total_for_painting("1 2 3") == 6, "Should be 6"
    assert total_for_painting("") == 0, "Should be 0"
    assert total_for_painting("100 200 300") == 600, "Should be 600"
    assert total_for_painting("0 0 0") == 0, "Should be 0"
    print("All tests passed!")

test_function()

