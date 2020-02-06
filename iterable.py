my_iterable = [1,2,3]
for x in my_iterable:
  if x % 2 == 0:
    print(f'EvenNumber: {x}')
  else:
    print(f'OddNumber: {x}')

list_sum = 0

for num in my_iterable:
  list_sum += num

print(list_sum)


# tuple unpacking
my_list = [(1,2), (3,4), (5,6), (7,8)]
for a,b in my_list:
  print(a)
  print(b)

# dictionary Iteration
d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d.items():
  print(d)

for key, value in d.items():
  print(value)

x = 10
while x < 5:
  print(f'The current value of x is {x}')
  x += 1
else:
  print('X is not less than 5')


# continue goes to top
# break ends the loop
# pass ignores
my_string = "Sammy"
for letter in my_string:
  if letter == 'a':
    break
  print(letter)
# Result 
# S


for num in range(0,11,2):
  print(num)
# Result
# 0
# 2
# 4
# 6
# 8
# 10


index_count = 0
for letter in 'abcde':
  print(f'At index {index_count} the letter is {letter}')
  index_count += 1
# Result
# At index 0 the letter is a
# At index 1 the letter is b
# At index 2 the letter is c
# At index 3 the letter is d
# At index 4 the letter is e


word = 'abcde'
for index, letter in enumerate(word):
  print(f'{index}: {letter}')
# Result
# 0: a
# 1: b
# 2: c
# 3: d
# 4: e


my_list1 = [1, 2, 3, 4]
my_list2 = ['a', 'b', 'c']
for item in zip(my_list1, my_list2):
  print(item)
# Result:
# (1, 'a')
# (2, 'b')
# (3, 'c')


if 'a' in my_list2:
  print('Present')
# true


print(min(my_list1))
# 1


print(max(my_list1))
# 4


from random import shuffle, randint

shuffle(my_list1)
print(my_list1)

# from random import randint

print(randint(0,100))

# result = input('Enter a number here: ')
# print(float(result))


my_new_list = [num**2 for num in my_list1 if num % 2 == 0]

print(my_new_list)