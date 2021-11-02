"""Module that generates a Hash Table"""
class HashTable():
    """Class that generates a Hash Table"""

    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in
        the table."""
        hv = self.calculate_hash_value(string)

        if self.lookup(string) == -1:

            if self.table[hv] != None:

                self.table[hv].append(string)

            else:

                self.table[hv] = [string]
        else:
            print("This string is already present in a table")

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hv = self.calculate_hash_value(string)

        if self.table[hv] != None:
            if string in self.table[hv]:
                return hv
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        if string.isupper():
            try:

                value = ord(string[0])*100 + ord(string[1])

            except IndexError:

                print(
                    "There must be at least two letters "
                    "in an input string. Please correct your code")
                exit()

            except TypeError:

                print("The input data must be a string. Please correct your code")
                exit()
        else:

            print('Input string should be uppercase')
            exit()
        return value


hash_table = HashTable()
