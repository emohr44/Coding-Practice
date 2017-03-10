# This script introduces the concept of data types such as of 
# integers and stings. We cast strings as integers and visaversa so 
# that we can add integers and concatenate strings.  
 
one, two = 1, 2
three = one + two
four = "4"
seven = int(four) + three
print three
print seven 

hello, world = "hello", "world"
helloworld = hello + " " + world
print helloworld

print helloworld + " " + str(three)
