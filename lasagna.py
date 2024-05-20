# lasagna.py

# Constant for the expected bake time in minutes
EXPECTED_BAKE_TIME = 40
"""int: Constant representing the expected bake time in minutes for the lasagna."""

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - the number of minutes the lasagna has been baking.
    :return: int - the number of minutes remaining until the lasagna is fully baked.

    This function takes an integer representing the number of minutes the lasagna has
    been baking and returns how many minutes are left until the lasagna is properly baked.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(layers):
    """Calculate the preparation time.

    :param layers: int - the number of layers added to the lasagna.
    :return: int - the total preparation time in minutes.

    This function takes an integer representing the number of layers you want to add
    to the lasagna and returns the total preparation time in minutes.
    """
    PREPARATION_TIME_PER_LAYER = 2
    return layers * PREPARATION_TIME_PER_LAYER

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


