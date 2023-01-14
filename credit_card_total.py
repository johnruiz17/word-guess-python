"""
File: credit_card_total.py
--------------------------
This program totals up a credit card bill based on
how much was spent at each store on the bill.
"""


INPUT_FILE = 'bill1.txt'


def main():
    """
    This function reads the file and creates key-value pairs where
    the name of the store is the key, and the value is the current total of credit card charges for that store.
    Loops through each line in the file, if the key does not exist, creates key-value pair.
    Otherwise, adds the value in that line to total value for that existing key.
    """
    dictionary = {}
    with open(INPUT_FILE) as file:
        for line in file:
            line = line.strip()
            key = get_key(line)
            value = get_value(line)
            if key not in dictionary:
                dictionary[key] = value
            else:
                total_value = dictionary[key]
                total_value += value
                dictionary[key] = total_value

        for key in dictionary:
            print(f'{key}: ${dictionary[key]}')


def get_key(line):
    """
    Returns the key which represents the name of the store for that line in the file.
    """
    key_start = line.find('[') + 1
    key_end = line.find(']')
    key = line[key_start:key_end]

    return key


def get_value(line):
    """
    Returns the value which represents the credit card charge for that line in the file.
    """
    value_start = line.find('$') + 1
    value_end = len(line)
    value = int(line[value_start:value_end])

    return value

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
