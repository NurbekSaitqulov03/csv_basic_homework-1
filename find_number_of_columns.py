def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    x = data.split()
    return len(x[0].split(','))

# Read the csv file
data = open('data.csv', 'r').read()
print(find_number_of_columns(data))