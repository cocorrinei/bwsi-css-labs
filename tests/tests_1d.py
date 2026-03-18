"""
tests_1b.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_two_sum():
    assert two_sum([0, 0, 0, 0], 11) == []
    assert two_sum([1, 1, 2, 5], 3) == [0, 2]
    assert two_sum([], 2) == []

if __name__ == "__main__":
    pytest.main()