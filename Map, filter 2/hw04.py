"""
DSC 20 Fall 2024 Homework 04
Name: Noa Wissam Omar AKAYAD
PID: U10274660
Source: N/A
"""

# Question 1
def place_of_birth(file_in):
    """
    ##############################################################
    # I open the file as a reader and I create 'lines' which his a list
    having for every line of the file a string representing this line thanks
    to the function 'readlines()'.
    
    Then I create an empty dictionnary named 'place_birth' and for every string
    from 'lines', I create 'city' which is the second element of my string,
    and I create 'name' which is the first element of my string,
    and if 'city' isn't already a key of my dictionnary, then I had 'city'
    as a key and '[name]' as its value, and otherwise, I add name to the value
    (list) of the key 'city'.
    
    And I return the dictionnary.#
    ##############################################################

    >>> place_of_birth('files/info_1.txt')
    {'Chicago': ['Rob'], 'New York': ['Ella'], 'New York.': ['Mary']}
    >>> place_of_birth('files/info_2.txt')
    {'Chicago': ['Rob'], 'London': ['Ezra'], 'Paris': \
['Mary'], 'paris': ['Ron', 'Harry']}
    >>> place_of_birth('files/header.txt')
    {}

    # Add at least 3 doctests below here #
    >>> place_of_birth('files/info_3.txt')
    {'San Diego': ['Sue'], 'London': ['Ben']}
    >>> place_of_birth('files/info_4.txt')
    {'Paris': ['Kate']}
    >>> place_of_birth('files/info_5.txt')
    {'Paris': ['Noa'], 'Tunis': ['Nordine'], 'Agadir': ['Sami']}
    """
    with open(file_in) as reader :
        lines = reader.readlines()
        
        place_birth={}
        
        for i in range(1, len(lines)) :
            line = lines[i]
            infos = line.split(',')
            city = infos[1].strip()
            name = infos[0].strip()
            
            if city in place_birth.keys() :
                place_birth[city].append(name)
            else :
                place_birth[city] = [name]
        
        return place_birth


# Question 2
def age_groups(file_in, file_out):
    """
    ##############################################################
    # Here I use a nested 'with open' where I open 'file_in' as a reader
    and 'file_out' as a writer.
    
    Then, I look at each line of 'file_in' thanks to a for loop on 'lines'
    which is the list I have created thanks to 'reader.readlines()'.
    
    For each line, I separate each word and put them on a list named 'infos'
    thanks to 'split(',')' and thus I have a list of strings where each string
    represent a word from my line.
    
    Thus, infos[0] has the name of the person and infos[2] has date of birth
    of this person as 'MM/DD/YYYY'.
    Thus to calculate the age of the person, I split infos[2] for every '/'
    and I put the string numbers in a list named 'dob'. So, the age is equal
    to 2024 - int(dob[2]).
    
    And thus, I just compare the age and 35 to see what to write in 'file_out'.
    ##############################################################

    >>> age_groups('files/info_1.txt', 'files/age_1_out.txt')
    >>> with open('files/age_1_out.txt', 'r') as outfile1:
    ...    for line in outfile1:
    ...       print(line.strip())
    name,older than 35
    Rob,-1
    Ella,1
    Mary,-1
    
    >>> age_groups('files/info_2.txt', 'files/age_2_out.txt')
    >>> with open('files/age_2_out.txt', 'r') as outfile2:
    ...    for line in outfile2:
    ...       print(line.strip())
    name,older than 35
    Rob,-1
    Ezra,1
    Mary,1
    Ron,0
    Harry,0

    >>> age_groups('files/header.txt', 'files/empty_out.txt')
    >>> with open('files/empty_out.txt', 'r') as outfile:
    ...    for line in outfile:
    ...       print(line.strip())
    name,older than 35

    # Add at least 3 doctests below here #
    >>> age_groups('files/info_3.txt', 'files/age_3_out.txt')
    >>> with open('files/age_3_out.txt', 'r') as outfile3:
    ...    for line in outfile3:
    ...       print(line.strip())
    name,older than 35
    Sue,-1
    Ben,1
    >>> age_groups('files/info_4.txt', 'files/age_4_out.txt')
    >>> with open('files/age_4_out.txt', 'r') as outfile4:
    ...    for line in outfile4:
    ...       print(line.strip())
    name,older than 35
    Kate,1
    >>> age_groups('files/info_5.txt', 'files/age_5_out.txt')
    >>> with open('files/age_5_out.txt', 'r') as outfile5:
    ...    for line in outfile5:
    ...       print(line.strip())
    name,older than 35
    Noa,-1
    Nordine,1
    Sami,1
    """
    with open(file_in, 'r') as reader :
        with open(file_out, 'w') as writer :
            lines = reader.readlines()
            writer.write("name,older than 35\n")
            limit = 35
            last_index = 2
            this_year = 2024
            
            for i in range(1, len(lines)) :
                    line = lines[i]
                    infos = line.split(',')
                    name = infos[0].strip()
                    dob = infos[last_index].split('/')
                    
                    if this_year - int(dob[last_index]) < limit :
                        writer.write(name + ",-1\n")
                    elif this_year - int(dob[last_index]) == limit :
                        writer.write(name + ",0\n")
                    else :
                        writer.write(name + ",1\n")

