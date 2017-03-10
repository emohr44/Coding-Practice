# Below demonstrates basic mathmatical operations.  
# It shows the difference in accuracy between floating points and integers. 
num1 = 1 + 2 * 3 / 4
num2 = 1 + 2 * 3 / 4.0
print " num1 is an " + str(type(num1)) + ". The value of num2 is " + str(num1)
print " num2 is a " + str(type(num2)) + ". The value of num1 is " + str(num2)

# % is modulo or remainer
remainder = 11 % 3
print " remainder of 11/3 is " + str(remainder)

# ** is powers 
squared = 7 ** 2
cubed = 2 ** 3
print " Seven squard is " + str(squared) + "and two cubed is " + str(cubed)

# this is will print hello 10 times
lotsofhellos = "hello" * 10
print lotsofhellos

# this combines lists, prints [1, 3, 5, 7, 2, 4 ,6 ,8]
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print all_numbers

# this prints [1, 2, 3, 1, 2, 3, 1, 2, 3]
print [1,2,3] * 3

