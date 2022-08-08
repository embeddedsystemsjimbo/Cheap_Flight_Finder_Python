from data_manager import DataManager
from flight_data import FlightData
from twillio import TwillioSMS

WEEK_OFFSET = 24
CURRENT_LOCATION = "LON"  # London GB city code

# get data from Google Sheets Reference Flight List
reference_flight_data = DataManager().get_city_list()

# get current available flights with prices
current_flight_data = FlightData(reference_flight_data, CURRENT_LOCATION, WEEK_OFFSET).get_flight_data()

for current_fight in current_flight_data:

    message = f"Low Price alert! Only ${current_fight['price']}US to fly from {current_fight['from_location']}-" \
              f"{current_fight['from_IATA']} to {current_fight['to_location']}-{current_fight['to_IATA']} from " \
              f" {current_fight['current_date']} to {current_fight['offset_date']}."

    # send text message to phone
    TwillioSMS(message)
