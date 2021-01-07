# Ex 1-3

class StrToDict():

	def makedict(self, my_string):
		mydict = dict()
		mylist = []
		newdict = dict()
		for i in my_string:
	 		mydict[i] = my_string.count(i)
		for i, j in mydict.items():
			if j not in mylist:
				mylist.append(j)
				newdict[i] = j
		newlist = []
		finaldic = dict()
		for i in mydict:
			newlist.append(mydict[i])
		newlist.sort()
		newlist.reverse()
		newlist = newlist[0: 3]
		return f"A dictionary according to your string is {mydict}.\nA dictionary without duplicate values is {newdict}.\nThe largest three values in your dictionary are {newlist}."

giv_str = input("Give me a string and I will return it to a dictionary, remove duplicate values and find the highest 3 values: ")
mystr = StrToDict()
print(mystr.makedict(giv_str))

# Ex 4

class Circle():

	def __init__(self, radius):
		self.radius = radius

	def circlearea(self):
		return f"The area of your circle is equal to {round(3.14 * self.radius ** 2, 1)}."

	def circleperimeter(self):
		return f"The perimeter of your circle is equal to {round(2 * 3.14 * self.radius, 1)}."

the_radius = int(input("Insert the radius of the circle and I will calculate its area and perimeter: "))
my_circle = Circle(the_radius)

print(my_circle.circlearea())
print(my_circle.circleperimeter())

# Ex 5

class FindPair():

 	def __init__(self, mylist, target):
 		self.mylist = mylist
 		self.target	= target

 	def pairofindices(self):
 		newlist = self.mylist.copy()
 		pairs = dict()
 		indices = []
 		for i in self.mylist:
 			for j in self.mylist:
 				if i + j == self.target:
 					pairs[i] = j
	 				if i in self.mylist:
	 					self.mylist.remove(i)
	 				if j in self.mylist:
	 					self.mylist.remove(j)
 		for i, j in pairs.items():
 			indices.append({newlist.index(i) + 1: newlist.index(j) + 1})
 		return indices

the_list = [10,20,10,40,50,60,70,30,0]
the_target = 50
myoption = FindPair(the_list, the_target)
print(f"The indices of numbers in the given {the_list} list which sum is equal to {the_target} are {myoption.pairofindices()}")