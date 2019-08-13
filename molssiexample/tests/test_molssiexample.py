"""
Unit and regression test for the molssiexample package.
"""

# Import package, test suite, and other packages as needed
import molssiexample
import pytest
import sys

def test_molssiexample_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molssiexample" in sys.modules
