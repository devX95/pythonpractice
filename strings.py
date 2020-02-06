msg = "hello world"
print(len(msg))
# [start:stop:step]
print(msg[0:11:3])
# up to but not including
print(msg[:3])
# start from but not including
print(msg[0:3])
# step size only
print(msg[:3:3])
# reverse string
print(msg[::-1])

name = "Sam"
last_letters = name[1:]

print('P' + last_letters)

print(name.upper())

print(name.swapcase())

print(msg.split('l'))

welcome = 'Hello {lastName} {lastName}'

print(welcome.format(firstName='Gibran', lastName='Gul'))

result = 10000/777

print('The result is {r:10.5f}'.format(r=result))

print(f'The result is {result:1.5f}')