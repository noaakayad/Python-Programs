"""
DSC 20 Fall 2023 Homework 07
Name: Noa Wissam Omar Akayad
PID: U10274660
Source: Lectures, thinkpython
"""

# Question 1
def type_with_number(message):
    """
    ##############################################################
    # If 'message' is empty then I return an empty string.
    Otherwise, I create 'nums' which is the result of the function on
    'message' without it first letter, and regarding the letter, I add to
    the reccursive result the corresponding number.#
    ##############################################################

    >>> type_with_number('Welcome to Beijing!')
    '9352663086023454641'
    >>> type_with_number('I miss my laptop.')
    '40647706905278671'
    >>> type_with_number('!!??..  ,,')
    '1111110011'

    # Add at least 3 doctests below here #
    >>> type_with_number('Noa')
    '662'
    >>> type_with_number('Cameron')
    '2263766'
    >>> type_with_number('sami')
    '7264'
    """
    if message == '' :
        return ''
    nums = type_with_number(message[1:])
    first_letter = message[0]
    if first_letter in ',.?!' :
        return '1' + nums
    elif first_letter in 'abc' or first_letter in 'ABC' :
        return '2' + nums
    elif first_letter in 'def' or first_letter in 'DEF' :
        return '3' + nums
    elif first_letter in 'ghi' or first_letter in 'GHI' :
        return '4' + nums
    elif first_letter in 'jkl' or first_letter in 'JKL' :
        return '5' + nums
    elif first_letter in 'mno' or first_letter in 'MNO' :
        return '6' + nums
    elif first_letter in 'pqrs' or first_letter in 'PQRS' :
        return '7' + nums
    elif first_letter in 'tuv' or first_letter in 'TUV' :
        return '8' + nums
    elif first_letter in 'wxyz' or first_letter in 'WXYZ' :
        return '9' + nums
    else :
        return '0' + nums

# Question 2
def make_palindrome(start, stop):
    """
    ##############################################################
    # Here I create a helper function that works recursively to return
    a string of numbers starting from 'start' to 'stop'.
    
    Thus, if start == stop, i return start.
    If start < stop, I return the result of my helper function for start and
    stop-1 + stop + the reversed result of my helper function.
    else, I do the same but with stop+1.#
    ##############################################################

    >>> make_palindrome(1, 1)
    '1'
    >>> make_palindrome(3, 5)
    '34543'
    >>> make_palindrome(5, 2)
    '5432345'

    # Add at least 3 doctests below here #
    >>> make_palindrome(1, 0)
    '101'
    >>> make_palindrome(0, 1)
    '010'
    >>> make_palindrome(0, 0)
    '0'
    """
    if start == stop :
        return str(start)
    elif start < stop :
        return str(start) + make_palindrome(start+1, stop) + str(start)
    else :
        return str(start) + make_palindrome(start-1, stop) + str(start)


# Question 3
def doctests_q3():
    """
    >>> my_phone = Phone('Apple', 4000, 64000)
    >>> my_phone.brand
    'Apple'
    >>> my_phone.charge
    2000
    >>> my_phone.num_apps
    0
    >>> my_phone.use(10)
    >>> my_phone.charge
    1900
    >>> my_phone.recharge(10)
    >>> my_phone.charge
    2100
    >>> my_phone.install(1000, 'Spotify')
    'App installed'
    >>> my_phone.apps
    {'Spotify'}
    >>> my_phone.storage
    63000
    >>> my_phone.use(210)
    'Out of charge'
    >>> my_phone.recharge(400)
    >>> my_phone.charge
    4000
    >>> my_phone.install(1000, 'Spotify')
    'App already installed'

    # Add your own doctests below
    
    >>> iphone = Phone('Apple', 5000, 70000)
    >>> iphone.brand
    'Apple'
    >>> iphone.max_charge
    5000
    >>> iphone.storage
    70000
    >>> iphone.use(5000000)
    'Out of charge'
    >>> iphone.recharge(500000000)
    >>> iphone.charge
    5000
    >>> iphone.install(70001, 'Google')
    'Not enough storage'
    
    
    >>> samsung = Phone('Samsung', 5000, 70000)
    >>> samsung.brand
    'Samsung'
    >>> samsung.max_charge
    5000
    >>> samsung.storage
    70000
    >>> samsung.use(5000000)
    'Out of charge'
    >>> samsung.recharge(500000000)
    >>> samsung.charge
    5000
    >>> samsung.install(700, 'Google')
    'App installed'
    
    >>> random = Phone('random', 1000, 7000)
    >>> random.brand
    'random'
    >>> random.max_charge
    1000
    >>> random.storage
    7000
    >>> random.use(5000000)
    'Out of charge'
    >>> random.recharge(500000000)
    >>> random.charge
    1000
    >>> random.install(700, 'Google')
    'App installed'
    >>> random.install(700, 'Google')
    'App already installed'
    
    >>> redmi = Phone('Redmi', 5000, 70000)
    >>> redmi.brand
    'Redmi'
    >>> redmi.max_charge
    5000
    >>> redmi.storage
    70000
    >>> redmi.use(5000000)
    'Out of charge'
    >>> redmi.recharge(500000000)
    >>> redmi.charge
    5000
    >>> redmi.install(700, 'Google')
    'App installed'
    """
    return

