class Flight():
	def __init__(self, capacity):
		self.capacity = capacity
		self.passengers = []

	def add_passengers(self, name):
		if not self.open_seats():
			return False
		self.passengers.append(name)
		return True

	def open_seats(self):
		return self.capacity - len(self.passengers)	

# We define the capacity of the flight
flight=Flight(5)

#We create a list of passengers
name_people = input("Enter passengers separated by space ")
people = name_people.split(" ")

for person in people:
	if flight.add_passengers(people):
		print(f"Added person with name {person}")
	else:
		print("There is no more place in the flight !")
