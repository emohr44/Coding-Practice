phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

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

phonebook["Jake"] = 938273443
del phonebook["Jill"]

if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

#this is a dictionary that stores the number of each item in an inventory
myInv = {
	"Pencil" : 6,
	"Pen" : 8,
	"Paper" : 5,
	"Desk" : 2,
	"Folder" : 3
}

def addItem(new, number, inv):
	inv[new] = number

def delItem(new, inv):
	del inv[new]

def reduceValue(new, number, inv):
	inv[new] = inv[new] - number 
	
	if inv[new] < 0:
		print "There are not enough items to fill this order."

def increaseValue(new, number, inv):
	inv[new] = inv[new] + number

addItem("Table", 3, myInv)

delItem("Pencil", myInv)

reduceValue("Pen", 5, myInv)

increaseValue("Desk", 3, myInv)

print myInv


