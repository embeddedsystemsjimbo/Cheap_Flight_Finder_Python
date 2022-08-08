import requests
import os

Sheety_API_KEY = os.environ.get("SHEETY_API_KEY")


class DataManager:

    """
        Get reference flight information from Google Sheets document
    """

    def __init__(self):

        flights_endpoint = "https://api.sheety.co/7c81d9be8a3fc40fb73b464d6005dd73/flights/sheet1"

        header = {
            "Authorization": Sheety_API_KEY
        }

        response = requests.get(url=flights_endpoint, headers=header).json()

        self.__city_list = [city for city in response["sheet1"]]

    def get_city_list(self):

        """
            Get list potential travel destinations.
                Return:
                    self.__city_list (str): Return list of potential destination cities.
        """

        return self.__city_list






