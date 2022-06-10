import pytest
from program import factorial

def test_fact():
    assert factorial.fact(0) == 1
    assert factorial.fact(1) == 1
    assert factorial.fact(3) == 6
    assert factorial.fact(4) == 24
    assert factorial.fact(5) == 120
    assert factorial.fact(9) == 362880