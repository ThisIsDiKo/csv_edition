import csv

folder_name = 'csv_orig/'
filenames = [
    '2018 140-2.csv',
    '2019 140-2.csv',
    '2020 140-2.csv',

    '2018 140-3.csv',
    '2019 140-3.csv',
    '2020 140-3.csv',

    '2018 160D1.csv',
    '2019 160D1.csv',
    '2020 160D1.csv',

    '2018 180D1.csv',
    '2019 180D1.csv',
    '2020 180D1.csv',

    '2018 250-2.csv',
    '2019 250-2.csv',
    '2020 250-2.csv'
]

for filename in filenames:
    fullFileName = folder_name + filename
    print(filename)
    data = []
    with open(fullFileName) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        t = []
        for row in spamreader:
            print(', '.join(row))
            t.append(row)

        for i in range(4, len(t[0]), 3):
            #print('week: {0} {1} {2}'.format(int(i/3), t[3][i-1], t[3][i]))
            slice = []

            if t[0][i-2].isdigit():
                v = int(t[0][i-2]) - 1
                v = str(v)
                slice.append(v)
            else:
                slice.append(t[0][i - 2])

            if t[3][i - 2] == '':
                slice.append('0')
            else:
                slice.append(t[3][i - 2])

            if t[3][i - 1] == '':
                slice.append('0')
            else:
                slice.append(t[3][i - 1])

            if t[3][i] == '':
                slice.append('0')
            else:
                slice.append(t[3][i])

            data.append(slice)

    cols = ['week', 'income', 'expense', 'balance']
    data.insert(0, cols)
    for slice in data:
        print(slice)


    f_name = 'csv_formatted/{0}.csv'.format(filename.split('.')[0]+'_formatted')

    with open(f_name, 'w') as file:
        writer = csv.writer(file, lineterminator="\r")
        writer.writerows(data)
