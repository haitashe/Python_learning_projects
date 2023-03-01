items = [
    'This is a short sentence with 40 characters.',
    'This is a longer sentence that has 60 characters.',
    'This is the longest sentence with 70 characters.'
]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for item, filename in zip(items, filenames):
    file = open(f"files/{filename}", "w")
    file.write(item)
