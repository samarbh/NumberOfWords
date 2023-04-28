import pytest
from nbOfWords import compter_mots
def test_compter_mots():
    # Test avec une chaîne vide
    assert compter_mots("") == 0
    # Test avec une chaîne contenant un mot
    assert compter_mots("Bonjour") == 1
    # Test avec une chaîne contenant plusieurs mots
    assert compter_mots("Bonjour tout le monde") == 4
    # Test avec une chaîne contenant plusieurs espaces consécutifs
    assert compter_mots("Bonjour    tout     le     monde") == 3
