my_file = open('test.txt')
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.readlines())
my_file.seek(0)
my_file.close()

with open('test.txt') as my_new_file: contents = my_new_file.read()

print(contents)

with open('test.txt',mode='r+') as annother_file: newContents = annother_file.read()

print(newContents)