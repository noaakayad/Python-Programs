"""
DSC 20 Fall 2024 Homework 06
Name: Noa Wissam Omar Akayad
PID: U10274660
Source: w3school, thinkpython
"""

#Question 1
def randomize(*args):
    """ 
    ##############################################################
    # If there are not arguments, then I return an empty dictionnary.
    
    Else, I take the last element of args and I add the corresponding key-value
    to 'result' which is the dictionnary returned by the function
    without the last element.
    
    Here I do the recursion on the last element because when we add an element
    to a dictionnary, Python will put it at the end of the dictionnary, thus,
    to respect the order of the result that we want, I need to start by the
    end of the dictionnary.#
    ##############################################################

    >>> randomize(1, 2.3, False, 'DSC20')
    {'int': [False], 'float': [2], 'garbage': [False], 'str': ['DC0']}
    >>> randomize(True, 4, 'ABC', -9.8, [1,2,3], 'a', False)
    {'garbage': [True, False], 'int': [True], 'str': ['AC', 'a']\
, 'float': [9.8], 'list': [3]}
    >>> randomize(False, True, 'DS', True, 'abc', -3.2, 5, {'a': 1}, -2, ' .')
    {'garbage': [False, True, True, {'a': 1}], 'str': ['D', 'ac', ' ']\
, 'float': [3.2], 'int': [False, True]}
    >>> randomize()
    {}
    >>> randomize(True)
    {'garbage': [True]}

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> randomize(1, 2, 3, False, True, False, 2.3, 5.3)
    {'int': [False, True, False], 'garbage': [False, True, False]\
, 'float': [2, 5]}
    >>> randomize('Noa', 'Akayad', '21')
    {'str': ['Na', 'Aaa', '2']}
    >>> randomize(1,1,1)
    {'int': [False, False, False]}
    
    """
    # YOUR CODE GOES HERE #
    if not args:
        return {}
    else:
        even = 2
        if isinstance(args[-1], str):
            
            result = randomize(*args[:-1])
            if 'str' in result:
                result['str'].append(args[-1][::even])
            else:
                result['str'] = [args[-1][::even]]
            return result
        
        elif isinstance(args[-1], int) and type(args[-1]) != bool:
            result = randomize(*args[:-1])
            
            if args[-1] % even == 0:
                if 'int' in result:
                    result['int'].append(True)
                else:
                    result['int'] = [True]
            else:
                if 'int' in result:
                    result['int'].append(False)
                else:
                    result['int'] = [False]
            
            return result
        
        elif isinstance(args[-1], float):
            result = randomize(*args[:-1])
            
            if args[-1] < 0:
                if 'float' in result:
                    result['float'].append(-args[-1])
                else:
                    result['float'] = [-args[-1]]
            else:
                if 'float' in result:
                    result['float'].append(int(args[-1]))
                else:
                    result['float'] = [int(args[-1])]
            
            return result
        
        elif isinstance(args[-1], list):
            result = randomize(*args[:-1])
            
            if 'list' in result:
                result['list'].append(len(args[-1]))
            else:
                result['list'] = [len(args[-1])]
                
            return result
        
        else:
            result = randomize(*args[:-1])
            
            if 'garbage' in result:
                result['garbage'].append(args[-1])
            else:
                result['garbage'] = [args[-1]]
            
            return result

#Question 2
def rearrange_args(*args, **kwargs):
    """
    ##############################################################
    # If 'args' and 'kwargs' are empty, then I return an empty list.
    
    Else, if 'kwargs' isn't empty, I take the last element of 'kwargs' because
    thus the length of kwargs - 1 is the number of its keyword. And then I add
    the corresponding tuple to 'return' which is the list returned by the
    function applied on kwargs without its last element.
    
    Else, I do the same logic that I used on kwargs but on args.#
    ##############################################################

    >>> rearrange_args(10, False, player1=[25, 30], player2=[5, 50])
    [('positional_0', 10), ('positional_1', False), \
('keyword_0_player1', [25, 30]), ('keyword_1_player2', [5, 50])]
    >>> rearrange_args('L', 'A', 'N', 'G', L='O', I='S')
    [('positional_0', 'L'), ('positional_1', 'A'), ('positional_2', 'N'), \
('positional_3', 'G'), ('keyword_0_L', 'O'), ('keyword_1_I', 'S')]
    >>> rearrange_args(no_positional=True)
    [('keyword_0_no_positional', True)]

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> rearrange_args(5, 10, 15)
    [('positional_0', 5), ('positional_1', 10), ('positional_2', 15)]
    
    >>> rearrange_args(x=1, y=2, z=3)
    [('keyword_0_x', 1), ('keyword_1_y', 2), ('keyword_2_z', 3)]
    
    >>> rearrange_args(42, test=True, sample='data')
    [('positional_0', 42), ('keyword_0_test', True), \
('keyword_1_sample', 'data')]
    """
    # YOUR CODE GOES HERE #
    if not args and not kwargs :
        return []
    
    elif kwargs :
        result = rearrange_args(*args, **dict(list(kwargs.items())[:-1]))
        return result + [('keyword_' + str(len(kwargs)-1) + '_' +
                          list(kwargs.keys())[-1], list(kwargs.values())[-1])]
    
    else :
        result = rearrange_args(*args[:-1], **kwargs)
        return result + [('positional_' + str(len(args)-1), args[-1])]
        

