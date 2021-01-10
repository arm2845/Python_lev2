# Ex 1
class Person():
	def __init__(self, name, surname, age, nationality, education):
		self.name = name
		self.surname = surname
		self.age = age
		self.nationality = nationality
		self.education = education

	def ShortPresentation(self):
		return f"My name is {self.name} {self.surname}. I am {self.nationality} and I am {self.age} years old. I have {self.education}."

class Student(Person):
	def __init__(self, name, surname, age, nationality, education, university):
		Person.__init__(self, name, surname, age, nationality, education)
		self.university = university
	
	def university_(self):
		return f"Now I am studying in {self.university}."


student1 = Student("Armine", "Sargsyan", 24, "Armenian", "Master's degree", "ASUE")
print(student1.ShortPresentation())
print(student1.university_())


# Ex 2

class Country():
	def __init__(self, country_name, continent):
		self.country_name = country_name
		self.continent = continent

	def aboutcountry(self):
		return f"{self.country_name.title()} is located in {self.continent.upper()}."

class Brand():
	def __init__(self, brand_name, business_start_date):
		self.brand_name = brand_name
		self.business_start_date = business_start_date

	def aboutbrand(self):
		return f"{self.brand_name.title()} was found in {self.business_start_date}."

class Season():
	def __init__(self, season_name, average_temp):
		self.season_name = season_name
		self.average_temp = average_temp

	def aboutseason(self):
		return f"The average temperature in {self.season_name} is equal to {self.average_temp}."

class Product(Country, Brand, Season):
	def __init__(self, country_name, continent, brand_name, business_start_date, season_name, average_temp, product_name, product_type, product_price, product_quantity, percent):
		Country.__init__(self, country_name, continent)
		Brand.__init__(self, brand_name, business_start_date)
		Season.__init__(self, season_name, average_temp)
		self.product_name = product_name
		self.product_type = product_type
		self.product_price = product_price
		self.product_quantity = product_quantity
		self.percent = percent

	def aboutproduct(self):
		return f"The type of {self.product_name} is {self.product_type}, its price is {self.product_price} $ and the quantity is {self.product_quantity}."

	def discount(self):
		return f"The price of {self.product_name} after discount is equal to {self.product_price - (self.product_price * self.percent / 100)} $."

	def increasequantity(self):
		return f"According to today's calculations the quantity of {self.product_name} has increased and now it is {self.product_quantity + 20}."

product1 = Product("Armenia", "Asia", "Yerevan Ararat Brandy-Wine-Vodka Factory", 1877, "autumn", "20°C", "wine", "alcoholic drink", 50, 100000, 10)
print(product1.aboutcountry())
print(product1.aboutbrand())
print(product1.aboutseason())
print(product1.aboutproduct())
print(product1.discount())
print(product1.increasequantity())