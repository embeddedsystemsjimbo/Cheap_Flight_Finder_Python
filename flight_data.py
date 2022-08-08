from flight_search import FlightSearch


class FlightData:

    """
        Organize reference and flight data.
            Parameters:
                reference_flight_data_container (DataManger): Reference Flight Data object.
                current_location (str): Current city location IATA code.
                date_offset_in_week (int): Interval in weeks from current date in which to search flight information.
    """

    def __init__(self,
                 reference_flight_data_container,
                 current_location,
                 date_offset_in_week,
                 min_return_time_days,
                 max_return_time_days):

        self.__destination_price_list = []

        for ref_destination in reference_flight_data_container:

            new_flight_search = FlightSearch(current_location,
                                             ref_destination["iataCode"],
                                             date_offset_in_week,
                                             ref_destination["lowestPrice"],
                                             min_return_time_days,
                                             max_return_time_days
                                             )

            search_result = new_flight_search.get_flight_data()

            try:
                for destination in search_result["data"]:
                    self.__destination_price_list.append({
                        "from_location": destination["cityFrom"],
                        "to_location": destination["cityTo"],
                        "from_IATA": destination["cityCodeFrom"],
                        "to_IATA": destination["cityCodeTo"],
                        "price": destination["price"],
                        "current_date": new_flight_search.get_date(),
                        "offset_date": new_flight_search.get_offset_date()
                    })
            except KeyError:
                print("No available flights")

    def get_flight_data(self):

        """
            Get current flight data.
                Returns:
                    self.__destination_price_list (dict): Returns list of available flight deals.
        """

        return self.__destination_price_list
