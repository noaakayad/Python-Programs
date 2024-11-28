"""
DSC 20 Project
Name(s): Noa Wissam Omar Akayad
PID(s):  U10274660
Sources: N/A
"""

import numpy as np
import os
from PIL import Image
from pydub import AudioSegment

NUM_CHANNELS = 3


# --------------------------------------------------------------------------- #

def img_read_helper(path):
    """
    Creates an RGBImage object from the given image file
    """
    # Open the image in RGB
    img = Image.open(path).convert("RGB")
    # Convert to numpy array and then to a list
    matrix = np.array(img).tolist()
    # Use student's code to create an RGBImage object
    return RGBImage(matrix)


def img_save_helper(path, image):
    """
    Saves the given RGBImage instance to the given path
    """
    # Convert list to numpy array
    img_array = np.array(image.get_pixels())
    # Convert numpy array to PIL Image object
    img = Image.fromarray(img_array.astype(np.uint8))
    # Save the image object to path
    img.save(path)


# --------------------------------------------------------------------------- #

# Part 1: RGB Image #
class RGBImage:
    """
    Represents an image in RGB format
    """

    def __init__(self, pixels):
        """
        Initializes a new RGBImage object

        # Test with non-rectangular list
        >>> pixels = [
        ...              [[255, 255, 255], [255, 255, 255]],
        ...              [[255, 255, 255]]
        ...          ]
        >>> RGBImage(pixels)
        Traceback (most recent call last):
        ...
        TypeError

        # Test instance variables
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img.pixels
        [[[255, 255, 255], [0, 0, 0]]]
        >>> img.num_rows
        1
        >>> img.num_cols
        2
        """
        # YOUR CODE GOES HERE #
        # Raise exceptions here
        if not isinstance(pixels, list) and pixels == []:
            raise TypeError()
        
        for row in pixels :
            if not isinstance(row, list) and row == []:
                raise TypeError()
        num_cols = len(pixels[0])
        for row in pixels :
            if len(row) != num_cols :
                raise TypeError()
            for col in row :
                if not isinstance(col, list) and len(col) != 3:
                    raise TypeError()
                for c in col :
                    if not isinstance(c, int) and (c < 0 or c > 255):
                        raise TypeError()
        
        self.pixels = pixels
        self.num_rows = len(pixels)
        self.num_cols = num_cols

    def size(self):
        """
        Returns the size of the image in (rows, cols) format

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img.size()
        (1, 2)
        """
        # YOUR CODE GOES HERE #
        return (self.num_rows, self.num_cols)

    def get_pixels(self):
        """
        Returns a copy of the image pixel array

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img_pixels = img.get_pixels()

        # Check if this is a deep copy
        >>> img_pixels                               # Check the values
        [[[255, 255, 255], [0, 0, 0]]]
        >>> id(pixels) != id(img_pixels)             # Check outer list
        True
        >>> id(pixels[0]) != id(img_pixels[0])       # Check row
        True
        >>> id(pixels[0][0]) != id(img_pixels[0][0]) # Check pixel
        True
        """
        return [[[i for i in col] for col in row] for row in self.pixels]

    def copy(self):
        """
        Returns a copy of this RGBImage object

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img_copy = img.copy()

        # Check that this is a new instance
        >>> id(img_copy) != id(img)
        True
        """
        new_pixels = self.get_pixels()
        copy_instance = RGBImage(new_pixels)
        return copy_instance

    def get_pixel(self, row, col):
        """
        Returns the (R, G, B) value at the given position

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)

        # Test with an invalid index
        >>> img.get_pixel(1, 0)
        Traceback (most recent call last):
        ...
        ValueError

        # Run and check the returned value
        >>> img.get_pixel(0, 0)
        (255, 255, 255)
        """
        if not isinstance(row, int) :
            raise TypeError()
        if not isinstance(col, int) :
            raise TypeError()
        if 0 > row or row >= self.num_rows :
            raise ValueError()
        if 0 > col or col >= self.num_cols :
            raise ValueError()
        return tuple(self.pixels[row][col])

    def set_pixel(self, row, col, new_color):
        """
        Sets the (R, G, B) value at the given position

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)

        # Test with an invalid new_color tuple
        >>> img.set_pixel(0, 0, (256, 0, 0))
        Traceback (most recent call last):
        ...
        ValueError

        # Check that the R/G/B value with negative is unchanged
        >>> img.set_pixel(0, 0, (-1, 0, 0))
        >>> img.pixels
        [[[255, 0, 0], [0, 0, 0]]]
        """
        if not isinstance(row, int) :
            raise TypeError()
        if not isinstance(col, int) :
            raise TypeError()
        if 0 > row or row >= self.num_rows :
            raise ValueError()
        if 0 > col or col >= self.num_cols :
            raise ValueError()
        if not isinstance(new_color, tuple) or len(new_color) != 3:
            raise TypeError()
        c1,c2,c3 = new_color 
        if not isinstance(c1, int) or c1 > 255 :
            raise ValueError()
        if c1 >= 0 :
            self.pixels[row][col][0] = c1
        if not isinstance(c2, int) or c2 > 255 :
            raise ValueError()
        if c2 >= 0 :
            self.pixels[row][col][1] = c2
        if not isinstance(c3, int) or c3 > 255 :
            raise ValueError()
        if c3 >= 0 :
            self.pixels[row][col][2] = c3
            

