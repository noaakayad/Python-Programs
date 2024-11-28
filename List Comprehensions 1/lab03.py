"""
DSC 20 Fall 2024 Lab 03
Name: Noa Wissam Omar, Akayad
PID: U10274660
"""

# Problem 1.1
def keep_a_secret(filename):
    """
    Decodes message from the given input file.

    >>> print(keep_a_secret('files/encoded_1.txt').strip())
    jack reacher
    23@4 b#l31oo%m@^ way
    FSD@si%m3~on fis#he%r
    121 rockefeller avenue
    32'1 fulleH##r "dr^i~v@e
    @@4:)5#0p1m#
    7/29 06.45
    >>> print(keep_a_secret('files/encoded_2.txt').strip())
    kurt hendricks
    simon 1p@egg
    @kremlin office
    b%i>%g@ be>n @lond#o&&n
    moscow
    @reykj@av>>ik:/
    12:50 23/11
    >>> print(keep_a_secret('files/encoded_3.txt').strip())
    <BLANKLINE>
    >>> keep_a_secret('files/encoded_4.txt').strip()
    'kurt hendricks\\nsimon 1p@egg'
    """
    
    with open(filename) as reader :
        lines = reader.readlines()
        secret = ''
        
        for i in range (len(lines)) :
            lines[i] = lines[i].strip()
            for a in lines[i] :
                if a == '!' or a == '?' or a == ';' or a == '$':
                    lines[i] = lines[i].replace(a, '')
            secret += lines[i] + '\n'
        
        return secret

# Problem 1.2
def skipped_lines(filename, skip):
    """
    Decodes message from the given input file by skipping some lines

    >>> print(skipped_lines('files/encoded_1.txt', 1).strip())
    jack reacher
    FSD@si%m3~on fis#he%r
    32'1 fulleH##r "dr^i~v@e
    7/29 06.45
    >>> print(skipped_lines('files/encoded_2.txt', 2).strip())
    kurt hendricks
    b%i>%g@ be>n @lond#o&&n
    12:50 23/11
    >>> print(skipped_lines('files/encoded_3.txt', 1).strip())
    <BLANKLINE>
    >>> skipped_lines('files/encoded_4.txt', 0).strip()
    'kurt hendricks\\nsimon 1p@egg'
    """
    
    if skip == 0 :
        with open(filename) as reader :
            lines = reader.readlines()
            secret = ''
            
            for i in range (len(lines)) :
                lines[i] = lines[i].strip()
                for a in lines[i] :
                    if a == '!' or a == '?' or a == ';' or a == '$':
                        lines[i] = lines[i].replace(a, '')
                secret += lines[i] + '\n'
            
            return secret
    
    with open(filename) as reader :
        count = 0
        lines = reader.readlines()
        secret = ''
        
        for i in range (len(lines)) :
            if count == 0 :
                lines[i] = lines[i].strip()
                for a in lines[i] :
                    if a == '!' or a == '?' or a == ';' or a == '$':
                        lines[i] = lines[i].replace(a, '')
                secret += lines[i] + '\n'
                count += 1
            elif count < skip :
                count += 1
            else :
                count = 0
        
        return secret

