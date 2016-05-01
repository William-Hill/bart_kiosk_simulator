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



def main():
	DUBLIN_TO_POWELL = 6.15
	FRUITVALE_TO_UNION_CITY = 3.80
	ORINDA_TO_RICHMOND = 3.35
	HAYWARD_TO_CONCORD = 5.20
	FREMONT_TO_COLMA = 6.60
	print "Test Cases"
	clipper_card1 = load_card(3,0,0,0)
	travel_to_destination(FREMONT_TO_COLMA,clipper_card1)

	clipper_card2 = load_card(1,0,0,1)
	travel_to_destination(HAYWARD_TO_CONCORD,clipper_card2)

	clipper_card3 = load_card(1,1,0,0)
	travel_to_destination(DUBLIN_TO_POWELL,clipper_card3)

	clipper_card4 = load_card(2,0,0,0)	
	travel_to_destination(FRUITVALE_TO_UNION_CITY,clipper_card4)
if __name__ == '__main__':
	main()