# Part 2: Image Processing Template Methods #
class ImageProcessingTemplate:
    """
    Contains assorted image processing methods
    Intended to be used as a parent class
    """

    def __init__(self):
        """
        Creates a new ImageProcessingTemplate object

        # Check that the cost was assigned
        >>> img_proc = ImageProcessingTemplate()
        >>> img_proc.cost
        0
        """
        # YOUR CODE GOES HERE #
        self.cost = 0

    def get_cost(self):
        """
        Returns the current total incurred cost

        # Check that the cost value is returned
        >>> img_proc = ImageProcessingTemplate()
        >>> img_proc.cost = 50 # Manually modify cost
        >>> img_proc.get_cost()
        50
        """
        return self.cost

    def negate(self, image):
        """
        Returns a negated copy of the given image

        # Check if this is returning a new RGBImage instance
        >>> img_proc = ImageProcessingTemplate()
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img_negate = img_proc.negate(img)
        >>> id(img) != id(img_negate) # Check for new RGBImage instance
        True

        # The following is a description of how this test works
        # 1 Create a processor
        # 2/3 Read in the input and expected output
        # 4 Modify the input
        # 5 Compare the modified and expected
        # 6 Write the output to file
        # You can view the output in the img/out/ directory
        >>> img_proc = ImageProcessingTemplate()                            # 1
        >>> img = img_read_helper('img/test_image_32x32.png')                 # 2
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_negate.png')  # 3
        >>> img_negate = img_proc.negate(img)                               # 4
        >>> img_negate.pixels == img_exp.pixels # Check negate output       # 5
        True
        >>> img_save_helper('img/out/test_image_32x32_negate.png', img_negate)# 6
        """
        # YOUR CODE GOES HERE #
        new_image = image.copy()
        
        new_pixels = [[[255 - val for val in col] for col in row] for row in \
                      new_image.pixels]
        new_image.pixels = new_pixels
        return new_image

    def grayscale(self, image):
        """
        Returns a grayscale copy of the given image

        # See negate for info on this test
        # You can view the output in the img/out/ directory
        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_gray.png')
        >>> img_gray = img_proc.grayscale(img)
        >>> img_gray.pixels == img_exp.pixels # Check grayscale output
        True
        >>> img_save_helper('img/out/test_image_32x32_gray.png', img_gray)
        """
        new_image = image.copy()
        
        new_pixels = [[[sum(col)//3 for val in col] for col in row] for row in\
                      new_image.pixels]
        new_image.pixels = new_pixels
        return new_image

    def rotate_180(self, image):
        """
        Returns a rotated version of the given image

        # See negate for info on this test
        # You can view the output in the img/out/ directory
        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_rotate.png')
        >>> img_rotate = img_proc.rotate_180(img)
        >>> img_rotate.pixels == img_exp.pixels # Check rotate_180 output
        True
        >>> img_save_helper('img/out/test_image_32x32_rotate.png', img_rotate)
        """
        # YOUR CODE GOES HERE #
        new_image = image.copy()
        
        n = new_image.num_rows
        m = new_image.num_cols
        
        new_pixels = [[new_image.pixels[n-1-i][m-1-j] for j in range(m)]
                      for i in range(n)]
        new_image.pixels = new_pixels
        return new_image

    def get_average_brightness(self, image):
        """
        Returns the average brightness for the given image

        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_proc.get_average_brightness(img)
        86
        """
        # YOUR CODE GOES HERE #
        pixels_avg = [sum(image.pixels[i][j])//3 for i in range(image.num_rows) 
                      for j in range(image.num_cols)]
        return sum(pixels_avg)//(image.num_rows*image.num_cols)

    def adjust_brightness(self, image, intensity):
        """
        Returns a new image with adjusted brightness level

        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_adjusted.png')
        >>> img_adjust = img_proc.adjust_brightness(img, 1.2)
        >>> img_adjust.pixels == img_exp.pixels # Check adjust_brightness
        True
        >>> img_save_helper('img/out/test_image_32x32_adjusted.png', img_adjust)
        """
        # YOUR CODE GOES HERE #
        if not isinstance(intensity, float) :
            raise TypeError()
        if intensity > 255 or intensity < -255 :
            raise ValueError()
        new_image = image.copy()
        
        new_pixels = [[[int(val*intensity) if int(val*intensity) <= 255 else
                        255 if int(val*intensity) >= 0 else 0 for val in col]
                       for col in row] for row in new_image.pixels]
        
        new_image.pixels = new_pixels
        return new_image


# Part 3: Standard Image Processing Methods #
class StandardImageProcessing(ImageProcessingTemplate):
    """
    Represents a standard tier of an image processor
    """

    def __init__(self):
        """
        Creates a new StandardImageProcessing object

        # Check that the cost was assigned
        >>> img_proc = StandardImageProcessing()
        >>> img_proc.cost
        0
        """
        # YOUR CODE GOES HERE #
        self.cost = 0
        self.coupon = 0

    def negate(self, image):
        """
        Returns a negated copy of the given image

        # Check the expected cost
        >>> img_proc = StandardImageProcessing()
        >>> img_in = img_read_helper('img/square_32x32.png')
        >>> negated = img_proc.negate(img_in)
        >>> img_proc.get_cost()
        5

        # Check that negate works the same as in the parent class
        >>> img_proc = StandardImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_negate.png')
        >>> img_negate = img_proc.negate(img)
        >>> img_negate.pixels == img_exp.pixels # Check negate output
        True
        """
        # YOUR CODE GOES HERE #
        if self.coupon > 0 :
            self.coupon -= 1
        else :
            self.cost += 5
        return super().negate(image)

    def grayscale(self, image):
        """
        Returns a grayscale copy of the given image

        """
        # YOUR CODE GOES HERE #
        if self.coupon > 0 :
            self.coupon -= 1
        else :
            self.cost += 6
        return super().grayscale(image)

    def rotate_180(self, image):
        """
        Returns a rotated version of the given image
        """
        # YOUR CODE GOES HERE #
        if self.coupon > 0 :
            self.coupon -= 1
        else :
            self.cost += 10
        return super().rotate_180(image)

    def adjust_brightness(self, image, intensity):
        """
        Returns a new image with adjusted brightness level
        """
        # YOUR CODE GOES HERE #
        if self.coupon > 0 :
            self.coupon -= 1
        else :
            self.cost += 1
        return super().adjust_brightness(image)

    def redeem_coupon(self, amount):
        """
        Makes the given number of methods calls free

        # Check that the cost does not change for a call to negate
        # when a coupon is redeemed
        >>> img_proc = StandardImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_proc.redeem_coupon(1)
        >>> img = img_proc.rotate_180(img)
        >>> img_proc.get_cost()
        0
        """
        # YOUR CODE GOES HERE #
        if not isinstance(amount, int) :
            raise TypeError()
        if amount <= 0 :
            raise ValueError()
        self.coupon += amount


# Part 4: Premium Image Processing Methods #
class PremiumImageProcessing(ImageProcessingTemplate):
    """
    Represents a paid tier of an image processor
    """

    def __init__(self):
        """
        Creates a new PremiumImageProcessing object

        # Check the expected cost
        >>> img_proc = PremiumImageProcessing()
        >>> img_proc.get_cost()
        50
        """
        # YOUR CODE GOES HERE #
        self.cost = 50

    def pixelate(self, image, block_dim):
        """
        Returns a pixelated version of the image, where block_dim is the size of 
        the square blocks.

        # Check output
        >>> img_proc = PremiumImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_pixelate = img_proc.pixelate(img, 4)
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_pixelate.png')
        >>> img_exp.pixels == img_pixelate.pixels # Check pixelate output
        True
        >>> img_save_helper('img/out/test_image_32x32_pixelate.png', img_pixelate)
        """
        # YOUR CODE GOES HERE #
        new_image = image.copy()
        
        n = new_image.num_rows
        m = new_image.num_cols
        
        visited = [[False for pixel in row] for row in new_image.pixels]
        
        num_blocks = n*m // block_dim
        
        for block in range(num_blocks) :
            block_ = []
            count_row = 1
            
            for i in range(n) :               
                if count_row <= block_dim :
                    count_col = 1
                    for j in range(m) :
                        if not visited[i][j] and count_col <= block_dim :
                            visited[i][j] = True
                            block_.append((i,j))
                            count_col += 1
                    if count_col > 1 :
                        count_row += 1
            
            
            if count_row > 1 and count_col > 1 :
                r_avg = sum([new_image.pixels[i][j][0] for i,j in block_])//((count_row-1)*(count_col-1))
                g_avg = sum([new_image.pixels[i][j][1] for i,j in block_])//((count_row-1)*(count_col-1))
                b_avg = sum([new_image.pixels[i][j][2] for i,j in block_])//((count_row-1)*(count_col-1))
                for (i,j) in block_ :
                    new_image.pixels[i][j][0] = r_avg
                    new_image.pixels[i][j][1] = g_avg
                    new_image.pixels[i][j][2] = b_avg
        
        return new_image
        

    def edge_highlight(self, image):
        """
        Returns a new image with the edges highlighted

        # Check output
        >>> img_proc = PremiumImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_edge = img_proc.edge_highlight(img)
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_edge.png')
        >>> img_exp.pixels == img_edge.pixels # Check edge_highlight output
        True
        >>> img_save_helper('img/out/test_image_32x32_edge.png', img_edge)
        """
        # YOUR CODE GOES HERE #
        
        new_image = image.copy()
        
        single_values = [[sum(row[i])//3 for i in range(len(row))] for row in new_image.pixels]
        
        n = new_image.num_rows
        m = new_image.num_cols
        
        for i in range(n) :
            for j in range(n) :
                if i != 0 and i != n-1 and j != 0 and j != m-1 :
                    masked_value = -single_values[i-1][j-1] -single_values[i-1][j] -single_values[i-1][j+1] -single_values[i][j+1] -single_values[i+1][j+1] -single_values[i+1][j] -single_values[i+1][j-1] - single_values[i][j-1] + 8*single_values[i][j]
                    
                    if masked_value > 255 :
                        masked_value = 255
                    if masked_value < 0 :
                        masked_value = 0
                    
                    new_image.pixels[i][j] = [masked_value, masked_value, masked_value]
                    
                elif j == m-1 and i != 0 and i != n-1 :
                    masked_value = -single_values[i-1][j-1] -single_values[i-1][j] -single_values[i+1][j] -single_values[i+1][j-1] - single_values[i][j-1] + 8*single_values[i][j]
                    
                    if masked_value > 255 :
                        masked_value = 255
                    if masked_value < 0 :
                        masked_value = 0
                    
                    new_image.pixels[i][j] = [masked_value, masked_value, masked_value]
                    
                elif j == 0 and i != 0 and i != n-1 :
                    masked_value = -single_values[i-1][j] -single_values[i-1][j+1] -single_values[i][j+1] -single_values[i+1][j+1] -single_values[i+1][j] + 8*single_values[i][j]
                    
                    
                    if masked_value > 255 :
                        masked_value = 255
                    if masked_value < 0 :
                        masked_value = 0
                    
                    new_image.pixels[i][j] = [masked_value, masked_value, masked_value]
                elif i == n-1 and j != 0 and j != n-1 :
                    masked_value = -single_values[i-1][j-1] -single_values[i-1][j] -single_values[i-1][j+1] -single_values[i][j+1] - single_values[i][j-1] + 8*single_values[i][j]
                    
                    if masked_value > 255 :
                        masked_value = 255
                    if masked_value < 0 :
                        masked_value = 0
                    
                    new_image.pixels[i][j] = [masked_value, masked_value, masked_value]
                elif i == 0 and j != 0 and j != n-1 :
                    masked_value = -single_values[i][j+1] -single_values[i+1][j+1] -single_values[i+1][j] -single_values[i+1][j-1] - single_values[i][j-1] + 8*single_values[i][j]
                    
                    if masked_value > 255 :
                        masked_value = 255
                    if masked_value < 0 :
                        masked_value = 0
                    
                    new_image.pixels[i][j] = [masked_value, masked_value, masked_value]
                elif i == 0 and j == 0 :
                    masked_value = -single_values[i][j+1] -single_values[i+1][j+1] -single_values[i+1][j] + 8*single_values[i][j]
                    
                    if masked_value > 255 :
                        masked_value = 255
                    if masked_value < 0 :
                        masked_value = 0
                    
                    new_image.pixels[i][j] = [masked_value, masked_value, masked_value]
                elif i == 0 and j == m-1 :
                    masked_value = -single_values[i][j-1] -single_values[i+1][j-1] -single_values[i+1][j] + 8*single_values[i][j]
                    
                    if masked_value > 255 :
                        masked_value = 255
                    if masked_value < 0 :
                        masked_value = 0
                    
                    new_image.pixels[i][j] = [masked_value, masked_value, masked_value]
                elif i == n-1 and j == 0 :
                    masked_value = -single_values[i-1][j] -single_values[i-1][j+1] -single_values[i][j+1] + 8*single_values[i][j]
                    
                    if masked_value > 255 :
                        masked_value = 255
                    if masked_value < 0 :
                        masked_value = 0
                    
                    new_image.pixels[i][j] = [masked_value, masked_value, masked_value]
                else :
                    masked_value = -single_values[i-1][j] -single_values[i-1][j-1] -single_values[i][j-1] + 8*single_values[i][j]
                    
                    if masked_value > 255 :
                        masked_value = 255
                    if masked_value < 0 :
                        masked_value = 0
                    
                    new_image.pixels[i][j] = [masked_value, masked_value, masked_value]

        
        return new_image
# --------------------------------------------------------------------------- #

def audio_read_helper(path):
    """
    Creates an AudioWave object from the given audio file
    """
    # Load the audio file
    audio = AudioSegment.from_file(file = path,  
                                  format = path.split('.')[-1])    
    # Convert to mono if it's stereo
    audio = audio.set_channels(1)
    # Get the raw audio data
    raw_data = np.array(audio.get_array_of_samples()).tolist()
    return AudioWave(raw_data)


def audio_save_helper(path, audio, sample_rate = 44100):
    """
    Saves the given AudioWave instance to the given path
    """
    # Convert list to numpy array
    audio_array = np.array(audio.wave).astype(np.int16)
    # Convert the NumPy array back to an AudioSegment
    audio_segment = AudioSegment(
        audio_array.tobytes(), 
        frame_rate=sample_rate,
        sample_width=audio_array.dtype.itemsize,
        channels=1
    )
    
    # Export the audio segment to a wav file
    audio_segment.export(path, format="wav")


# --------------------------------------------------------------------------- #
# Part 5: Multimedia Processing
class AudioWave():
    """
        Represents audio through a 1-dimensional array of amplitudes
    """
    def __init__(self, amplitudes):
        self.wave = amplitudes

## TODO: PremiumPlusMultimediaProcessing Class Implementation
class PremiumPlusMultimediaProcessing(PremiumImageProcessing) :
    
    def __init__(self):
        self.cost = 75
        
    def reverse_song(self, audio) :
        if not isinstance(audio, AudioWave):
            raise TypeError()
        
        return AudioWave([audio.wave[i] for i in range(len(audio.wave)-1, -1, -1)])
    
    def slow_down(self, audio, factor) :
        if not isinstance(audio, AudioWave):
            raise TypeError()
        if not isinstance(factor, int) or factor < 0:
            raise TypeError()
        
        return AudioWave([audio.wave[i] for i in range(len(audio.wave)) for j in range(factor)])
    
    def speed_up(self, audio, factor) :
        if not isinstance(audio, AudioWave):
            raise TypeError()
        if not isinstance(factor, int) or factor < 0:
            raise TypeError()
        
        return AudioWave([audio.wave[i] for i in range(len(audio.wave)) if i%factor == 0])
    
    def reverb(self, audio) :
        if not isinstance(audio, AudioWave):
            raise TypeError()
        
        return AudioWave([round(audio.wave[i] + audio.wave[i-1] * 0.8 + audio.wave[i-2] * 0.6 + audio.wave[i-3] * 0.4 + audio.wave[i-4] * 0.2) if i>=4 else audio.wave[i] for i in range(len(audio.wave))])

    def clip_song(self, audio, start, end) :
        if not isinstance(audio, AudioWave):
            raise TypeError()
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError()
        if end < 0 or end > 100 or start < 0 or start > 100:
            raise ValueError()
        
        start_index =  round((start/100)*len(audio.wave))
        end_index =  round((end/100)*len(audio.wave))
        
        return AudioWave(audio.wave[start_index:end_index])
        

# Part 6: Image KNN Classifier #
class ImageKNNClassifier:
    """
    Represents a simple KNNClassifier
    """

    def __init__(self, k_neighbors):
        """
        Creates a new KNN classifier object
        """
        # YOUR CODE GOES HERE #
        self.k_neighbors = k_neighbors

    def fit(self, data):
        """
        Stores the given set of data and labels for later
        """
        # YOUR CODE GOES HERE #
        if len(data) < self.k_neighbors :
            raise ValueError()
        self.data = data

    def distance(self, image1, image2):
        """
        Returns the distance between the given images

        >>> img1 = img_read_helper('img/steve.png')
        >>> img2 = img_read_helper('img/knn_test_img.png')
        >>> knn = ImageKNNClassifier(3)
        >>> knn.distance(img1, img2)
        15946.312896716909
        """
        # YOUR CODE GOES HERE #
        if not isinstance(image1, RGBImage) or not isinstance(image2, RGBImage) :
            raise TypeError()
        if image1.num_rows*image1.num_cols != image2.num_rows*image2.num_cols :
            raise ValueError()
        return (sum([(image1.pixels[row][col][i] - image2.pixels[row][col][i])**2 for row in range(image1.num_rows) for col in range(image1.num_cols) for i in range(3)]))**0.5

    def vote(self, candidates):
        """
        Returns the most frequent label in the given list

        >>> knn = ImageKNNClassifier(3)
        >>> knn.vote(['label1', 'label2', 'label2', 'label2', 'label1'])
        'label2'
        """
        # YOUR CODE GOES HERE #
        d = {}
        for candidate in candidates :
            if candidate in d.keys() :
                d[candidate] += 1
            else :
                d[candidate] = 0
        
        candidate_max = candidates[0]
        for candidate, freq in d.items() :
            if freq > d[candidate_max] :
                candidate_max = candidate
                
        return candidate_max

    def predict(self, image):
        """
        Predicts the label of the given image using the labels of
        the K closest neighbors to this image

        The test for this method is located in the knn_tests method below
        """
        # YOUR CODE GOES HERE #
        if not self.data :
            raise ValueError
        
        dist = [(self.data[i], self.distance(image, self.data[i][0])) for i in range(len(self.data))]
        
        dist = sorted(dist, key = lambda t : t[1])
        labels = [dist[i][0][1] for i in range(len(dist))]
        
        return self.vote(labels)

def knn_tests(test_img_path):
    """
    Function to run knn tests

    >>> knn_tests('img/knn_test_img.png')
    'nighttime'
    
    """
    # Read all of the sub-folder names in the knn_data folder
    # These will be treated as labels
    path = 'knn_data'
    data = []
    for label in os.listdir(path):
        label_path = os.path.join(path, label)
        # Ignore non-folder items
        if not os.path.isdir(label_path):
            continue
        # Read in each image in the sub-folder
        for img_file in os.listdir(label_path):
            train_img_path = os.path.join(label_path, img_file)
            img = img_read_helper(train_img_path)
            # Add the image object and the label to the dataset
            data.append((img, label))

    # Create a KNN-classifier using the dataset
    knn = ImageKNNClassifier(5)

    # Train the classifier by providing the dataset
    knn.fit(data)
    
    #Create an RGBImage object of the tested image
    test_img = img_read_helper(test_img_path)

    # Return the KNN's prediction
    predicted_label = knn.predict(test_img)
    return predicted_label

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
