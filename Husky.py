from Dog import Dog

class Husky(Dog):


	def __init__(self, initName):
		#Dog(initName)
		super(Husky, self).__init__(initName)
		self.eyeColor = "blue"