""" contains key functions such as get_next_passes(location:dict) and def print_next_pass(pass_data: dict)

    get_next_passes(location:dict): gets five future passes of the international space station based on
    any given location in the world and formats them in human readable way.

    def print_next_pass(pass_data: dict): This prints any of the passes retrieved by get_next_passes
    in a human readable format.
"""

import requests
from datetime import datetime
from requests.exceptions import RequestException

def get_next_passes(location: dict):
    """ this function receives a latitude and longitude in the form of a
    dictionary, retrieves and formats the number of future passes the
    international space station would make

    Args:
        dict: this contains the latitude and longitude of a particular location in the world

    Raise:
        RequestException: this captures a broad list of http error including 404, 401, 500, etc
        ConnectionError: any failed error from no internet access or inabilitu for request.get not getting
        to the server.

    Return:
        list: it returns a list of dictionaries which would contain the rise_time, direction, duration,
        and max_elevation of the latitude and longitude that was passed as argument into the function
    
    Example:


    """

    lat_titude, lon_gitude = location["lat"], location["lon"]
    try:
        response = requests.get(f"https://iss-api.polluxlabs.io/iss-pass?lat={lat_titude}&lon={lon_gitude}")
 
        #checks response status and catches raises exceptions for unssuccessful Http Errors
        #like 404, 401, 500 etc
        response.raise_for_status()
    except RequestException as e:
        print(f"{e} kindly enter a valid location")
        return

    data = response.json()
    passes = data["passes"]
    cleaned_pass = []
    for index in passes:
        string_time = index["rise"]["time"]
        utc_time = datetime.fromisoformat(string_time)
        useful_data = {
            "rise_time": utc_time,
            "direction": index["rise"]["compass"],
            "duration": index["duration_sec"],
            "max_elevation": index["culmination"]["elevation_deg"]
        }
        cleaned_pass.append(useful_data)
    return cleaned_pass

if __name__ == "__main__":
    get_next_passes({"lat": 4.8242, "lon": 7.0336})
