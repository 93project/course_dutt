# import module

# command = input('Введите команду\n')

# command = command.lower()

# if command == 'изменить базу':
# 	changes = input('Что вы хотите изменить?').lower()
p = int(input('Введите число\n'))

if p > 10:
	exit(1)

# while p <= 10:
# 	if p % 2 == 0:
# 		print(p)
# 	p+=1

for k in range(p+1, 11):
	if k % 2 == 0:
		print(k)
