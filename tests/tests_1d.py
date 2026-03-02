"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_max_subarray_sum():
    assert two_sum([2,7,11,15], 9) == [0,1]              # Test for example case
    assert two_sum([3,2,4], 6) == [1,2]                   # Test for example case
    assert two_sum([3,3], 6) == [0,1]                     # Test for duplicate numbers
    assert two_sum([2,5,5,11], 10) == [1,2]              # Test for duplicate numbers

if __name__ == "__main__":
    pytest.main()