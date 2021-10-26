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


#### Lists ####
squares = [1, 4, 9, 16, 25, 36]
print('printing a list...')
print(squares)
print('printing index 0 of the list..')
print(squares[0])
print('printing the last index of the list...')
print(squares[-1])
print('slicing the list using : operator...')
print(squares[3:])
print(squares[:3])
# Slice operators returns a new list containing the requested elements.
# This means that the following slice returns a shallow copy of the list.
print('copying the list...')
copied_list = squares[:]
print(copied_list)

print('Fibonacci series:')
a, b = 0, 1
while a < 10:
	print(a)
	a, b = b, a+b


#### More Control Flow Tools ####
# the range() and len() functions
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
    
print('Printing the sum of all numbers between the given range:')
sum(range(4))

# break and continue statements in for loops
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
            print(n, 'is a prime number')
            

# pass Statement does nothing. 
# Often used to create a mininal classes
class MyEmptyClass
    pass
    
# or in a functions that has not been implemented yet
def initLog(*args):
    pass ## TODO
    
# match Statement. Very similar to switch statements in other languages
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
            

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")