class Phone:
    """
    Implementation of Phone
    """
    def __init__(self, brand, max_charge, storage) :
        """
        This constructor take as input brand, max_charge and storage to put
        them as instances attributes and use them values to put 5 other
        attributes to a Phone object.
        """
        self.brand = brand
        self.max_charge = max_charge
        self.storage = storage
        half = 2
        self.charge = max_charge//half
        
        if brand == 'Apple' :
            self.drain_rate = 10
        elif brand == 'OnePlus' :
            self.drain_rate = 12
        elif brand == 'Samsung' :
            self.drain_rate = 8
        else :
            self.drain_rate = 15
        
        self.charge_rate = 20
        
        self.num_apps = 0
        
        self.apps = set([])
    
    def use(self, minutes) :
        """
        Drain_rate represents how much charge the phone uses per
        minute thus, minutes * drain_rate represents the amount of charge
        that has been used, if this amount is greater than the current charge,
        then we just put the charge at 0 as everything has been used, else,
        we put charge - this amount as the current charge.
        """
        used = minutes * self.drain_rate
        
        if used >= self.charge :
            self.charge = 0
            return 'Out of charge'
        else :
            self.charge = self.charge - used

    def recharge(self, minutes) :
        """
        Charge_rate represents how much charge the phone can take per
        minute thus, minutes * charge_rate represents the amount of charge
        that has been charged, if this amount is greater than the max charge,
        then we just put the charge at its max as everything has been used,
        else, we put charge + this amount as the current charge.
        """
        add = minutes * self.charge_rate
        
        if add + self.charge >= self.max_charge :
            self.charge = self.max_charge
        else :
            self.charge = add + self.charge
    
    def install(self, app_size, app_name) :
        """
        if the phone has no charge then we can't install the app,
        if the phone has no space left, we can't install the app,
        if the app is already installed, we can't install it,
        else, we add it to the set apps and we reduce the storage by the
        size of the app and we increment the number of apps.
        """
        if self.charge == 0 :
            return 'Out of charge'
        elif self.storage < app_size :
            return 'Not enough storage'
        elif app_name in self.apps :
            return 'App already installed'
        else :
            self.apps.add(app_name)
            self.storage -= app_size
            self.num_apps += 1
            return 'App installed'
        
        
################ CLASS PART ##################

# Question 4

