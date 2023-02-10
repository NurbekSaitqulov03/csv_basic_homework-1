import csv
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    x = csv.reader(data, delimiter=",")
    a = []
    for i in x:
        a.append(i[0])
    return a
# Read the csv file
data = open('data.csv', 'r')
print(get_first_column(data))