def depth(value: dict) -> int:
    """Returns the depth of the dictionary specified by the parameter value.

    The function must be recursive.


    For this exercise, you are only required to consider dictionaries that
    appear as values inside of other dictionaries. You do not need to consider
    dictionaries inside of other structures, e.g., a dictionary that appears
    inside of a list.

    Below are three examples of depth 1, depth 2, and depth 4, respectively.

    depth_1 = {
        "key1": 34,
        "key2": "fish"
    }

    depth_2 = {
        "key1": {
            "key3": 34,
            "key4": 56
        },
        "key2": "fish"
    }

    depth_4 = {
        "key1": {
            "key2": "value1",
            "key3": [1, 2, 3]
        },
        "key4": {
            "key5": {
                "key6": {
                    "key8": "fish"
                }
            },
            "key7": 34
        }
    }

    Parameter:
      value (dict): a dictionary
    Return:
      int representing the maximum depth of the dictionary
    """
    pass
