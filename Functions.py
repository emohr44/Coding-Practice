def sum_two_numbers(a, b):
    return a + b

a = input("What would you like 'a' to equal?: ")
b = input("What would you like 'b' to equal?: ")

print "if a = %d, and b = %d, then a + b = %d" % (a, b, sum_two_numbers(a, b)) 


# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", " Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return benefit + " is a benefit of functions!"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

