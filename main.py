from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

WEEK_OFFSET = 24 # search interval in weeks ~ 6 months.
MIN_RETURN_TIME_DAYS = 7  # 7 days min trip length
MAX_RETURN_TIME_DAYS = 30  # 30 days max trip length
CURRENT_LOCATION = "LON"  # London GB city code ...default location.

# get data from Google Sheets Reference Flight List
reference_flight_data = DataManager().get_city_list()

# get current available flights with prices
current_flight_data = FlightData(reference_flight_data_container=reference_flight_data,
                                 current_location=CURRENT_LOCATION,
                                 date_offset_in_week=WEEK_OFFSET,
                                 min_return_time_days=MIN_RETURN_TIME_DAYS,
                                 max_return_time_days=MAX_RETURN_TIME_DAYS).get_flight_data()

for current_fight in current_flight_data:

    message = f"Low Price alert! Only ${current_fight['price']}US to fly from {current_fight['from_location']}-" \
              f"{current_fight['from_IATA']} to {current_fight['to_location']}-{current_fight['to_IATA']} between " \
              f" {current_fight['current_date']} to {current_fight['offset_date']}"

    # send text message to phone
    NotificationManager(message)