def loose_change(cents_lst):
    """
    >>> loose_change([200, 456])
    ['2 dollar(s) and 0 cents', '4 dollar(s) and 56 cents']
    >>> loose_change([9])
    ['0 dollar(s) and 9 cents']
    >>> loose_change([])
    []
    >>> loose_change([7, 77, 777, 7777])
    ['0 dollar(s) and 7 cents', '0 dollar(s) and 77 cents', '7 dollar(s) \
and 77 cents', '77 dollar(s) and 77 cents']
    """
    return [str(i//100)+' dollar(s) and '+str(i%100)+' cents' for i in cents_lst]

def ignore_cents(cents_lst):
    """
    >>> ignore_cents([20, 46, 24])
    0
    >>> ignore_cents([])
    0
    >>> ignore_cents([120, 746, 3224, 15])
    40
    """
    return sum([i//100 for i in cents_lst])

def ignore_cents_and_small_amount(cents_lst):
    """
    >>> ignore_cents_and_small_amount([34, 245, 6678, 16608])
    232
    >>> ignore_cents_and_small_amount([120, 746, 3224, 15])
    0
    >>> ignore_cents_and_small_amount([])
    0
    >>> ignore_cents_and_small_amount([12345, 50000, 4999])
    623
    """
    
    return sum([i//100 for i in cents_lst if i//100 >= 50])


def keep_dollars_only(money_list):
    """
    >>> keep_dollars_only([(150, "dollars"), (80, "euros"), (120, "euros")])
    [150, 'skip', 'skip']
    >>> keep_dollars_only([(133, "euros"), (72, "rubles"), (120, "renminbi")])
    ['skip', 'skip', 'skip']
    >>> keep_dollars_only([(19, "dollars"), (275, "dollars"), (100, "dollars")])
    [19, 275, 100]
    """
    
    return [t[0] if t[1] == 'dollars' else 'skip' for t in money_list]

def combine_the_strings(names_and_salaries):
    """
    >>> combine_the_strings([("Tom", "Cruise"), ("Jon", "Voight"),("Henry",)])
    ['Tom', 'Cruise', 'Jon', 'Voight', 'Henry']
    >>> combine_the_strings([()])
    []
    >>> combine_the_strings([])
    []
    >>> combine_the_strings([("Marina", "Langlois")])
    ['Marina', 'Langlois']
    """
    
    return [t[i] for t in names_and_salaries for i in range(len(t))]

def selected_name(names, char):
    """
    >>> selected_name(['Marina Langlois', 'James Bond', 'Austin Madden'], 'E')
    ['Austin']
    >>> selected_name(['Martina Sampson', 'Jill Gordon', 'Cary Barber'], 's')
    ['Martina']
    >>> selected_name(['Dana Donaldson', 'Selma Owen'], 'Z')
    []
    """
    return [(name.split())[0] for name in names if char in (name.split())[1] or\
            char.lower() in (name.split())[1].lower()]

def pay_reaction(proposed_salaries):
    """
    >>> pay_reaction([2200, 1400, 55, 1991])
    ['Will take it', 'Thinking', 'Not enough', 'Thinking']
    >>> pay_reaction([])
    []
    >>> pay_reaction([0.01, 100000])
    ['Not enough', 'Will take it']
    """
    return['Not enough' if x <= 1000 else 'Thinking' if 1000 < x <= 2000 else 'Will take it' for x in proposed_salaries]

def months_to_years(ages):
    """
    >>> ages = [[119, 154, 345], [4, 61]]
    >>> months_to_years(ages)
    [[9, 12, 28], [0, 5]]
    >>> ages = [[], []]
    >>> months_to_years(ages)
    [[], []]
    >>> ages = [[200], [615, 0]]
    >>> months_to_years(ages)
    [[16], [51, 0]]
    """
    return[[i//12 for i in lst] for lst in ages]

def harder_convert(ages):
    """
    >>> ages = [[119, 14, -34], [5, -177, -232, 362]]
    >>> harder_convert(ages)
    [[9, 1, 0], [0, 0, 0, 30]]
    >>> ages = [[], []]
    >>> harder_convert(ages)
    [[], []]
    >>> ages = [[132], [-65, 0]]
    >>> harder_convert(ages)
    [[11], [0, 0]]
    """
    return[[i//12 if i > 0 else 0 for i in lst] for lst in ages]

def older_than_30(ages):
    """
    >>> ages = [[120, -154, 245], [145, -360, -615, 306]]
    >>> older_than_30(ages)
    0
    >>> ages = [[8848], [779, 0]]
    >>> older_than_30(ages)
    2
    >>> ages = [[80, -854, 900], [45, 360, 15]]
    >>> older_than_30(ages)
    2
    """
    return len([i//12 for lst in ages for i in lst if i//12 >= 30])
