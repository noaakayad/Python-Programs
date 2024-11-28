"""
DSC 20 Fall 2024 Homework 08
Name: Noa Wissam Omar Akayad
PID: U10274660
Source: N/A
"""

def q1_doctests():
    """
    Doctests for Question 1.
    
    >>> broom_1 = FlyingBroom()
    >>> broom_2 = NormalBroom()
    >>> broom_3 = CursedBroom()
    >>> broom_2.boost(20)
    True
    >>> broom_1.duel(broom_2)
    False
    >>> broom_2.high_score()
    9100
    >>> broom_2.duel(broom_3)
    False
    >>> broom_2.speed
    30
    >>> broom_3.high_score()
    25750
    >>> broom_4 = CursedBroom()
    >>> broom_3.duel(broom_4)
    True
    >>> broom_4.size
    7
    >>> broom_4.speed
    20
    >>> broom_3.size
    8
    >>> broom_4.boost(40)
    True
    >>> broom_4.lives
    6
    >>> broom_4.duel(broom_2)
    True
    >>> broom_4.high_score()
    24650
    >>> broom_4.size
    8
    >>> broom_2.speed
    50
    
    
    # ADD DOCTESTS HERE #
    >>> broom1 = FlyingBroom()
    >>> broom2 = NormalBroom()
    >>> broom3 = CursedBroom()
    
    >>> broom1.speed, broom1.size, broom1.magic_power, broom1.lives
    (50, 5, 3, 3)
    >>> broom2.speed, broom2.size, broom2.magic_power, broom2.lives
    (50, 5, 3, 3)
    >>> broom3.speed, broom3.size, broom3.magic_power, broom3.lives
    (70, 7, 5, 5)
    
    >>> broom1.high_score()
    6500
    >>> broom2.high_score()
    6500
    >>> broom3.high_score()
    15750
    
    >>> broom1.boost(20)
    True
    >>> broom1.speed
    76
    >>> broom1.magic_power
    2
    >>> broom3.boost(40)
    True
    >>> broom3.speed
    114
    >>> broom3.magic_power
    4
    >>> broom1.boost(20)
    True
    >>> broom1.lives
    3
    >>> broom1.magic_power
    1
    
    >>> broom1.boost(20)
    True
    >>> broom1.magic_power
    0
    >>> broom1.boost(20)
    False
    
    >>> broom4 = FlyingBroom()
    >>> broom1.duel(broom4)
    False
    
    >>> broom4.set_size(4)
    >>> broom1.duel(broom4)
    True
    >>> broom1.speed
    209
    >>> broom4.speed
    0
    >>> broom4.lives
    3
    >>> broom4.speed
    0
    
    >>> broom2.duel(broom3)
    False
    >>> broom2.speed
    30
    >>> broom3.size
    8
    >>> broom3.speed
    164
    
    >>> broom2.high_score()
    4000
    >>> broom3.high_score()
    34550
    
    >>> broom5 = NormalBroom()
    >>> broom5.set_size(6)
    >>> broom5.duel(broom4)
    True
    >>> broom5.speed
    100
    >>> broom4.speed
    50
    >>> broom4.lives
    2
    >>> broom5.size
    7
    
    >>> broom6 = CursedBroom()
    >>> broom6.high_score()
    15750
    >>> broom6.duel(broom5)
    False
    >>> broom6.high_score()
    15750
    >>> broom5.speed
    100
    >>> broom6.speed
    70

    """
    return