# Question 3
def several_files(files_lst, file_out):
    """
    ##############################################################
    # First, I create a dictionnary named 'month' where the keys are strings
    that go from '01' to '12' and each value represent the month of the key
    for example month['01'] = 'Jan'.
    
    Then I open 'file_out' as a writer
    
    then for each 'file_in' of 'files_lst', I open it as a reader with a for
    loop
    
    Then, I look at each line of 'file_in' thanks to a for loop on 'lines'
    which is the list I have created thanks to 'reader.readlines()'.
    
    For each line, I separate each word and put them on a list named 'infos'
    thanks to 'split(',')' and thus I have a list of strings where each string
    represent a word from my line.
    
    Thus, infos[0] has the name of the person and infos[2] has date of birth
    of this person as 'MM/DD/YYYY'.
    Thus to calculate the age of the person, I split infos[2] for every '/'
    and I put the string numbers in a list named 'dob'.
    
    And thus, I just to write in writer the name + the city + the value of the
    key of 'month' for the first element of 'dob' as it is the month,
    the second element of dob and finally the third element of dob#
    ##############################################################

    >>> lst_1 = ['files/info_1.txt','files/info_3.txt', 'files/info_4.txt']
    >>> several_files(lst_1, 'files/several_1_out.txt')
    >>> with open('files/several_1_out.txt', 'r') as outfile1:
    ...    for line in outfile1:
    ...       print(line.strip())
    name,city,DOB
    Rob,Chicago,Oct 10 2010
    Ella,New York,Apr 09 1970
    Mary,New York.,Jan 01 2004
    Sue,San Diego,Mar 19 2015
    Ben,London,Dec 08 1970
    Kate,Paris,Jul 13 1945

    >>> lst_2 = ['files/info_2.txt','files/header.txt']
    >>> several_files(lst_2, 'files/several_2_out.txt')
    >>> with open('files/several_2_out.txt', 'r') as outfile2:
    ...    for line in outfile2:
    ...       print(line.strip())
    name,city,DOB
    Rob,Chicago,Oct 10 2010
    Ezra,London,Apr 12 1978
    Mary,Paris,Sep 11 1975
    Ron,paris,Nov 11 1989
    Harry,paris,Dec 15 1989


    # Add at least 3 doctests below here #
    >>> lst_3 = ['files/info_2.txt','files/info_3.txt']
    >>> several_files(lst_3, 'files/several_3_out.txt')
    >>> with open('files/several_3_out.txt', 'r') as outfile3:
    ...    for line in outfile3:
    ...       print(line.strip())
    name,city,DOB
    Rob,Chicago,Oct 10 2010
    Ezra,London,Apr 12 1978
    Mary,Paris,Sep 11 1975
    Ron,paris,Nov 11 1989
    Harry,paris,Dec 15 1989
    Sue,San Diego,Mar 19 2015
    Ben,London,Dec 08 1970
    
    >>> lst_4 = ['files/info_3.txt','files/info_4.txt']
    >>> several_files(lst_4, 'files/several_4_out.txt')
    >>> with open('files/several_4_out.txt', 'r') as outfile4:
    ...    for line in outfile4:
    ...       print(line.strip())
    name,city,DOB
    Sue,San Diego,Mar 19 2015
    Ben,London,Dec 08 1970
    Kate,Paris,Jul 13 1945
    
    >>> lst_5 = ['files/info_4.txt','files/info_5.txt']
    >>> several_files(lst_5, 'files/several_5_out.txt')
    >>> with open('files/several_5_out.txt', 'r') as outfile5:
    ...    for line in outfile5:
    ...       print(line.strip())
    name,city,DOB
    Kate,Paris,Jul 13 1945
    Noa,Paris,Jan 18 2003
    Nordine,Tunis,Apr 12 1978
    Sami,Agadir,Sep 11 1975
    """
    month = {
                "01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr", 
                "05": "May", "06": "Jun", "07": "Jul", "08": "Aug", 
                "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"
            }
    
    dob_index = 2
    
    with open(file_out, 'w') as writer :
        writer.write("name,city,DOB\n")
        for file_in in files_lst :
            with open(file_in, 'r') as reader :
                lines = reader.readlines()
                
                for i in range(1, len(lines)) :
                        line = lines[i]
                        infos = line.split(',')
                        name = infos[0].strip()
                        city = infos[1].strip()
                        dob = infos[dob_index].split('/')
                        writer.write(name+',' + city + ',' +
                                     month[dob[0].strip()] + ' ' +
                                     dob[1].strip() + ' ' +
                                     dob[dob_index].strip() + '\n')



