# Ex 1

class Hotel():
	def __init__(self, name_of_hotel, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price, discount_for_hotel):
		self.name_of_hotel = name_of_hotel
		self.place = place
		self.rooms_mid = {"room1": "free", "room2": "free", "room3": "free"}
		self.mid_room_price = mid_room_price
		self.rooms_lux = {"room1": "free", "room2": "free", "room3": "free"}
		self.lux_room_price = lux_room_price
		self.discount_for_hotel = discount_for_hotel

	def presentation1(self):
		return f"We suggest you hotel {self.name_of_hotel} it is located in {self.place}."

	def booking(self):
		for i in self.rooms_mid:
			self.rooms_mid[i] = "busy"
		return self.rooms_mid

	def available_room_check(self):
		for i in self.rooms_mid:
			if self.rooms_mid[i] == "free":
				return f"There is a free middle room."
		for i in self.rooms_lux:
			if self.rooms_lux[i] == "free":
				return f"There is a free lux room."

	def dicscount1(self):
		return f"With your discount of {self.discount_for_hotel} % the price for the standard room is {self.lux_room_price - (self.lux_room_price * self.discount_for_hotel / 100)} $ and for the lux it is {self.mid_room_price - (self.mid_room_price * self.discount_for_hotel / 100)} $."


class Taxi():
	def __init__(self, name_of_taxi, car_types, price_for_tour, discount_for_taxi):
		self.name_of_taxi = name_of_taxi
		self.car_types = car_types
		self.price_for_tour = price_for_tour
		self.discount_for_taxi = discount_for_taxi

	def presentation2(self):
		return f"The name of your taxi is {self.name_of_taxi} its model is {self.car_types}."

	def discount2(self):
		return f"The price for the tour is equal to {self.price_for_tour} $ and with your discount it will be {self.price_for_tour - (self.price_for_tour * self.discount_for_taxi / 100)} $."


class Tour(Hotel, Taxi):
	def __init__(self, name_of_hotel, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price, discount_for_hotel, name_of_taxi, car_types, price_for_tour, discount_for_taxi, name, price_lux, price_mid):
		Hotel.__init__(self, name_of_hotel, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price, discount_for_hotel)
		Taxi.__init__(self, name_of_taxi, car_types, price_for_tour, discount_for_taxi)
		self.name = name
		self.price_lux = price_lux
		self.price_mid = price_mid

	def globalpresentation(self):
		return f"The total amount of standard tour is equal to {self.price_mid} $" \
		f"and for the lux it is {self.price_lux} $. It includes the price of hotel and taxi." \
		f" We suggest you hotel {self.name_of_hotel} it is located in {self.place}." \
		f" With your discount of {self.discount_for_hotel} % the price for the standard room in" \
		f"this hotel is {self.lux_room_price - (self.lux_room_price * self.discount_for_hotel / 100)} $" \
		f"and for the lux it is {self.mid_room_price - (self.mid_room_price * self.discount_for_hotel / 100)} $."\
		f"The name of our taxi service is {self.name_of_taxi} the model of its cars is {self.car_types}." \
		f"The price for the tour is equal to {self.price_for_tour} $ and with your discount it will be " \
		f"{self.price_for_tour - (self.price_for_tour * self.discount_for_taxi / 100)} $."

my_tour = Tour("Double Tree", "The City Center", "middle", 1000, "lux", 500, 20, "Dream", "Mercedes ML350", 1000, 10, "Rome", 1700, 1300)
print(my_tour.globalpresentation())


# Ex 2

class HouseHeating():
	def __init__(self, room_temp, current_temp, goal_temp):
		self.room_temp = room_temp
		self.current_temp = current_temp
		self.goal_temp = goal_temp

	def get_temp(self):
		return f"The temperature in the room is {self.room_temp} °C." \
		f"The current temperature is {self.current_temp} °C." \
		f"And we want to reach to to the {self.goal_temp} °C."

	def check(self):
		if self.current_temp == self.goal_temp:
			return "The preferable temperature is reached."
		else:
			return "We need to change the temperature."

house1 = HouseHeating(25, 23, 28)
house2 = HouseHeating(24, 27, 27)
house3 = HouseHeating(23, 26, 26)
house4 = HouseHeating(21, 23, 25)

answer1 = house1.check()
answer2 = house2.check()
answer3 = house3.check()
answer4 = house4.check()

answers = [answer1, answer2, answer3, answer4]

def calc(list_of_answers):
	count = 0
	for i in answers:	
		if i == "The preferable temperature is reached.":
			count += 1
	return f"The number of houses with preferable temperatures is {count}."

print(calc(answers))