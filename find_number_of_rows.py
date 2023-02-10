def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    
    return len(data.split('\n')[1:-1])

# Read the csv file
data = open('data.csv', 'r').read()
print(find_number_of_rows(data))