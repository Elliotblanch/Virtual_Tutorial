import pytest
from program import vowels

def test_vowels():
    assert vowels.vowels("take") == 2
    assert vowels.vowels("league") == 4
    assert vowels.vowels("project") == 2
    assert vowels.vowels("etemenanki") == 5