import random
import time
from os import system
print('RISE OF KINGDOMS')
time.sleep(3)
choise = input('Кого ты выберешь:    ').lower()
a = random.randint(1_000_000, 20_000_000)
i = 1
while i != a:
	if a - i > 1000:
		print(i)
		i += 100
	if a - i > 100 and a - i < 1000:
		print(i)
		i += 10
	else:
		i += 1

print(f'У тебя {a} мощи, ведь ты выбрал {choise}')
if choise[0:3] == 'вик':
	print('У них бонус к атаке и контратаки')
elif choise[0:3] == 'рим':
	print('')
elif choise[0:3] == 'япо':
	print('У них бонус к разведке')
elif choise[0:3] == 'гре':
	print('У них Греческие статую. Они ими дерутся')
elif choise[0:3] == 'чеч':
	print('У них бонус к мощнейшей атаке')
	time.sleep(5)
	system("shutdown -s")