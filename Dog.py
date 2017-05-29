from random import randint
import csv # comma seperated values



class Dog(object):


	# Constructor
	def __init__(self, initName="Jim"):
		self.numLegs = 4
		self.isAlive = True
		self.color = "brown"
		self.height = 10
		self.name = initName



	# ---  Methods  ---
	def grow(self):
		self.height += 2

	def paintDog(self, newColor):
		self.color = newColor

	def printStatus(self):
		if not self.isAlive:
			print("Roll Credits")
		elif self.height < 16:
			print("Movie just started")
		else:
			print("Pupper is now",self.height,"inches tall")

# x = randint(0,10)
# print(x)


# dogList = []

# buddy = Dog("Buddy")
# buddy.grow()
# dogList.append(buddy)

# lou = Dog("Dog")
# lou.paintDog("blue")
# lou.grow()
# lou.grow()
# lou.grow()
# lou.grow()
# dogList.append(lou)

# marley = Dog("Marley")
# marley.isAlive = False
# dogList.append(marley)


# for dog in dogList:
# 	dog.printStatus()





# def printList(list):
# 	for s in list:
# 		print(s)


# x = [2,5,3,78]
# printList(x)