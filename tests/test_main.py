"""Test for ALL main.py functions"""
from src import main
import pytest

def test_calculate_hash_value():
    """Test function to test ALL main.py functions"""
    hash_table = main.HashTable()

    hash_table.store('LALA')
    hash_table.store('LALA')
    hash_table.store('LALAFA')

    assert hash_table.calculate_hash_value(
        'LALA') == hash_table.lookup('LALA'), "Test failed"

    assert hash_table.calculate_hash_value(
        'LALAFA') == hash_table.calculate_hash_value('LAFAFA')

    assert hash_table.calculate_hash_value('UDACITY') == 8568

    with pytest.raises(SystemExit) as e:
        hash_table.calculate_hash_value('a')
        assert e.type == SystemExit

    with pytest.raises(SystemExit) as e:
        hash_table.calculate_hash_value('a')
        assert e.type == SystemExit

    with pytest.raises(SystemExit) as f:
        hash_table.calculate_hash_value('A')
        assert f.type == SystemExit

    with pytest.raises(AttributeError) as h:
        hash_table.calculate_hash_value(1)
        assert h.type == AttributeError


