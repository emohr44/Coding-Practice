# Define a function by writing def followed by the function name
# Place the arguments or parameters in the proceeding parantheses
# Follow with a colon, then indent on the next line
# Python identifies blocks through indentation
def say_hello(friends):
	# This is a for loop. It will iterate through each item friend in the 
	# list friends. Use the pattern for item in items:
	# Then begin a new block
    for friend in friends:
    	print "Hello, " + friend
    print "Goodbye, friends"

 # Say hello to everyone in a list of friends  
friends = ["World", "Jack"]
say_hello(friends)  