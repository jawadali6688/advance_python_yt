# file = open('apple.txt', 'r')

# print(file.read())

# file.close()


# with open('files/new_apple.txt', 'r') as apple_file:
#     content = apple_file.read(20)
#     # content = apple_file.readline(2)
#     # print(content)
#     # content = apple_file.readlines(4)
#     print(content)

#     # for line in content:
#     #     print(line)


# with open('apple.txt', 'w') as file:
#     file.write('This is my new content')


# with open('apple.txt', 'a') as file:
#     file.write('\nThis is my new content in second line')

import os

os.remove('files/new_apple.txt')