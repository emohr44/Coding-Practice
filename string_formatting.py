# This prints out "Hello, John!"
name = "John"
print "Hello, %s!" % name

# This prints out "John is 23 years old."
name = "John"
age = 23
print "%s is %d years old." % (name, age)

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print "A list: %s" % mylist

# This prints out "John is 23 years old."
name = "John"
age = 23
print "%s is %d years old." % (name, age)

month_name = "January" 
month_num = 1
day = 19
year = 2017
print "the date is %s %d %d. " % (month_name, day, year)
print "Today is %d / %d / %d." % (month_num, day, year)
print "today is the %dth of %s %d" % (day, month_name, year)
