import pytest
import numpy as np

import molssiexample as me


@pytest.mark.parametrize('n, answer', [(0, 1), (1, 2), (2, 2.5), (3, 2.6666667)])
def test_euler(n, answer):

    assert me.math.euler(n) == pytest.approx(answer, abs=1.e-6)

def test_euler_failures():

    with pytest.raises(ValueError) as exc:
        me.math.euler(-1)

    assert "positive int" in str(exc.value)


def test_pi():
    np.random.seed(0)

    assert me.math.pi(1e6) == pytest.approx(3.140936, abs=1.e-6)
