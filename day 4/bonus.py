filenames = ["1. Raw data.txt", "2. Reports.txt", "3. Presesantion.txt"]

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)