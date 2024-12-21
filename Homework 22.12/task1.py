from typing import List

def convert_to_string_list(numbers: List[int]) -> List[str]:
    """
    Converts a list of integers to a list of their string representations.

    :param numbers: List of integers.
    :return: List of strings representing the integers.
    """
    return [str(number) for number in numbers]
