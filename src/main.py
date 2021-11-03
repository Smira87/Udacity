"""Module that generates a Hash Table"""
import sys
class HashTable():
    """Class that generates a Hash Table"""

    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in
        the table."""
        h_v = self.calculate_hash_value(string)

        if self.lookup(string) == -1:

            if self.table[h_v] is not None:

                self.table[h_v].append(string)

            else:

                self.table[h_v] = [string]
        else:
            print("This string is already present in a table")

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        h_v = self.calculate_hash_value(string)

        if self.table[h_v] is not None:
            if string in self.table[h_v]:
                return h_v
        return -1

    @classmethod
    def calculate_hash_value(cls, string):
        """Helper function to calulate a
        hash value from a string."""
        if string.isupper():
            try:

                value = ord(string[0])*100 + ord(string[1])

            except IndexError:

                print(
                    "There must be at least two symbols "
                    "in an input string. Please correct your code")
                sys.exit()

        else:

            print('Input string should be uppercase')
            sys.exit()
        return value


hash_table = HashTable()