# Question 4
def postcards(info_list):
    """
    ##############################################################
    # First I verify that 'info_list' is a list
    Then I verify that all elements in 'info_list' are tuples
    Then I verify that they all have a lenght of 4
    Then I verify if the elements in the tuples have the right type
    
    Then I first filter info list, so I only take the tuples with a
    price lower than 75.
    Then I map this result by returning for each tuple, a tuple of length 2
    that has first the name of the person, and then the asked result.
    And I cast this map into a dictionnary has we have a map of tuples of
    length 2.#
    ##############################################################

    >>> postcards([
    ...     ('Yue Wang', 96, 18, 'Hoover Dam'),
    ...     ('Cleo Patra', 10, 32, 'Bellagios')
    ... ])
    {'Cleo Patra': 'cle32patra0soigalleb'}
    >>> postcards([])
    {}
    >>> postcards([
    ...     ('Mari Noh', 155, 18, 'tram'),
    ...     ('Gwen Am', 34, 54, 'Venetian'),
    ...     ('Freya Dog', 34, 1, 'The Strip')
    ... ])
    {'Gwen Am': 'gwe54am4naitenev', 'Freya Dog': 'fre1dog4pirts eht'}

    # Add at least 3 doctests below here #
    >>> postcards([('John Doe', 25, 45, 'Eiffel Tower')])
    {'John Doe': 'joh45doe5rewot leffie'}
    
    >>> postcards([('Anne Marie Louise', 65, 20, 'Louvre')])
    {'Anne Marie Louise': 'ann20louise5ervuol'}

    >>> postcards([('No Akayad', 25, 21, 'Paris')])
    {'No Akayad': 'no21akayad5sirap'}
    """
    assert isinstance(info_list, list)
    assert all(isinstance(t, tuple) for t in info_list)
    assert all(len(t) == 4 for t in info_list)
    assert all(isinstance(t[0],str) and isinstance(t[1],int) and t[1] >= 0
               and isinstance(t[2],int) and t[2] >= 0 and isinstance(t[3],str)
               for t in info_list)
    
    third_letter = 3
    limit_price = 75
    age_index = 2
    
    return dict(map(lambda t :(t[0],
                               t[0].strip().split()[0][:third_letter].lower() +
                    str(t[age_index]) +
                    t[0].strip().split()[-1].lower() + str(t[1])[-1] +
                    t[-1][::-1].lower()) if len(t[0].strip().split()[0]) >=
                    third_letter
                    else (t[0], t[0].strip().split()[0].lower()
                          + str(t[age_index]) +
                    t[0].strip().split()[-1].lower() + str(t[1])[-1] +
                    t[-1][::-1].lower()), filter(lambda t :
                                                t[1] <limit_price, info_list)))


