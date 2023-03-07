EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from
        'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time

    return remaining_bake_time


def preparation_time_in_minutes(layers):
    """
    Return elapsed cooking time.
    This function takes two numbers representing the number of layers & the
    time already spent baking and calculates the total elapsed minutes spent
    cooking the lasagna.
    """
    prep_time = layers * PREPARATION_TIME

    return prep_time


def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """
    Return elapsed cooking time.
    This function takes two numbers representing the number of layers & the
    time already spent baking and calculates the total elapsed minutes spent
    cooking the lasagna.
    """

    prep_time = layers * PREPARATION_TIME
    total_time = prep_time + elapsed_bake_time

    return total_time
