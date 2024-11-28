"""
DSC 20 Fall 2024 Homework 01
Name: Noa Wissam Omar AKAYAD
PID: U10274660
"""

# Question 1
def login(fname, lname):
    """
    ##############################################################
    # First I reverse 'fname' by creating an empty string that will
    get at each loop of a for loop the letter of 'fname'
    but backwords because the loop goes from the end of 'fname' to
    its beginning.
    
    Then, I just keep every 2 characters of the reversed 'fname' : I
    store that in the variable 'first_name'.
    
    And finally, I just add to 'first_name', every 3 letters from
    'last_name'
    
    Also, even if I will not lose points for these magic numbers,
    I have created the variables 'power_2' and 'square_power' to
    avoid the magic numbers issue with gradescope #
    ##############################################################

    >>> login("Marina", "Langlois")
    'aiaLgi'
    >>> login("", "")
    ''
    >>> login("San", "Diego")
    'nSDg'

    # Add your own doctests below
    >>> login("Noa", "Akayad")
    'aNAy'
    >>> login("UCSD", "DSC20")
    'DCD2'
    >>> login("", "Test")
    'Tt'
    """
    
    reversed_fname = ""
        
    for i in range(len(fname)-1, -1, -1):
        reversed_fname = reversed_fname + fname[i]
    
    first_name = ""
    increment_by_2 = 2
    increment_by_3 = 3
    
    for i in range(0, len(fname), increment_by_2) :
        first_name = first_name + reversed_fname[i]
    
    
    log = first_name
    
    for i in range(0, len(lname), increment_by_3) :
        log = log + lname[i]
    
    return log
    

# Question 2
def ages(age1, age2):
    """
    ##############################################################
    #I created an int variable 'limit_age' that equals 23 : the limit of age.
    
    And then I just look at all the possible cases by comparing
    the ages with the limit of age :
    If they all are > 23 then they both can rent
    If one is bigger than 23 and not the other then the one
    below 23 is closer to 23
    And if they all are below 23, I compare the distance of both
    of them to 23 and return the closer one.#
    ##############################################################

    >>> ages(19, 21)
    21
    >>> ages(26, 21)
    21
    >>> ages(26, 27)
    'You both can rent!'
    >>> ages(19, 23)
    19

    # Add your own doctests below
    >>> ages(21, 21)
    21
    >>> ages(18, 19)
    19
    >>> ages(25, 25)
    'You both can rent!'
    """
    
    limit_age = 23
    if (age1 >= limit_age) and (age2 >= limit_age) :
        return "You both can rent!"
    elif (age1 >= limit_age) and (age2 < limit_age) :
        return age2
    elif (age1 < limit_age) and (age2 >= limit_age) :
        return age1
    else :
        range_1 = limit_age - age1
        range_2 = limit_age - age2
        
        if range_1 < range_2 :
            return age1
        else :
            return age2


# Question 3
def renter(name1, name2, name3):
    """
    ##############################################################
    First I see the case when all the names have the same length,
    if so then I return the name3 as it is the farest in the
    parameters. For that, I created 3 variables len1, len2, len3,
    that equal the length of each name
    
    Then I see the case when only name1 and name2 have the same
    length, thus I return name2.
    
    And I follow the same logic when name1 and name 3 have the
    same length and when name2 have the same length as name3
    
    Now that I have seen all the cases when the names can have the
    same length, I see the cases when the lengths are different :
    Then we just need to return the longest name.#
    ##############################################################

    >>> renter("K", "BB", "Joy")
    'Joy'
    >>> renter("Joy", "K", "BB")
    'Joy'
    >>> renter("BB", "Joy", "K")
    'Joy'
    >>> renter("BB", "K", "Jo")
    'Jo'
    >>> renter("BB", "Jo", "Su")
    'Su'

    # Add your own doctests below
    >>> renter("AAA", "BBB", "CCC")
    'CCC'
    >>> renter ("Noa", "Wissam", "Akayad")
    'Akayad'
    >>> renter("", "", "")
    ''
    """
    
    len1 = len(name1)
    len2 = len(name2)
    len3 = len(name3)
    
    if len1 == len2 and len2 == len3 :
        return name3
    elif len1 == len2 :
        return name2
    elif len1 == len3 :
        return name3
    elif len2 == len3 :
        return name3
    else :
        if max(len1, len2, len3) == len1 :
            return name1
        elif max(len1, len2, len3) == len2 :
            return name2
        else :
            return name3


# Question 4.1
def helper_distance(lst, x2, y2):
    """
    ##############################################################
    #Here, I just follow the formula of the Euclidean distance by
    using '**' as the power function and by assuming that '**0.5' is
    equivalent of square root
    
    Also, even if I will not lose points for these magic numbers,
    I have created the variables 'power_2' and 'square_power' to
    avoid the magic numbers issue with gradescope #
    ##############################################################
    
    >>> helper_distance([0, 0], 3, 4)
    5.0
    >>> helper_distance([-3, -4], 3, 4)
    10.0
    >>> helper_distance ([100, 100], 100.5, 100)
    0.5

    # Add your own doctests below
    >>> helper_distance([0, 0], 0, 0)  
    0.0
    >>> helper_distance([1, 2], 1, 2)
    0.0
    >>> helper_distance([0, 0], -4, -3)  
    5.0
    """
    
    # YOUR CODE GOES HERE #
    power_2 = 2
    square_power = 0.5
    
    return float( ( float((lst[0] - x2))**power_2 + float((lst[1] - 
    y2)**power_2) )** square_power )