def doctests_go_here():
    """
    >>> track1 = Song('More Life', 3.11, 'Just Until...', 'Cordae', 1220980)
    >>> print(track1)
    'More Life' by Cordae on 'Just Until...' is 3.11 minutes long with \
1220980 streams
    >>> track1.get_artist()
    'Cordae'
    >>> Song.platform
    'Spotify'
    >>> track1.platform
    'Spotify'
    >>> play1 = Playlist('Rap Caviar', 'James')
    >>> print(play1)
    Playlist 'Rap Caviar' by James has 0 songs
    >>> play1.add_song(track1)
    True
    >>> play1.get_total_streams()
    1220980
    >>> print(play1)
    Playlist 'Rap Caviar' by James has 1 songs
    >>> play1.add_song(track1)
    False
    >>> play1.remove_song(track1)
    True
    
    >>> track2 = Song('Good Days', 4.65, 'Good Days', 'SZA', 276568815)
    >>> track3 = Song('Heat Waves', 3.999, 'Dreamland', 'Glass Animals', 5000)
    >>> play1.add_song(track2)
    True
    >>> play1.add_song(track1)
    True
    >>> play1.add_song(track3)
    True
    >>> track2.add_to_playlist(play1)
    False
    >>> play1.sort_songs('length')
    >>> [x.get_name() for x in play1.get_songs()]
    ['More Life', 'Heat Waves', 'Good Days']
    >>> play1.sort_songs('name')
    >>> [x.get_name() for x in play1.get_songs()]
    ['Good Days', 'Heat Waves', 'More Life']
    >>> play1.sort_songs('streams')
    >>> [x.get_name() for x in play1.get_songs()]
    ['Heat Waves', 'More Life', 'Good Days']
    >>> play1.get_most_played_song()
    'Good Days'
    >>> play1.get_total_streams()
    277794795
    >>> play1.get_total_length()
    11.759
    >>> print(play1.play())
    Listening to 'Heat Waves' by Glass Animals
    Listening to 'More Life' by Cordae
    Listening to 'Good Days' by SZA
    >>> print(track1.listen())
    Listening to 'More Life' by Cordae
    >>> play1.get_total_streams()
    277794799
    >>> play2 = Playlist('Anti Pop', 'Spotify')
    >>> play1.combine_playlists(play2)
    True
    >>> play2.combine_playlists(play1)
    True
    >>> print(play2)
    Playlist 'Anti Pop' by Spotify has 3 songs
    >>> play2.combine_playlists(play1)
    3
    >>> play2.remove_song(track2)
    True
    >>> play2.get_most_played_song()
    'More Life'
    >>> track2.add_to_playlist(play2)
    True
    >>> play2.get_most_played_song()
    'Good Days'
    >>> play3 = Playlist('test', 'ab')
    >>> play3.get_most_played_song()
    ''
    >>> play3.get_total_streams()
    0
    >>> play3.get_total_length()
    0
    >>> play3.sort_songs('length')
    >>> play3.songs
    []
    >>> play2.combine_playlists(play3)
    True

    >>> TS = Song('Shake it Off', 1.23, '1989', 'Taylor Swift', 12345)
    >>> BC = Song('Halo', 2.34, 'I Am... Sasha Fierce', 'Beyoncé', 23456)
    >>> JB = Song('Baby', 3.45, 'Okay', 'Justin Bieber', 34567)
    >>> LG = Song('Bad Romance', 4.53, 'Talk You Back', 'Lady Gaga', 45678)
    >>> AG = Song('Side to Side', 1.01, 'Dangerous Woman', 'Ariana Grande', \
56432)
    >>> SG = Song('BiggieBig', 3.22, 'The Album', 'Selena Gomez', 987)
    >>> WG = Song('God is Fair', 32.43, 'GOD IS AROUND US', 'Windaco God', \
    99999999)
    >>> BM = Song('Talking to the Moon', 3.38, 'Doo-Wops & Hooligans', \
    'Bruno Mars', 2814901)
    >>> NB = Song('Long Song', 99999.99, 'Billy Boy', 'Nobody Billy', 7654321)
    >>> Playlist1 = Playlist('God Spoken!', 'Yes sir')
    >>> Playlist2 = Playlist('Do you still love me if I am DJ', 'Xiaozi')
    >>> Playlist3 = Playlist('Best Song', 'Ye')
    >>> lst = [TS,BC,JB,LG,AG,SG,WG,BM,NB]
    
    >>> song1 = Song('fein', 2.5, 'utopia', 'travis', 500)
    >>> print(song1)
    'fein' by travis on 'utopia' is 2.5 minutes long with 500 streams
    >>> song1.listen()
    "Listening to 'fein' by travis"
    
    >>> noa = Playlist('noa', 'noa')
    >>> print(noa)
    Playlist 'noa' by noa has 0 songs
    >>> noa.add_song(song1)
    True
    >>> song1.add_to_playlist(noa)
    False
    >>> noa.remove_song(song1)
    True
    >>> noa.sort_songs('name')
    >>> print(noa.songs)
    []
    >>> noa.add_song(song1)
    True
    >>> noa.get_total_streams()
    501
    >>> noa.get_total_length()
    2.5
    >>> print(noa.play())
    Listening to 'fein' by travis
    >>> noa.combine_playlists(noa)
    1
    >>> noa.get_most_played_song()
    'fein'
    
    
    >>> song2 = Song('sprinter', 2, 'cee', 'cench', 5000)
    >>> print(song2)
    'sprinter' by cench on 'cee' is 2 minutes long with 5000 streams
    >>> song2.listen()
    "Listening to 'sprinter' by cench"
    
    >>> noa2 = Playlist('noa2', 'noa')
    >>> print(noa2)
    Playlist 'noa2' by noa has 0 songs
    >>> noa2.add_song(song2)
    True
    >>> song2.add_to_playlist(noa2)
    False
    >>> noa2.remove_song(song2)
    True
    >>> noa2.sort_songs('name')
    >>> print(noa2.songs)
    []
    >>> noa2.add_song(song2)
    True
    >>> noa2.get_total_streams()
    5001
    >>> noa2.get_total_length()
    2
    >>> print(noa2.play())
    Listening to 'sprinter' by cench
    >>> noa2.combine_playlists(noa2)
    1
    >>> noa2.get_most_played_song()
    'sprinter'
    
    
    
    >>> song3 = Song('hot', 3, 'ysl', 'young', 400)
    >>> print(song3)
    'hot' by young on 'ysl' is 3 minutes long with 400 streams
    >>> song3.listen()
    "Listening to 'hot' by young"
    
    >>> noa3 = Playlist('noa3', 'noa')
    >>> print(noa3)
    Playlist 'noa3' by noa has 0 songs
    >>> noa3.add_song(song3)
    True
    >>> song3.add_to_playlist(noa3)
    False
    >>> noa3.remove_song(song3)
    True
    >>> noa3.sort_songs('name')
    >>> print(noa3.songs)
    []
    >>> noa3.add_song(song3)
    True
    >>> noa3.add_song(song1)
    True
    >>> noa3.add_song(song2)
    True
    >>> noa3.get_total_streams()
    5905
    >>> noa3.get_total_length()
    7.5
    >>> print(noa3.play())
    Listening to 'hot' by young
    Listening to 'fein' by travis
    Listening to 'sprinter' by cench
    >>> noa3.combine_playlists(noa)
    1
    >>> noa3.get_most_played_song()
    'sprinter'
    
    """
    return