#Question 3.1
def count_the_password(lst, password):
    """
    ##############################################################
    # If 'lst' is empty then I return 0
    
    Else, if the first element of lst is equal to 'password' then I return
    1 + the result of the function applied on lst without its first element.
    else, I return the result of the function applied on lst without its first
    element#
    ##############################################################

    >>> count_the_password(["cooldragon", "dragon", "gold"], "dragon")
    1
    >>> count_the_password(["DRAGON", "dragon!!"], "dragon")
    0
    >>> count_the_password([], "dragon")
    0
    >>> count_the_password(["dragon "], "dragon")
    0
    >>> count_the_password(["dragon", "likes", "recursions", "right", \
"dragon", "?"], "dragon")
    2

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> count_the_password(["dragon", "dragon", "dragon"], "dragon")
    3
    >>> count_the_password(["Dragon", "dragon", "DRAGON"], "dragon")
    1
    >>> count_the_password(["no", "matches", "here"], "dragon")
    0
    """
    # YOUR CODE GOES HERE #
    if lst == [] :
        return 0
    else :
        if lst[0] == password :
            return 1 + count_the_password(lst[1:], password)
        else :
            return count_the_password(lst[1:], password)

#Question 3.2  
def corrupt_password(input, to_insert):
    """
    ##############################################################
    # If input is empty then I return ''
    
    Else, I return the first element of 'input' plus 'to_insert'
    and plus the string returned by the function applied on input without
    its first element.#
    ##############################################################

    >>> corrupt_password('dragon', '#')
    'd#r#a#g#o#n#'
    >>> corrupt_password('', '@')
    ''
    >>> corrupt_password('I can help', '-')
    'I- -c-a-n- -h-e-l-p-'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> corrupt_password('12345', '*')
    '1*2*3*4*5*'
    >>> corrupt_password('OpenAI', '!')
    'O!p!e!n!A!I!'
    >>> corrupt_password('password', '')
    'password'

    """
    # YOUR CODE GOES HERE #
    if input == '' :
        return ''
    else :
        return input[0] + to_insert + corrupt_password(input[1:], to_insert)

# Question 3.3
def outsmart_dragon(lst, password, to_insert):
    """
    ##############################################################
    # If 'lst' is empty then I return []
    
    Else, if the first element of lst is different than password then I add
    the result of corrupt_password on the first element of lst to the result of
    the function applied on lst without its first element.
    else, I add 'password' to the result of the function applied on lst without
    its first element #
    ##############################################################

    >>> outsmart_dragon(['dragon'], 'dragon','#')
    ['dragon']
    >>> outsmart_dragon([], 'dragon','@')
    []
    >>> outsmart_dragon(['help me', 'dragon'], 'dragon','-')
    ['h-e-l-p- -m-e-', 'dragon']
    >>> outsmart_dragon(['help me', 'dear dragon'], 'dragon','-')
    ['h-e-l-p- -m-e-', 'd-e-a-r- -d-r-a-g-o-n-']
    >>> outsmart_dragon(['DrAgOn', 'Dragon'], 'dragon','-')
    ['D-r-A-g-O-n-', 'D-r-a-g-o-n-']

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> outsmart_dragon(['dragon', 'slayer'], 'dragon', '*')
    ['dragon', 's*l*a*y*e*r*']
    >>> outsmart_dragon(['dragon', 'dragon', 'dragon'], 'dragon', '%')
    ['dragon', 'dragon', 'dragon']
    >>> outsmart_dragon(['escape', 'from', 'dragon'], 'dragon', '-')
    ['e-s-c-a-p-e-', 'f-r-o-m-', 'dragon']

    """
    # YOUR CODE GOES HERE #
    if lst == [] :
        return []
    else :
        if lst[0] != password :
            return [corrupt_password(lst[0], to_insert)] + \
                   outsmart_dragon(lst[1:], password, to_insert)
        else :
            return [password] + outsmart_dragon(lst[1:], password, to_insert)

#Question4
def corrupt_with_vowels(input):
    """
    ##############################################################
    # If input is empty then I return ''
    
    Else, if the first element of input isn't a vowel then I return the first
    element of 'input' plus 'to_insert'
    else, I return the result of the function applied on input without
    its first element. #
    ##############################################################

    >>> corrupt_with_vowels('buy and sell')
    'by nd sll'
    >>> corrupt_with_vowels('gold gold gold')
    'gld gld gld'
    >>> corrupt_with_vowels('AeI oU')
    ' '

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> corrupt_with_vowels('The quick brown fox')
    'Th qck brwn fx'
    >>> corrupt_with_vowels('HELLO WORLD')
    'HLL WRLD'
    >>> corrupt_with_vowels('corrupt_with_vowels')
    'crrpt_wth_vwls'
    """
    # YOUR CODE GOES HERE #
    if input == '' :
        return ''
    else :
        if input[0] not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] :
            return input[0] + corrupt_with_vowels(input[1:])
        else :
            return corrupt_with_vowels(input[1:])

#Question 5
def where_to_go(point1, point2, separator):
    """
    ##############################################################
    # If point1 == point2 then I return point1 casted as a string.
    
    Else, if point1 < point2 then I return str(point1) plus the separator
    and plus the string resulted by the function applied on point1 + 1.
    Else, I do the same but I apply the function on point1 - 1#
    ##############################################################

    >>> where_to_go(17, 17, 'left')
    '17'
    >>> where_to_go(1, 8, ',')
    '1,2,3,4,5,6,7,8'
    >>> where_to_go(8, 1, '->')
    '8->7->6->5->4->3->2->1'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> where_to_go(5, 5, '-')
    '5'
    >>> where_to_go(3, 6, '->')
    '3->4->5->6'
    >>> where_to_go(10, 5, '|')
    '10|9|8|7|6|5'

    """
    # YOUR CODE GOES HERE #
    if point1 == point2 :
        return str(point1)
    else :
        if point1 < point2 :
            return str(point1) + separator + \
                   where_to_go(point1 + 1, point2, separator)
        else :
            return str(point1) + separator + \
                   where_to_go(point1 - 1, point2, separator)
        
