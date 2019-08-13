"""
A file for executing math functions.
"""

from typing import Union
import numpy as np


def euler(n = 10):
    """
    This function computes :math:`e` via a Taylor series.

    .. math::

        e = 1 + \\sum_n^\\infty \\frac{1}{n!}

    Parameters
    ----------
    n : int
        The order of the Taylor expansion.

    Returns
    -------
    e_value : float
        The computed value of Euler's number.
    """

    if n < 0:
        raise ValueError("Only positive integers are allowed")

    n += 1
    e_value = 0
    for i in range(n):
        e_value += 1 / factorial(i)
    return e_value


def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1


def pi(n: Union[int, float] = 1e4) -> float:
    return 4 * np.mean(np.linalg.norm(np.random.rand(int(n), 2), axis=-1) < 1)