class Song:
    """
    Implementation of a song
    """

    platform = 'Spotify'
    
    def __init__(self, name, length, album, artist, streams):
        """
        Constructor of Song
        Parameters:
        name (str): name of the song
        length (float): song duration in minutes
        album (str): name of album the song is in
        artist (str): name of artist
        streams (int): number of times the song has been streamed
        """
        self.name = name
        self.length = length
        self.album = album
        self.artist = artist
        self.streams = streams


    def get_name(self):
        """ Getter for name attribute """
        return self.name


    def get_length(self):
        """ Getter for length attribute """
        return self.length


    def get_album(self):
        """ Getter for album attribute """
        return self.album


    def get_artist(self):
        """ Getter for artist attribute """
        return self.artist


    def get_streams(self):
        """ Getter for streams attribute """
        return self.streams


    def __str__(self):
        """
        String representation of Song
        """
        return "'"+self.name+"' by "+self.artist+" on '"+self.album+"' is "+ \
str(self.length)+' minutes long with '+str(self.streams)+' streams'


    def listen(self):
        """
        Listens to the song, increasing the stream counter.
        Returns a string with the song name and artist
        """
        self.streams += 1
        return "Listening to '"+self.name+"' by "+self.artist


    def add_to_playlist(self, playlist):
        """
        Takes a Playlist object and adds the current Song instance into it.
        return True if successful
        return False if song is already included in playlist
        """
        return playlist.add_song(self)

