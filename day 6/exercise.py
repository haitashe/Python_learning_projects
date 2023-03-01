# 1

# file = open('files/essay.txt', 'r')
# some = file.read()
# print(some.title())

# 2
#
# file = open('files/essay.txt', 'r')
# content = file.read()
#
# nr_chars = len(content)
#
# print(nr_chars)


# 3
# member = input("Add a new member: ")
#
# file = open("files/members.txt", 'r')
# existing_members = file.readlines()
# file.close()
#
# existing_members.append(member + "\n")
#
# file = open("files/members.txt", 'w')
# existing_members = file.writelines(existing_members)
# file.close()
#
# print(file)

# # 4
#
# files = ['files/subfiles/1.txt',
#          'files/subfiles/2.txt',
#          'files/subfiles/3.txt'
#          ]
#
# for file in files:
#     filex = open(file, 'w')
#     filex.write("Hello")
#     filex.close()


# 5

files = ['more_files/a.txt',
         'more_files/b.txt',
         'more_files/c.txt'
         ]

for file in files:
    filex = open(file, 'r')
    content = filex.read()
    print(content)
