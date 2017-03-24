# This a class that describes my pet

class myPet:
	
	# This initializes the object with name, breed, color, and sound. 
	def __init__(self, myName, myBreed, myColor, mySound): 
		self.name = myName
		self.breed = myBreed
		self.color = myColor
		self.sound = mySound

	def make_sound(self):
		print (self.sound)


pet1 = myPet("Jack", "Spaniel", "brown", "woof")
pet2 = myPet("Pat", "Retriever", "black", "bark")
	
print "My first pets name is %s and it is a %s %s." % (pet1.name, pet1.color, pet1.breed)
print "My first pets name is %s and it is a %s %s." % (pet2.name, pet2.color, pet2.breed)

pet1.make_sound()

class complexNum:

	def __init__(self, real, imaginary):
		self.re = real
		self.im = imaginary

	def add(self, complex): 
		self.re = self.re + complex.re 
		self.im = self.im + complex.im

	def sub(self, complex):
		self.re = self.re - complex.re
		self.im = self.im - complex.im

a = complexNum(2, 3)
b = complexNum(4, 5)

a.add(b)

print "a = %d + %di" % (a.re, a.im)



