import datetime
import os
import requests


# import environmental variables
Tequilla_Affill_ID = os.environ.get("AFFILL_ID")
Tequilla_API_KEY = os.environ.get("API_KEY")
tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"


class FlightSearch:

    """
        Get current flight information from Kiwi.com Tequila API
            Parameters:
                flight_from (str): Current location.
                flight_to (str):  Destination location.
                week_range (int): Interval in weeks from current date in which to search flight information.
    """

    def __init__(self, flight_from, flights_to, week_range, price_to, min_return_time_days, max_return_time_days):

        self.__flight_from = flight_from,
        self.__flight_to = flights_to
        self.__price_to = price_to

        # get current date
        today = datetime.date.today()
        self.__formatted_today = today.strftime("%d/%m/%Y")

        # get offset date
        offset_date = today + datetime.timedelta(weeks=week_range)
        self.__formatted_offset_date = offset_date.strftime("%d/%m/%Y")

        header = {
            "apikey": Tequilla_API_KEY
        }

        tequila_params = {
            "fly_from": self.__flight_from,
            "fly_to": self.__flight_to,
            "date_from": self.__formatted_today,
            "data_to": self.__formatted_offset_date,
            "price_to": self.__price_to,
            "one_for_city": 1,
            "curr": "USD",
            "nights_in_dst_from": min_return_time_days,
            "nights_in_dst_to": max_return_time_days,
            "flight_type": "round"
        }

        self.__response = requests.get(url=tequila_endpoint, params=tequila_params, headers=header)

    def get_flight_data(self):

        """
            Get one available flights for current flight object if price is lower than reference max price.
                Return:
                    self.__response (json): Returns available flight data from Tequila API
        """

        return self.__response.json()

    def get_date(self):

        """
            Get current date.
                Return:
                    self.__formatted_today (str): Returns current date.
        """

        return self.__formatted_today

    def get_offset_date(self):

        """
            Get date offset by provided number of weeks from current date.
                Return:
                    self.__formatted_offset_date (str): Returns current date.
        """

        return self.__formatted_offset_date





