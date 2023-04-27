import pytest 
import nbOfWords
import unittest
from unittest.mock import patch, MagicMock

def compter_mots(chaine):
    # Gérer l'entrée de chaîne vide
    if not chaine:
        return 0

    # Supprimer les espaces de début et de fin
    input_str = chaine.strip()

    nb_mots = 1

    for char in input_str:
        if char == ' ':
            nb_mots += 1

    return nb_mots


class TestCompterMots(unittest.TestCase):
    
    def test_compter_mots_patch(self):
        with patch('__main__.len') as mock_len:
            mock_len.return_value = 5
            chaine = "test"
            self.assertEqual(compter_mots(chaine), 1)
            mock_len.assert_called_once_with(['test'])
            
    def test_compter_mots_return_value(self):
        with patch('__main__.len') as mock_len:
            mock_len.return_value = 3
            chaine = "Bonjour tout le monde"
            self.assertEqual(compter_mots(chaine), 3)
            mock_len.assert_called_once_with(['Bonjour', 'tout', 'le'])
            
    def test_compter_mots_side_effect(self):
        mock_strip = MagicMock
        mock_strip.return_value = "test"
        with patch('__main__.str.strip', new=mock_strip):
            chaine = "    test    "
            self.assertEqual(compter_mots(chaine), 1)
            mock_strip.assert_called_once_with('    test    ')
