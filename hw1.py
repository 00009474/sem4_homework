
num = input("Put your Number: ")
num = int(num)

def countdown(n):

if n <= 0:
		print('Blastoff!')
	else:
		print(n)
		countdown(n-1)

def countup(n):
	if n >= 0:
		print('Blastoff')
	else:
		print(n)
		countup(n+1) #Here we just plus and have -3, -2 and etc

if num > 0:
  countdown(num) #Simple Calculations
elif num < 0:
  countup(num)
else:
  print('Blastoff!')