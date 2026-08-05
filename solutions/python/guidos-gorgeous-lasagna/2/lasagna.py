"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    

def preparation_time_in_minutes(number_of_layers):
    """Time taken to make the layers.

    Parameters:
        number_of_layers (int): The numbers of layers required to make the lasagna.

    Returns:
        int: The time (in minutes) required to make the layers.

    Function that takes the number of layers required to make each lasagna and returns
    total time (in minutes) required to make the layers based on the `PREPARATION_TIME`.
    """
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Time taken in the kitchen.

    Parameters:
        number_of_layers (int): The numbers of layers required to make the lasagna.
        elapsed_bake_time (int): The baking time already elapsed.
    Returns:
        int: The time (in minutes) required to make the layers.

    Function that takes the number of layers required to make each lasagna and 
    the number of minutes the lasagna has spent baking in the oven already
    returns total time (in minutes) spent in the kitchen.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time