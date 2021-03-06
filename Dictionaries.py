# This is an empty dictionary

phonebook = {}

 # These are the names and numebers in the dictionary. 
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

#This is a dictionary with names and values already encoded
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# This is deletes a  name and number from the dictionary 
phonebook["Jake"] = 938273443
del phonebook["Jill"]

if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

#this is a dictionary that stores the number of each item in an inventory
class myInv:

	# Initializes the inventory 
	def __init__ (self, inventory):
		self.inv = inventory

	# Adds a new name and number
	def addItem(self, new, number):
		self.inv[new] = number

	# Deletes a contact
	def delItem(self, new):
		del self.inv[new]

	# Reduces values of a contact
	def reduceValue(self, new, number):
		self.inv[new] = self.inv[new] - number 
		
		if self.inv[new] < 0:
			print "There are not enough items to fill this order."

	# Increases values of a contact
	def increaseValue(self, new, number):
		self.inv[new] = self.inv[new] + number

# This is a dictionary that stores the data
inv_dict = {
	"Pencil" : 6,
	"Pen" : 8,
	"Paper" : 5,
	"Desk" : 2,
	"Folder" : 3
}

# This is an instance of myInv
inv1 = myInv(inv_dict)

# An item is being added
inv1.addItem("Table", 3)

# An item is being deleted
inv1.delItem("Pencil")

# An item is being reduced
inv1.reduceValue("Pen", 5)

# An item is being increased
inv1.increaseValue("Desk", 3)

# This prints whats in the dictionary 
print inv1.inv



