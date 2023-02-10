import csv
def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   d = csv.reader(data, delimiter=(','))
   x = []
   for i in d:
    x.append(i)
   return x[1] 

# Read the csv file
data = open('data.csv', 'r')
print(get_first_row(data))