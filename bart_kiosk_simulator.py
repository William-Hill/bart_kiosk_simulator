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



def main():
	DUBLIN_PLEASANTON = ["Dublin/Pleasanton", "West Dublin/Pleasanton", "Castro Valley", "Bay Fair", "San Leandro", "Coliseum", "Fruitvale", "Lake Merritt", "West Oakland", "Embarcadero", "Montgomery St.", "Powell St.", "Civic Center/UN Plaza", "16th St. Mission", "24th St. Mission", "Glen Park", "Balboa Park","Daly City"]
	print "Station List: "
	print DUBLIN_PLEASANTON
	starting_point = raw_input("Where are you boarding the train? ")
	if starting_point in DUBLIN_PLEASANTON:
		starting_station = DUBLIN_PLEASANTON.index(starting_point)
	else:
		"There's no such BART station"
	end_point = raw_input("What is your destination? ")
	if end_point in DUBLIN_PLEASANTON:
		destination_station = DUBLIN_PLEASANTON.index(end_point)		
	else:
		"You're heading towards nowhere"

	calculate_fare(DUBLIN_PLEASANTON, starting_station, destination_station)
	
if __name__ == '__main__':
	main()