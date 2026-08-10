import requests

""" retrieves city, temperature and condition of any city
Example:
    >>> import get_weather
    >>> owere = get_weather("oweri")
    >>> print(owere["city"])
    owere
"""

def get_weather(city: str):
    """
    Args:
        str: name of a geographic location to get the intended weather condition from
    
    Raises:
        ConnectionError: when the api is unable to get the desired weather data

    Return:
        dictionary: the name, temperature, and weatherr condition of the desired city
    
    Example:
        >>> import get_weather
        >>> owere = get_weather("imo")
        >>> print(owere[imo])
        imo

        >>> import get_weather
        >>> sahara_desert = get_weather("sahara_desert")
        >>> print(sahara_desert["city"])
        ConnectionError
    """
    response = requests.get(f"https://api.weather.com/{city}")
    if response.status_code != 200:
        raise ConnectionError("Weather API Failed")
    data = response.json()
    return {
        "city": data["city"],
        "temperature": data["temperature"],
        "condition": data["condition"]
    }
