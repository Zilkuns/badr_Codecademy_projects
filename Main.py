import csv

insurances ={}
columns = []
line_one = True
with open("insurance.csv", "w",newline="") as csv_file:
    reader = csv.reader(csv_file)
    j = 1
    for row in reader:
        internal_dict= {}
        i = 0
        split_row=row.split(',')
        if line_one:
            for column in split_row:
                columns.append(column)
            line_one = False
        else:
            split_row = row.split(",")
            for value in split_row:
                internal_dict[columns[i]] = value
                i +=1
        insurances["insurance-"+str(j)] =  internal_dict
        j +=1
for key , values in insurances.items():
    print(key +  "values are:")
    print(values)