class Pet:
	number_of_pets = 0
	#constructor
	def __init__(self,name,species):
		self.name = name
		self.species = species
		Pet.number_of_pets+=1
	def get_name(self):
		return self.name
	def get_species(self):
		return self.species
my_pet1 = Pet("polly","parrtot")
my_pet2 = Pet("Tom","dog")
print("My pet {0} is a {1}".format(my_pet1.name,my_pet1.species))
print("My pet {0} is a {1}".format(my_pet2.name,my_pet2.species))
print("Now, I have %d pets" % Pet.number_of_pets)
print("Name: %s| Species %s"% (my_pet1.get_name(),my_pet1.get_species()))