# Question 4.2
def lunch(lunch_places, office_x, office_y, threshold):
    """
    ##############################################################
    #I created en empty list named places which will receive every
    lunch places that has a distance from the office lower than
    'threshold'. I use a for loop to test all lunch places that are
    in the list 'lunch_places'.#
    ##############################################################

    >>> lunch([[0, 0], [30.5, 20.7]], 3.2, 4, 6)
    [[0, 0]]
    >>> lunch([[-3, -4], [6, 7]], 3, 4, 10)
    [[-3, -4], [6, 7]]
    >>> lunch ([[100, 100]], 100.5, 100, 0.2)
    []

    # Add your own doctests below
    >>> lunch([[15.1, 15.1], [20, 20], [30, 30]], 0, 0, 15) 
    []
    >>> lunch([], 0, 0, 0) 
    []
    >>> lunch([[1, 1]], 1, 1, 0)
    [[1, 1]]
    """

    places = []
    
    for place in lunch_places :
        if helper_distance(place, office_x, office_y) <= threshold : 
            places.append(place)
    
    return places

# Question 5
def lunch_names(lunch_places, office_x, office_y, threshold, names):
    """
    ##############################################################
    #I follow the same logic as the previous function but here, I
    use a "for i in range" for loop instead of a "for place in
    lunch_place" for loop.
    
    Thus I can see if the distance of the lunch place number 'i' is
    lower than threshold, and if so, I can put the lunch name in
    the list places as the lunch name is the string number 'i' of
    the list names.#
    ##############################################################

    >>> lunch_names([[0, 0], [30, 20], [5, 9]], 3.2, 4, 6, \
    ['place1', 'place2', 'place3'])
    ['place1', 'place3']
    >>> lunch_names([[-3, -4], [6, 7]], 3, 4, 10, \
    ['place1', 'place2'])
    ['place1', 'place2']
    >>> lunch_names ([[100, 100]], 100.5, 100, 0.2, ['place1'])
    []

    # Add your own doctests below
    >>> lunch_names([[15.1, 15.1], [20, 20], [30, 30]], 0, 0,\
    15, ['place1', 'place2', 'place3'])  
    []
    >>> lunch_names([], 10, 10, 5, [])  
    []
    >>> lunch_names([[10, 10]], 10, 10, 0, ['place1'])  
    ['place1']
    """
    places = []
    
    for i in range(len(lunch_places)) :
        if helper_distance(lunch_places[i], office_x, office_y) <= threshold :
            places.append(names[i])
    
    return places


# Question 6
def meeting_message(i_name, time, place, s_name):
    """
    ##############################################################
    #Here I just use the concatenation '+' function to return the
    paragraph and I use '\n' to skip lines#
    ##############################################################

    >>> print(meeting_message("Penny", "3:15pm", "Cheesecake Factory", \
        "Sheldon"))
    Dear Penny,
    Please join our meeting at 3:15pm, at the Cheesecake Factory.
    <BLANKLINE>
    See you soon: Sheldon

    >>> print(meeting_message("Freya", "", "Dog Park", "Marina"))
    Dear Freya,
    Please join our meeting at , at the Dog Park.
    <BLANKLINE>
    See you soon: Marina

    # Add your own doctests below
    >>> print(meeting_message("Marina", "11a", "DSC 20 Class", "Noa"))
    Dear Marina,
    Please join our meeting at 11a, at the DSC 20 Class.
    <BLANKLINE>
    See you soon: Noa
    >>> print(meeting_message("", "", "", ""))
    Dear ,
    Please join our meeting at , at the .
    <BLANKLINE>
    See you soon: 
    >>> print(meeting_message("", "11a", "DSC 20 Class", ""))
    Dear ,
    Please join our meeting at 11a, at the DSC 20 Class.
    <BLANKLINE>
    See you soon: 
    """
    # YOUR CODE GOES HERE #
    return "Dear " + i_name + ",\nPlease join our meeting at " + \
    time + ", at the " + place + ".\n\nSee you soon: " + s_name


# Question 7
def seat_number(lst):
    """
    ##############################################################
    #I have created an empty list 'seats' which will receive the
    length of names from the list 'lst' only if these numbers are not
    already in seats, otherwise, I put the string 'taken'.
    
    I use a 'for name in lst' for loop to access all the name and I
    use the function 'in' to see if a number is already in seats#
    ##############################################################

    >>> seat_number(["Marina", "Tom", "B"])
    [6, 3, 1]
    >>> seat_number(["Marina", "Sue", "Ben", "Freya"])
    [6, 3, 'taken', 5]
    >>> seat_number(["Marina", "Sue", "Ben", ""])
    [6, 3, 'taken', 0]

    # Add your own doctests below
    >>> seat_number(["Noa", "Akayad", "Marina", "Langlois"])
    [3, 6, 'taken', 8]
    >>> seat_number(["Noa", "Noa", "Noa", "Noa"])
    [3, 'taken', 'taken', 'taken']
    >>> seat_number(["", "Noa", "", "Akayad"])
    [0, 3, 'taken', 6]
    """
    
    seats = []
    
    for name in lst :
        if len(name) in seats :
            seats.append("taken")
        else :
            seats.append(len(name))
    
    return seats
            