# Question 5
def win_or_lose(lst, operations):
    """
    ##############################################################
    #First I verify that the lst and operations are lists and aren't empty.
    Then that they have the right type of elements
    Then that operations doesn't have any other command
    And that the second element of each tuple from operations has
    the right type.
    
    For the key advance I return a list where I map over the int of the
    parameter 'lst' and I add the parameter 'amount' to every int
    
    For 'lost' I do the same but I remove 'amount'
    
    For 'tie' I return a filtered list where I only keep the number of 'lst'
    that are greater or equal to 'threshold'.
    
    For 'eliminate' I return a mapped list where for each int of lst, if it is
    positive then I return the message + 'won', else, the message + 'lost'.
    
    for 'win', I return the message + the sum of lst as a string.
    
    
    And thus, I create an intermediaire list named 'list_inter' that is first
    equal to 'lst'.
    
    Then I do a for loop over the tuples of lst and for each tuple, I apply the
    corresponding function to 'list_inter'
    
    And finally, I return list_inter.#
    ##############################################################

    >>> lst = [1, 12, 123, 1234, 12345, 123456]
    >>> operations_1 = [('advance', 5), ('lost', 3), ('tie', 4)]
    >>> win_or_lose(lst, operations_1)
    [14, 125, 1236, 12347, 123458]
    >>> operations_2 = [('lost', 200), ('eliminate', 'Team ')]
    >>> win_or_lose(lst, operations_2)
    ['Team lost', 'Team lost', 'Team lost', 'Team won', 'Team won', 'Team won']

    # Add at least 3 doctests below here #
    >>> lst = [-5, 0, 15, 100]
    >>> operations_4 = [('lost', 5), ('eliminate', 'Game ')]
    >>> win_or_lose(lst, operations_4)
    ['Game lost', 'Game lost', 'Game won', 'Game won']
    
    >>> lst = [5, 10, 15, 20]
    >>> operations_5 = [('advance', 5), ('lost', 2), ('win', 'Final Score: ')]
    >>> win_or_lose(lst, operations_5)
    'Final Score: 62'
    
    >>> lst = [50, 100, 150]
    >>> operations_6 = [('advance', 20), ('lost', 30), ('tie', 100), \
('win', 'Total: ')]
    >>> win_or_lose(lst, operations_6)
    'Total: 140'
    """
    # TODO: Fill out the lambda functions as dictionary values
    # Break lines if go past 79 characters
    assert(isinstance(lst, list))
    assert(isinstance(operations, list))
    assert(lst != [])
    assert(operations != [])
    assert all(isinstance(n, int) for n in lst)
    assert all(isinstance(t, tuple) and len(t) == 2 for t in operations)
    assert all(t[0] == 'advance' or t[0] == 'lost' or t[0] == 'tie' or
               t[0] == 'eliminate' or t[0] == 'win' for t in operations)
    assert all(isinstance(t[1], int) for t in operations if t[0] == 'advance')
    assert all(isinstance(t[1], int) for t in operations if t[0] == 'lost')
    assert all(isinstance(t[1], int) for t in operations if t[0] == 'tie')
    assert all(isinstance(t[1],str) for t in operations if t[0] == 'eliminate')
    assert all(isinstance(t[1], str) for t in operations if t[0] == 'win')
    
    commands = {
            'advance': lambda lst, amount: list(map(lambda n : n+ amount, lst))
            ,'lost': lambda lst, amount: list(map(lambda n : n - amount, lst)),
            'tie': lambda lst, threshold:
                list(filter(lambda n : n>=threshold, lst)),
            'eliminate':  lambda lst, symbol:
                list(map(lambda n : symbol+'won' if n>=0 else symbol+'lost',
                     lst)),
            'win': lambda lst, message: message + str(sum(lst)),
    }
    
    list_inter = lst
    
    for t in operations :
        list_inter = commands[t[0]](list_inter, t[1])
    
    return list_inter

