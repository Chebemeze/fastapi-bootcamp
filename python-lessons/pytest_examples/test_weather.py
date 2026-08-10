from weather import get_weather
from unittest.mock import Mock, patch


def test_weather():
    """ verifies if the weather api request will return the right weather information.
    it does so by temporary bypassing the requests.get() online call which would have been
    made by using patch(). patch() enables us to bypass a function when testing a the call.

    I replicated the behaviour of the requests.get() method by using a Mock() class.
    mock_response.json is a child object of the mock_response,
    mock_response.json.return_value specifies the value that will be returned (in this case a dictionary) when
    mock_response.json() is called like a function. the .return_value is a special way
    objects created from Mock() declares what will be returned when they are called like a function.
    """
    with patch("weather.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"temperature": 31, "condition": "Sunny"}
        mock_get.return_value = mock_response
    
        result = get_weather("Lagos")

        assert result == {
            "city": "Lagos",
            "temperature": 31,
            "condition": "Sunny"
        }
