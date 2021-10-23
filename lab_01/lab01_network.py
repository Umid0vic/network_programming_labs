#lab 1
#printing hello world and exploring Python!

print("Hello world!")

####  Numbers ####
tax = 12 / 100
# division always returns a floating point number
price = 100
print ("printing some numbers")
print ( tax * price )


#### Strings ####
a = "String using double quotes"
b = 'String using single quotes'
c = 'Use \' to escape quotes'
print(a)
print(b)
print(a + b)

# String literals can span multiple lines. We can use it with triple-quotes
print('''
Usage: thingy [OPTIONS]
	-h			Display this usage message
	-H hostname		Hostname to connect to
''')

# To concatenate strings use + operator. To repeat strings use * operator
hello = 'hello '
world = 'world'
print(2 * hello + world)

print('Put several strings within parantheses'
	'to have them joined')