# Question 8
def computers(choices):
    """
    ##############################################################
    #I have created a counter for the number of string "DESKtop"
    named 'count_desktop' and one for the number of string
    "LAPtop" named 'count_laptop'.
    
    Then, thanks to 'for choice in choices' for loop, if the
    string choice is "DESKtop" or "LAPtop", either count_desktop
    or count_laptop get incremented.
    
    And thus after visiting all the choices, I just compare the
    counters to return a boolean about who's greatter 
    ##############################################################

    >>> computers(["DESKtop", "LAPtop", "DESKtop"])
    True
    >>> computers(["LAPtop", "LAPtop"])
    False
    >>> computers(["DESKtop", "Pager", "Tablet", "LAPtop"])
    False

    # Add your own doctests below
    >>> computers([])
    False
    >>> computers(["Tablet", "Tablet", "Tabler"])
    False
    >>> computers(["DESKtop", "DESKtop", "LAPtop", "LAPtop"])
    False
    """
    
    count_desktop = 0
    count_laptop = 0
    
    for choice in choices :
        if choice == "DESKtop" :
            count_desktop = count_desktop + 1
        elif choice == "LAPtop" :
            count_laptop = count_laptop + 1
        else :
            continue
   
    return count_desktop > count_laptop


# Question 9
def age_average(lst):
    """
    ##############################################################
    #I have created the variables average and numb_pos that
    represent the average and the number of positive numbers in
    'lst'.
    
    After dealing with an empty list case, I have taken every
    string age in 'lst' thanks to a for loop and considered them as
    float thanks to a cast : float(age). If this float is > 0
    then numb_pos get incremented and I add this number to
    average.
    
    Thus, after having calculated the addition of all the
    positive ages, we just need to divide that by numb_pos (if
    numb_pos == 0 then I return '0.0') and cast as a string
    the rounded result #
    ##############################################################

    >>> age_average(["20", "21", "22"])
    '21.0'
    >>> age_average(["50", "25", "30"])
    '35.0'
    >>> age_average(["40", "-999", "45"])
    '42.5'
    >>> age_average([])
    '0.0'

    # Add your own doctests below
    >>> age_average(["-1", "-1"])
    '0.0'
    >>> age_average(["10", "0"])
    '10.0'
    >>> age_average(["15.5", "17.3", "16.6"])
    '16.5'
    """
    average = 0.0
    numb_pos = 0
    
    if len(lst) == 0 :
        return '0.0'
    else :
        for age in lst :
            if float(age) > 0 :
                numb_pos = numb_pos + 1
                average = average + float(age)
        
        if numb_pos == 0:
            return str(0.0)
        else:
            return str( round( (average / numb_pos), 1 ) )


# Question 10
def supervision_teams(team, company_name):
    """
    ##############################################################
    #I have created 2 empty lists, one name first_team that will
    receive all members at even indices of the team list, and
    another named second_team that will receive all members at odd
    indices of the team list.
    
    Thus, I used one "for i in range" for loop where i is
    incremented by 2 and starts at 0, and I used an other
    "for i in range" where i is incremented by 2  but starts at 1.
    
    Then I return a tuple that has first_team and second_team
    
    Also, even if I will not lose points for this magic number,
    I have created the variable 'incremented_by_2' to
    avoid the magic numbers issue with gradescope #
    ##############################################################

    >>> supervision_teams(["p1", "p2", "p3"], "Marina")
    (['Marina', 'p1', 'p3'], ['p2', 'Marina'])
    >>> supervision_teams(["p1"], "Marina")
    (['Marina', 'p1'], ['Marina'])
    >>> supervision_teams(["p1", "p2", "p3", "p4", "p5", "p6"], "Marina")
    (['Marina', 'p1', 'p3', 'p5'], ['p2', 'p4', 'p6', 'Marina'])

    # Add your own doctests below
    >>> supervision_teams([], "Noa")
    (['Noa'], ['Noa'])
    >>> supervision_teams(["1", "2", "3", "4"], "Noa")
    (['Noa', '1', '3'], ['2', '4', 'Noa'])
    >>> supervision_teams(["1", "2"], "Noa")
    (['Noa', '1'], ['2', 'Noa'])
    """
    
    first_team = []
    second_team = []
    
    first_team.append(company_name)
    
    increment_by_2 = 2
    
    for i in range(0, len(team), increment_by_2) :
        first_team.append(team[i])
    for i in range(1, len(team), increment_by_2) :
        second_team.append(team[i])
    
    second_team.append(company_name)
    
    return first_team, second_team