class FlyingBroom:
    """
    Implementation of FlyingBroom.
    """
    def __init__(self):
        self.speed = 50
        self.size = 5
        self.magic_power = 3
        self.lives = 3
        """
        Constructor of FlyingBroom.
        
        Initializes the specified attributes on creation:
        - speed (non-negative int): current speed of broom, default is 50
        - size (positive int): physical size of broom, default is 5
        - magic_power (non-negative int): number of magic boosts remaining
          for this broom, default is 3
        - lives (non-negative int): number of lives a wizard has while
          flying this broom, default is 3
        """
        pass

    def boost(self, charm_power):
        """
        Boosts the speed of the broom by using a magical
        charm. Speed boost is calculated using the formula
        specified in the write-up. If boost is successfully
        applied (enough magic power to perform boost), return True.
        Otherwise (no remaining magic power to perform boost), return False.
        
        Parameters:
        - charm_power (int): used to calcualte speed boost formula.
          Applied as long the broom still has some magic power
          remaining.
        """
        if self.magic_power > 0 :
            squarred = 2
            speed_100 = 100
            lives_500 = 500
            previous_score = self.high_score()
            new_speed = int(((self.speed + charm_power)**squarred + \
                             (self.speed - charm_power)**squarred)**0.5)
            self.speed = new_speed
            if self.high_score() >= previous_score * squarred :
                self.lives += 1
            self.magic_power -= 1
            return True
        else :
            return False

    def set_speed(self, new_speed):
        """
        Setter method that assigns given speed value to 
        speed attribute.
        
        Parameters:
        - new_speed (int): new speed value
        """
        self.speed = new_speed

    def set_lives(self, gains = True):
        """
        Setter method that increments lives attribute 
        by 1 if gains is True, otherwise decrement by 1.
        
        Parameters:
        - gains (bool): decides whether to increment/decrement
          lives attribute by 1.
        """
        if gains :
            self.lives += 1
        else :
            self.lives -= 1

    def set_size(self, new_size):
        """
        Setter method that assigns given size value
        (non-negative) to size attribute.
        
        Parameters:
        - new_size (non-negative int): new size value
        """
        self.size = new_size

    def duel(self, other_broom):
        """
        Determines if a duel can occur between
        current broom and other_broom. If so,
        the following happens as specified in
        the write-up. Return True if current
        broom successfully performs duel, otherwise
        False.
        
        Parameters:
        - other_broom (object): Broom object
        """
        if self.size > other_broom.size :
            self.speed += 50
            other_broom.speed -= 50
            if other_broom.speed < 0 :
                other_broom.lives -= 1
                other_broom.speed = 50
                self.size += 1
            return True
        elif self.size < other_broom.size :
            self.speed -= 50
            other_broom.speed += 50
            if self.speed < 0 :
                self.lives -= 1
                self.speed = 50
                other_broom.size += 1
            return True
        else :
            return False

    def high_score(self):
        """
        Formula for high score and returns it.
        """
        speed_100 = 100
        lives_500 = 500
        return int(self.speed * speed_100 + self.lives * lives_500)

class NormalBroom(FlyingBroom):
    """
    Implementation of NormalBroom. Subclass of FlyingBroom.
    """
    def duel(self, other_broom):
        """
        Duel method for NormalBroom.
        - If other_broom is an instance of CursedBroom,
          current NormalBroom loses one life, and its speed 
          resets to 30.
        - CursedBroom object gains a size, and its speed
          increases by 50.
        - Attack is thus considered unsuccessful, function
          returns False.
        - If other_broom is not a CursedBroom object, duel
          method is the same as in the parent class.
        
        Parameters:
        - other_broom (object): Broom object
        """
        if isinstance(other_broom, CursedBroom) :
            self.lives -= 1
            self.speed = 30
            other_broom.size += 1
            other_broom.speed += 50
            return False
        else :
            return super().duel(other_broom)

class CursedBroom(FlyingBroom):
    """
    Implementation of CursedBroom. Subclass of FlyingBroom.
    """
    def __init__(self):
        """
        Constructor of CursedBroom.
        
        Initializes the specified attributes on creation:
        - speed (non-negative int): default is 70
        - size (positive int): default is 7
        - magic_power (non-negative int): default is 5
        - lives (non-negative int): default is 5
        """
        super().__init__()
        self.speed = 70
        self.size = 7
        self.magic_power = 5
        self.lives = 5

    def high_score(self):
        """
        Formula for a CursedBroom high score and returns it.
        """
        return int(self.speed * 200 + self.lives * 300 + 250)


# Question 2
# Q2, Part 1
def fix_1(lst1, lst2):
    """
    ##############################################################
    # Here for every 'num' I do a try and except block to see if the
    division is possible, if so, then we add it to out, else, we just 'pass'
    to the next 'num'.#
    ##############################################################

    >>> fix_1([1, 2, 3], [0, 1])
    [1.0, 2.0, 3.0]
    >>> fix_1([], [])
    []
    >>> fix_1([10, 20, 30], [0, 10, 10, 0])
    [1.0, 2.0, 3.0, 1.0, 2.0, 3.0]
    
    # NO DOCTESTS NEEDED #
    """
    out = []
    for div in lst2:
        for num in lst1:
            try :
                out.append(num / div)
            except :
                pass
    return out

