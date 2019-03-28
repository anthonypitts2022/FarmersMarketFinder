def read_markets(filename):
    #A dictionary mapping zip codes to lists of farmers markets
    zip_to_markets = {} 
    #A dictionary mapping towns to set of zipcodes
    town_to_zip = {}
    with open(filename, 'r') as f:
        for line in f:
            market_as_list = line.split("#")
                                        
            #if zipcode is already in dict, then append to market list
            if(market_as_list[4] in zip_to_markets):
                zip_to_markets[market_as_list[4]].append(market_as_list)
            #if zipcode is not in dict, then create a market list
            else:
                zip_to_markets[market_as_list[4]] = [market_as_list]
                
            #if town is already in dict, then append to zipcode set
            if(market_as_list[3] in town_to_zip):
                town_to_zip[market_as_list[3]].add(market_as_list[4])
            #if town is not in dict, then make new zipcode set
            else:
                town_to_zip[market_as_list[3]] = {market_as_list[4]}
            
    return (zip_to_markets, town_to_zip)
            

def print_market(market):
    market_string = "{}\n{}\n{}, {} {}"
    return market_string.format(market[1], market[2], market[3], market[0], market[4])

if __name__ == "__main__":
    FILENAME = "markets.txt"
    try: 
        zip_to_market, town_to_zips = read_markets(FILENAME)
        user_input = input("Enter a zipcode or town name or type 'quit': ")
        while (user_input != "quit"):
            #finds if input is zipcode or not
            isNumeric = True
            numericList = ["0","1","2","3","4","5","6","7","8","9"]
            for i in user_input:
                if(i not in numericList):
                    isNumeric = False
            #if userInput is zipcode
            if(isNumeric):
                if(user_input in zip_to_market):
                    markets_of_zip = zip_to_market[user_input]
                    for this_ind_market in markets_of_zip:
                        print(print_market(this_ind_market))
                else:
                    print("Not found.")
                
            #if userInput is town
            else:
                if(user_input in town_to_zips): 
                    zipcodes_from_town = town_to_zips[user_input]
                    any_zip_to_market = False
                    for ind_zip in zipcodes_from_town:
                        if(ind_zip in zip_to_market):
                            any_zip_to_market = True
                            markets_at_zip = zip_to_market[ind_zip]
                            for ind_market in markets_at_zip:
                                print(print_market(ind_market))
                    if(any_zip_to_market==False):
                        print("Not found.")
                else:
                    print("Not found.")
            user_input = input("Enter a zipcode or town name or type 'quit': ")

    except (FileNotFoundError, IOError): 
        print("Error reading {}".format(FILENAME))
