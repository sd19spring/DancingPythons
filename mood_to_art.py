"""
Generating Computational Art
Course: Software Design
@author: Anthony Krichevskiy
"""

import random
import music_to_mood
from PIL import Image


def build_random_function(min_depth, max_depth):
    """Build a random function.

    Builds a random function of depth at least min_depth and depth at most
    max_depth. (See the assignment write-up for the definition of depth
    in this context)

    Args:
        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function

    Returns:
        The randomly generated function represented as a nested list.
        (See the assignment writ-eup for details on the representation of
        these functions)

    """
    #Establish empty list to build off of.
    function = []
    #There were lots of problems with min_depth decreasing too far. 1 should be the minimum.
    if min_depth < 1:
        min_depth = 1
    #Determine depth of the function. Only really used to determine if base case is triggered.
    from random import randint
    depth = randint(min_depth, max_depth)
    #Base case that ends recursion. All functions with depth = 1 must be either "x" or "y"
    if depth == 1:
        generator = randint(1, 2)
        if generator == 1:
            function.append("x")
        if generator == 2:
            function.append("y")
        return function
    else:
    #A random integer generator determines which of the 6 functions will be used.
        generator = randint(1, 6)
    #The "prod" and "avg" functions have 2 inputs and therefore 2 more lists have to be appended.
        if generator == 1:
            function.append("prod")
            #Max_depth and min_depth have to decrease by 1 for each recursion.
            function.append(build_random_function(min_depth - 1, max_depth - 1))
            function.append(build_random_function(min_depth - 1, max_depth - 1))
            return function
        if generator == 2:
            function.append("avg")
            function.append(build_random_function(min_depth - 1, max_depth - 1))
            function.append(build_random_function(min_depth - 1, max_depth - 1))
            return function
        if generator == 3:
            function.append("sin_pi")
            function.append(build_random_function(min_depth - 1, max_depth - 1))
            return function
        if generator == 4:
            function.append("cos_pi")
            function.append(build_random_function(min_depth - 1, max_depth - 1))
            return function
        if generator == 5:
            function.append("square")
            function.append(build_random_function(min_depth - 1, max_depth - 1))
            return function
        if generator == 6:
            function.append("root_abs")
            function.append(build_random_function(min_depth - 1, max_depth - 1))
            return function


def evaluate_random_function(f, x, y):
    """Evaluate the random function f with inputs x,y.

    The representation of the function f is defined in the assignment write-up.

    Args:
        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function

    Returns:
        The function value

    Examples:
        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["y"],0.1,0.02)
        0.02
        >>> evaluate_random_function(["sin_pi", ["cos_pi", ["x"]]], -0.5, 0)
        0
        >>> evaluate_random_function(["prod", ["prod", ["y"], ["sin_pi", ["x"]]], ["sin_pi", ["y"]]], 0.5, -0.5)
        0.5
        >>> evaluate_random_function(["avg", ["prod", ["x"], ["y"]], ["sin_pi", ["x"]]], 0.5, 0.82)
        0.705
        >>> evaluate_random_function(["square", ["avg", ["sin_pi", ["y"]], ["cos_pi", ["x"]]]], 0, (1/6))
        0.5625
        >>> evaluate_random_function(["root_abs", ["x"]], -0.09, 1)
        0.3
    """
    #The first term of the function list determines which function is called, therefore, conditionals are used.
    import math
    if f[0] == "prod":
        return evaluate_random_function(f[1], x, y) * evaluate_random_function(f[2], x, y)
    if f[0] == "avg":
        return 0.5 * (evaluate_random_function(f[1], x, y) + evaluate_random_function(f[2], x, y))
    if f[0] == "cos_pi":
    #Cos_pi and sin_pi were having problems returning numbers in scientific notation that were very very close to 0.
    #Therefore, I implemented this conditional which returns 0 when cos_pi or sin_pi are within 0.01 of 0.
        if math.cos(math.pi * evaluate_random_function(f[1], x, y)) < 0.01 and math.cos(math.pi * evaluate_random_function(f[1], x, y)) > -0.01:
            return 0
        else:
            return math.cos(math.pi * evaluate_random_function(f[1], x, y))
    if f[0] == "sin_pi":
        if math.sin(math.pi * evaluate_random_function(f[1], x, y)) < 0.01 and math.sin(math.pi * evaluate_random_function(f[1], x, y)) > -0.01:
            return 0
        else:
            return math.sin(math.pi * evaluate_random_function(f[1], x, y))
    if f[0] == "square":
        return evaluate_random_function(f[1], x, y)**2
    if f[0] == "root_abs":
    #You cannot take the square root of the negative, so I had to take the square root of the absolute value.
        return abs(evaluate_random_function(f[1], x, y))**0.5
    if f[0] == "x":
        return x
    if f[0] == "y":
        return y


def remap_interval(val,
                   input_interval_start,
                   input_interval_end,
                   output_interval_start,
                   output_interval_end):
    """Remap a value from one interval to another.

    Given an input value in the interval [input_interval_start,
    input_interval_end], return an output value scaled to fall within
    the output interval [output_interval_start, output_interval_end].

    Args:
        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values

    Returns:
        The value remapped from the input to the output interval

    Examples:
        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
    # TODO: implement this
    valfraction = (val - input_interval_start) / (input_interval_end - input_interval_start)
    outputfraction = valfraction * (output_interval_end - output_interval_start)
    remap = outputfraction + output_interval_start
    return remap


def color_map(val, min_rgb=0, max_rgb=255):
    """Maps input value between -1 and 1 to an integer 0-255, suitable for use as an RGB color code.

    Args:
        val: value to remap, must be a float in the interval [-1, 1]

    Returns:
        An integer in the interval [0,255]

    Examples:
        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, min_rgb, max_rgb)
    return int(color_code)


<<<<<<< HEAD
def generate_art(filename, x_size=640, y_size=480, red_min=0, red_max=255, green_min=0, green_max=255, blue_min=0, blue_max=255):
=======
def test_image(filename, x_size=350, y_size=350):
    """Generate a test image with random pixels and save as an image file.

    Args:
        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel

    im.save(filename)


def generate_art(filename, x_size=640, y_size=480):
>>>>>>> a2f58cd95510483f1467e4fc62b01d29464585a0
    """Generate computational art and save as an image file.

    Args:
        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    red_function = build_random_function(7, 9)
    green_function = build_random_function(7, 9)
    blue_function = build_random_function(5, 7)

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                color_map(evaluate_random_function(red_function, x, y), min_rgb=red_min, max_rgb=red_max),
                color_map(evaluate_random_function(green_function, x, y), min_rgb=green_min, max_rgb=green_max),
                color_map(evaluate_random_function(blue_function, x, y), min_rgb=blue_min, max_rgb=blue_max)
            )
    im.save(filename)


if __name__ == '__main__':
    if music_to_mood.mood_output() == 'happy':
        generate_art('test.png', x_size=300, y_size=300, red_min=255, red_max=255, green_min=100, green_max=255, blue_min=0, blue_max=150)
    else:
        print('Sad song')
