"""
# tests/test_lib.py
"""

from mlproject.lib import hello_world


def test_length_of_hello_world():
    """Test length of hello world."""
    assert len(hello_world()) != 0
