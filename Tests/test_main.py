from Scripts import main
import random
import string

"""Test function to test ALL main.py functions"""
def test_calculate_hash_value():

    hash_table = main.HashTable()

    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k = random.randint(2, 150)))

    hash_table.store(random_string)

    assert hash_table.calculate_hash_value(random_string) == hash_table.lookup(random_string), "Test failed"
    assert hash_table.calculate_hash_value(random_string) != -1
