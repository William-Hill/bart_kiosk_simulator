def load_card(one_dollar_bills,five_dollar_bills,ten_dollar_bills,twenty_dollar_bills):
	ones = one_dollar_bills * 1
	fives = five_dollar_bills * 5
	tens = ten_dollar_bills * 10
	twenties = twenty_dollar_bills * 20
	print "You entered %i $1 bills, %i $5 bills, %i $10 bills, and %i $20 bills" % (one_dollar_bills,five_dollar_bills,ten_dollar_bills,twenty_dollar_bills)
	return float(ones + fives + tens + twenties)


def travel_to_destination(fare_price,card_value):
	if card_value > fare_price:
		print "Welcome aboard, enjoy your trip!"
	else:
		print "You need more money!"



def calculate_fare(bart_line,start_point,end_point):
	if start_point > end_point:
		trip = bart_line[start_point:end_point-1: -1]
	else:
		trip = bart_line[start_point:end_point+1]
	print trip
	total = len(trip) * 1.25
	return total

def choose_destination(bart_line_stations_list):
	station_indexes = []
	print "Station List: "
	print bart_line_stations_list

	starting_station_name = raw_input("Where are you boarding the train? ")

	if starting_station_name in bart_line_stations_list:
		starting_station_index = bart_line_stations_list.index(starting_station_name)
		station_indexes.append(starting_station_index)
	else:
		"There's no such BART station"

	destination_station_name = raw_input("What is your destination? ")

	if destination_station_name in bart_line_stations_list:
		destination_station_index = bart_line_stations_list.index(destination_station_name)		
		station_indexes.append(destination_station_index)
	else:
		"You're heading towards nowhere"
	return station_indexes

def main():
	DUBLIN_PLEASANTON = ["Dublin/Pleasanton", "West Dublin/Pleasanton", "Castro Valley", "Bay Fair", "San Leandro", "Coliseum", "Fruitvale", "Lake Merritt", "West Oakland", "Embarcadero", "Montgomery St.", "Powell St.", "Civic Center/UN Plaza", "16th St. Mission", "24th St. Mission", "Glen Park", "Balboa Park","Daly City"]
	clipper_card = 0.00
	station_numbers = None
	trip_cost = 0.00
	exit = False
	while exit != True:
		print "1. Add money to card \n2. Choose Destination \n3. Calculate Fare \n4. Travel To Destination \n5. Exit"
		selection = int(raw_input("Please choose an action from the menu: "))
		if selection == 1:
			ones = int(raw_input("Enter the number of $1 bills?"))
			fives = int(raw_input("Enter the number of $5 bills?"))
			tens = int(raw_input("Enter the number of $10 bills?"))
			twenties = int(raw_input("Enter the number of $20 bills?"))
			clipper_card+=load_card(ones,fives,tens,twenties)
			print "Your new Clipper Card value is $%.2f" % (clipper_card)
		if selection == 2:
			station_numbers = choose_destination(DUBLIN_PLEASANTON)
			print "Starting station: %s" % (DUBLIN_PLEASANTON[station_numbers[0]])
			print "Destination station: %s" % (DUBLIN_PLEASANTON[station_numbers[1]])
		if selection == 3:
			trip_cost = calculate_fare(DUBLIN_PLEASANTON, station_numbers[0], station_numbers[1])
			print "Trip Cost: ", trip_cost
		if selection == 4:
			travel_to_destination(trip_cost,clipper_card)
		if selection == 5:
			exit = True
	# DUBLIN_PLEASANTON = ["Dublin/Pleasanton", "West Dublin/Pleasanton", "Castro Valley", "Bay Fair", "San Leandro", "Coliseum", "Fruitvale", "Lake Merritt", "West Oakland", "Embarcadero", "Montgomery St.", "Powell St.", "Civic Center/UN Plaza", "16th St. Mission", "24th St. Mission", "Glen Park", "Balboa Park","Daly City"]
	# 
	# starting_index = station_numbers[0]
	# destination_index = station_numbers[1]

	
	
if __name__ == '__main__':
	main()