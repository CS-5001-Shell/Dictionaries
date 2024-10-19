# Practice with Dictionaries

This lab assignment requires the following concepts:
- Dictionaries
- Recursion
- Python Style

For this assignment, you will complete three programs.

**All auto-graded tests require you to pass a style check.** You will not pass
the test cases unless you address all issues reported by `pycodestyle`. The unit
test output will not provide you with comprehensive information about *why* your
style check has failed. You will need to use the pycodestyle tool to identify
any issues that need to be fixed.


## Convert To Dictionary

`convert_to_dictionary.py` requires the following function:

```python
def convert_to_dictionary(list1, list2) -> dict:
    """Converts two lists into a dictionary where the ith item of list1 is a
    key and the ith item of list2 is its value.
    Parameter:
      list1: keys
      list2: values
    Return:
      dictionary
    Raises:
      ValueError if list1 and list2 are not the same length or if there is a
      duplicate item in list1
    """
    pass
```


## Depth

`depth.py` requires the following function:

```python
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
```


## Find Duplicate Values

`find_duplicate_values.py` requires the following function:

```python
def find_duplicate_values(mapping: dict) -> list:
    """Returns list of duplicated values in the dictionary passed as a
    parameter. Items that appear as values more than twice will only appear
    once in the returned list.
    Example: {'a': 1, 'b': 2, 'c': 2, 'd': 4} expected output: [2]
    Example: {'a': '1', 'b': '1', 'c': '2', 'd': '1', 'e': '2'} expected output
    ['1', '2']
    Parameter:
      mapping (dict)
    Return:
      list of all duplicates
    """
    pass
```

## Assignment Submission

To earn credit for this assignment you must commit all of your changes to your GitHub repository prior to the deadline. It is strongly recommended that you commit your changes regularly. Do not wait until you complete all parts of the assignment to upload your (partial) solution.

Step 1 - *Stage Changes*: Select the Source Control icon in the VSCode left menu. In the Changes section, click the + to *Stage All Changes*.

Step 2 - Commit Message: In the text box that says Message enter a meaningful message that describes the change you just completed.

Step 3 - *Commit & Push*: Select the down arrow in the blue box that says Commit. Choose *Commit & Push*.

Step 4 - Verify: Visit the repository on GitHub to confirm that your changes were uploaded successfully
