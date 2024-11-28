"""
DSC 20 Fall 2024 Homework 05
Name: Noa Wissam Omar Akayad
PID: U10274660
Source: w3school
"""

# Question 1

def get_qualified_customers(data, max_avg, min_range):
    """
    ##############################################################
    # First I verify that data is a dictionnary that has the right type for
    its keys and values, and I verify that max_avg and min_range are positive
    integers.
    
    I first create a dictionnary comprehension where for each key I put the
    mean of its list value if it doesn't have duplicated integers and if its
    not empty, otherwise I put either None if it has dupplicated values
    or 0 if its empty
    
    I do the same with the range in 'dct_range'
    
    And thus I just need to create a list comprehension where I only put in
    this list the keys from data who has a value in 'dct_avg' that is not None
    and that is lesser or equal than 'max_avg', and that has a range greater
    or equal than 'min_range'#
    ##############################################################

    >>> data = { \
        "Jayden": [10, 10, 10, 10, 10], \
        "Terry": [1, 2, 3, 4, 5, 6, 7, 8], \
        "Austin": [10, 11, 12, 13, 14], \
        "Noah": [2, 3, 4, 5] \
    }
    >>> get_qualified_customers(data, 11, 5)
    ['Terry']

    >>> data = { \
        "Caleb": [0, 1, 2, 3, 4, 5], \
        "Keenan": [8, 9, 10], \
        "Rome": [7, 8, 9], \
        "Khalil": [] \
    }
    >>> get_qualified_customers(data, 9, 2)
    ['Caleb', 'Keenan', 'Rome']

    # Add at least 3 doctests below here #
    
    >>> data = { \
        "Alice": [5, 7, 5, 7, 5, 7], \
        "Bob": [15, 20, 25], \
        "Charlie": [1, 2, 3], \
        "David": [] \
    }
    >>> get_qualified_customers(data, 30, 5)
    ['Bob']

    >>> data = { \
        "Emma": [6, 6, 6, 6, 6], \
        "Sophia": [3, 4, 5, 6, 7], \
        "Olivia": [8, 8, 8], \
        "Liam": [2, 3, 4] \
    }
    >>> get_qualified_customers(data, 7, 2)
    ['Sophia', 'Liam']

    >>> data = { \
        "Isabella": [9, 10, 11], \
        "Ethan": [2, 4, 6, 8], \
        "Mia": [12, 14, 16, 18], \
        "Lucas": [1, 3, 5, 7, 9] \
    }
    >>> get_qualified_customers(data, 10, 4)
    ['Ethan', 'Lucas']
    """
    # YOUR CODE GOES HERE #
    assert isinstance(data, dict)
    assert all(isinstance(key, str) and isinstance(value, list)
               for key,value in data.items())
    assert all(isinstance(i, int) for value in data.values() for i in value)
    assert isinstance(max_avg, int) and max_avg >= 0
    assert isinstance(min_range, int) and min_range >= 0
    
    dct_avg = {key : sum(value)/len(value) if value != [] and
                               len(set(value)) == len(value)
               else None if len(set(value)) != len(value)
               else 0 for key, value in data.items()}
            
    dct_range = {key : max(value) - min(value) if value != [] and
                               len(set(value)) == len(value)
                 else None if len(set(value)) != len(value)
                 else 0 for key, value in data.items()}
    return [key for key in data if dct_avg[key] != None
            and dct_avg[key]<= max_avg
            and dct_range[key] != None
            and dct_range[key] >= min_range]
    


# Question 2