# Question 5

class Playlist:
    """
    Implementation of a playlist
    """

    def __init__(self, title, user):
        """
        Constructor of Playlist
        Parameters:
        title (str): title of the playlist
        user (str): username of user who created playlist
        Attributes:
        songs (list): list used to store songs in playlist
        """
        self.title = title
        self.user = user
        self.songs = []


    def get_title(self):
        """ Getter for title attribute """
        return self.title 


    def get_user(self):
        """ Getter for user attribute """
        return self.user 
    

    def get_songs(self):
        """ Getter for songs attribute """
        return self.songs 


    def __str__(self):
        """
        String representation of Playlist
        """
        return "Playlist '"+self.title+"' by "+self.user+' has '+ \
str(len(self.songs))+' songs' 


    def add_song(self, song):
        """
        Adds song to list
        return True if successful
        return False if song is already included in playlist
        """
        assert isinstance(song, Song)
        assert isinstance(song, Song)
        assert isinstance(song.name, str)
        assert isinstance(song.length, (float,int)) and song.length >= 0
        assert isinstance(song.album, str)
        assert isinstance(song.artist, str)
        assert isinstance(song.streams, int) and song.streams >= 0
        if song not in self.songs :
            self.songs.append(song)
            return True
        else :
            return False

    def remove_song(self, song):
        """
        Removes a song from the list
        return True if successful
        return False if song is not in the playlist
        """
        assert isinstance(song, Song)
        assert isinstance(song.name, str)
        assert isinstance(song.length, (float,int)) and song.length >= 0
        assert isinstance(song.album, str)
        assert isinstance(song.artist, str)
        assert isinstance(song.streams, int) and song.streams >= 0
        if song in self.songs :
            self.songs.remove(song)
            return True
        else :
            return False


    def sort_songs(self, sort_by):
        """
        Sorts the songs by the sort_by attribute in ascending order
        """
        assert sort_by in "name, length, album, artist, streams"
        self.songs = sorted(self.songs, key = lambda song :
                            getattr(song, sort_by))
        


    def get_total_streams(self):
        """
        Returns the total amount of streams of the songs in the playlist
        """
        return sum([song.streams for song in self.songs])


    def get_total_length(self):
        """
        Returns the total length of the playlist
        """
        return sum([song.length for song in self.songs])


    def play(self):
        """
        Plays every song in the playlist.
        Returns a string that records all the songs played.
        If the playlist is empty, return "Empty"
        """
        if self.songs == [] :
            return 'Empty'
        else :
            result = ''
            for song in self.songs :
                result += song.listen() + '\n'
            
            return result[:-1]
    

    def combine_playlists(self, other_playlist):
        """
        Add all songs from other_playlist to current playlist.
        If all songs were added successfully, return True. 
        If not, return the number of songs that weren't added.
        """
        assert isinstance(other_playlist, Playlist)
        assert all(isinstance(song, Song) for song in other_playlist.songs)
        assert all(isinstance(song.name, str) for song in other_playlist.songs)
        assert all(isinstance(song.length, (float,int)) and song.length >= 0
                   for song in other_playlist.songs)
        assert all(isinstance(song.album, str)
                   for song in other_playlist.songs)
        assert all(isinstance(song.artist, str)
                   for song in other_playlist.songs)
        assert all(isinstance(song.streams, int) and song.streams >= 0
                   for song in other_playlist.songs)
        
        unique_songs = [1 if song not in self.songs
                        else 0 for song in other_playlist.songs]
        if sum(unique_songs) == len(other_playlist.songs) :
            self.songs += other_playlist.songs
            return True
        else :
            self.songs += [song for song in other_playlist.songs
                           if song not in self.songs]
            return len(other_playlist.songs) - sum(unique_songs)
    

    def get_most_played_song(self):
        """
        Return the name of the most played song
        """
        if self.songs == [] :
            return ''
        else :
            max_song = self.songs[0]
            for song in self.songs :
                if song.get_streams() > max_song.get_streams() :
                    max_song = song
            
            return max_song.get_name()
