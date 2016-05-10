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
	trip = bart_line[start_point:end_point+1]
	print trip
	total = len(trip) * 1.25
	print total

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
	print "Station List: "
	print DUBLIN_PLEASANTON
	station_numbers = choose_destination(DUBLIN_PLEASANTON)

	calculate_fare(DUBLIN_PLEASANTON, station_numbers[0], station_numbers[1])
	
if __name__ == '__main__':
	main()