def message_to_customers(customer_file, decision, message):
    """
    ##############################################################
    # After verifying that the 3 parameters have the right type,
    I create an empty list named 'result'.
    
    The I open 'customer_file' as reader on read mode and for each line of
    'customer_file', I the list 'line' that contains every words from the
    current line and I verify that it has the right format.
    
    If so, if the decision in this line is the same as the on in the parameters
    then I add the corresponding string to 'result'.
    
    Finally, I return 'result'.#
    ##############################################################

    >>> msg = "unfortunately we cannot work with you."
    >>> message_to_customers("files/customers.txt", "w", msg)
    ['(to: steve@apple.com) Dear Steve at Apple, \
unfortunately we cannot work with you.', \
'(to: jensen@nvidia.com) Dear Jensen at NVIDIA, \
unfortunately we cannot work with you.']

    >>> msg = "we are excited to work with you!"
    >>> message_to_customers("files/customers.txt", "s", msg)
    ['(to: jeff@amazon.com) Dear Jeff at Amazon, \
we are excited to work with you!', \
'(to: mark@fb.com) Dear Mark at Facebook, \
we are excited to work with you!']

    # Add at least 3 doctests below here #
    >>> msg = "we are excited to work with you!"
    >>> message_to_customers("files/customers2.txt", "s", msg)
    ['(to: noa@nike.com) Dear Noa at Nike, \
we are excited to work with you!']

    >>> msg = "we are excited to work with you!"
    >>> message_to_customers("files/customers2.txt", "w", msg)
    []
    
    >>> msg = "we are excited to work with you!"
    >>> message_to_customers("files/customers2.txt", "a", msg)
    Traceback (most recent call last):
    ...
    AssertionError

    """
    # YOUR CODE GOES HERE #
    assert isinstance(customer_file, str)
    assert isinstance(decision, str)
    assert decision == 's' or decision == 'w'
    assert isinstance(message, str)
    
    result = []
    
    with open(customer_file) as reader :
        lines = reader.readlines()
        decision_customer = 3
        mail_customer = 2
        for line in lines :
            line = line.strip().split(',')
            assert len(line) == 4
            if line[decision_customer] == decision :
                result.append('(to: '+line[mail_customer]+') Dear '+line[1]+
                              ' at '+line[0]+', '+message)
        
        return result
            


# Question 3

def forge_votes(vote_file):
    """
    ##############################################################
    # Here I first open vote_file as reader in a read mode, then I open
    'forged' as a writer nested into the first with open.
    
    Then I create 'lines' which is a list containing every lines of vote_file.
    
    Then I create numb_0 et numb_1 that are intergers that first equal to 0.
    Then I create the list 'list_1' that is a list that has either 1 at index i
    if the ith line has '1' or 0 otherwise.
    And I do the same with 'list_0'.
    Thus 'numb_0' is the sum of 'list_0' and idem for 'numb_1' and 'list_1'.
    
    Thus, if there is a majority of '0',
    I first calcul the numbers of lines that we need to change :
    'remain = remain = (numb_0 - numb_1)//2 + 1' and I create the list
    'lines_with_0' that contains all the indexes of 'lines' that has a '0'.
    and thus I create 'lines_to_change' that only contains the first 'remain'
    elements of 'lines_with_0', so now I know which lines I need to change.
    So I rewrite all these lines in 'lines' and I write them in 'forged'.
    
    And if we first had a majority of '1', then I just copy every line from
    lines in 'forged'.
    ##############################################################

    >>> forge_votes("files/vote1.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Patrick,1
    Travis,0
    Clyde,1
    Andy,1

    >>> forge_votes("files/vote2.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Maxx,1
    Tre,1
    Jakobi,0

    >>> forge_votes("files/vote3.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Andy,1

    # Add at least 3 doctests below here #
    >>> forge_votes("files/vote4.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Noa,1
    Sami,0
    Adame,1
    
    >>> forge_votes("files/vote5.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Noa,1
    Sami,0
    Adame,1
    
    >>> forge_votes("files/vote6.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Noa,1
    Sami,1
    Adame,0
    """
    # YOUR CODE GOES HERE #
    with open(vote_file) as reader :
        with open("files/forged.txt", 'w') as writer :
            lines = reader.readlines()
            numb_1 = 0
            numb_0 = 0
            
            list_with_1 = [1 if '1' in line else 0 for line in lines]
            list_with_0 = [1 if '0' in line else 0 for line in lines]
            numb_1 = sum(list_with_1)
            numb_0 = sum(list_with_0)
            
            
            if numb_0 >= numb_1 :
                half = 2
                remain = (numb_0 - numb_1)//half + 1
                lines_with_0=[i for i in range(len(list_with_0))
                              if list_with_0[i]==1]
                lines_to_change = lines_with_0[:remain]
                lines = [lines[i].split(',')[0] + ',' + '1\n'
                         if i in lines_to_change
                         else lines[i] for i in range(len(lines))]
                writer.write(''.join(map(str, lines)))
                
            else :
                writer.write(''.join(map(str, lines)))
                
    
# Question 4

def complexity_tf():
    """
    Write your answers to time complexity True/False questions in this
    function. No new doctests required.

    >>> answers = complexity_tf()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, bool) for ans in answers])
    True
    """
    # REPLACE ... WITH YOUR ANSWERS (True/False) #
    return [True, True, False, True, False, True, False, True, False, False]