# Q2, Part 2
def fix_2(*filepaths):
    """
    ##############################################################
    # Here for every file, I try to open them, if there is no problem with that
    then I pront that the file has been opened and I close it, else, I
    print the that the file was not found.#
    ##############################################################

    >>> fix_2('files/a.txt', 'files/b.txt', 'files/c.txt')
    files/a.txt opened
    files/b.txt not found
    files/c.txt not found
    >>> fix_2('docs.txt')
    docs.txt not found
    
    # NO DOCTESTS NEEDED #
    """
    for filepath in filepaths:
        try :
            cur_file = open(filepath, "r")
            print(filepath + ' opened')
            cur_file.close()
        except :
            print(filepath +' not found')

# Q2, Part 3
def fix_3(lst):
    """
    ##############################################################
    # Here for every index and its value of 'lst', I try the algorithm,
    if an error occurs and it is of type TypeError then I print what is asked
    and if the error is an IndexError then I do the same logic.#
    ##############################################################

    >>> fix_3([1, '1', 2, None])
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'IndexError'>
    []
    >>> fix_3([1, 2, 3, 4])
    <class 'IndexError'>
    [3, 5, 7]
    >>> fix_3([])
    []
    
    # NO DOCTESTS NEEDED #
    """
    sum_of_pairs = []
    for i, _ in enumerate(lst):
        try :
            sum_of_pairs.append(lst[i] + lst[i + 1])
        except TypeError :
            print("<class 'TypeError'>")
        except IndexError :
            print("<class 'IndexError'>")
    return sum_of_pairs


# Question 3
def check_inputs(input1, input2):
    """
    ##############################################################
    # Here for the 'input1', I check if it is a list and contains only
    numeric values, if an error occurs then I raise the corresponding TypeError
    message. For 'input2', I check if it is an int and if an error occurs then
    I raise the appropriate TypeError messageand then if I check if it is in
    'input1', if an error occurs then I raise the appropriate
    TypeError message. #
    ##############################################################

    >>> check_inputs([1, 2.0, 3.0, 4], 4)
    'Input validated'
    >>> check_inputs([], 1)
    Traceback (most recent call last):
    ...
    TypeError: input2 not in input1
    >>> check_inputs(1, 1)
    Traceback (most recent call last):
    ...
    TypeError: input1 is not the correct type
    >>> check_inputs([1, 2, 'hi'], 4)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 2 is not numeric
    >>> check_inputs([1.0, 2.0, 3.0], 'hello')
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type
    
    # Add at least 3 doctests below here #
    >> check_inputs([0, -1.2, 3.5], -1.2)
    'Input validated'
    >>> check_inputs(['a', 2, 3], 2)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 0 is not numeric
    >>> check_inputs([10, 20, 30], 40)
    Traceback (most recent call last):
    ...
    TypeError: input2 not in input1
    """
    if not isinstance(input1, list) :
        raise TypeError("input1 is not the correct type")
    for i in range(len(input1)) :
        if not isinstance(input1[i], (int, float)) :
            raise TypeError("The element at index "+str(i)+" is not numeric")
    if not isinstance(input2, int) :
        raise TypeError("input2 is not the correct type")
    if input2 not in input1 :
        raise TypeError("input2 not in input1")
    return 'Input validated'

# Question 4
def load_file(filepath):
    """
    ##############################################################
    # Here I first check if 'filepath' is a str, if not, I raise the
    corresponding TypeError message.
    
    Then I try to open filepath, if I can't then I raison the FileNotFound
    error message,
    if I can open it, then I put in the list 'lines' every line of my file,
    if lines is [] then I raise the corresponding ValueError.
    Else, everything is okay so I calcul the number of words thanks to a
    list comprehension having the length of every line stripped and splitted
    with ' ' and I return the sum of this list.#
    ##############################################################

    >>> load_file(1)
    Traceback (most recent call last):
    ...
    TypeError: filepath is not a string
    >>> load_file('files/ten_words.txt')
    10
    >>> load_file('files/empty.txt')
    Traceback (most recent call last):
    ...
    ValueError: File is empty
    >>> load_file('files/nonexistant.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/nonexistant.txt does not exist
    
    # Add at least 3 doctests below here #
    >>> load_file([])
    Traceback (most recent call last):
    ...
    TypeError: filepath is not a string
    
    >>> load_file('files/doesnt_exist.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/doesnt_exist.txt does not exist
    
    >>> load_file('files/5_words.txt')
    5
    """
    if not isinstance(filepath, str) :
        raise TypeError("filepath is not a string")
    try :
        reader = open(filepath,'r')
        lines = reader.readlines()
        if lines == [] :
            raise ValueError("File is empty")
        return sum([len(word.strip().split()) for word in lines])
    except FileNotFoundError :
        raise FileNotFoundError(filepath + ' does not exist')
