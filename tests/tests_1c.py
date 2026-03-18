"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_sum():
    assert max_subarray_sum([0, 0, -1, 0, 0]) == 0 # edge case
    assert max_subarray_sum([0, 1, 2, -5, 2, -1, 2]) == 3 # normal case
    assert max_subarray_sum([]) == 0 # empty list (edge case)

if __name__ == "__main__":
    pytest.main()