# Network programming lab 4 - Python: Generators
# created by Osman Said 2021-11-02

def fibonacci(n):
	print('Fibonacci series:')
	a, b = 0, 1
	while a < n:
		yield a 
		a, b = b, a+b

for i in fibonacci(1000):
	print (i) 
