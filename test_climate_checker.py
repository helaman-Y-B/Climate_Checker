# Imports some functions from climate_checker
from climate_checker import date_time, get_page, get_details_of_page
import pytest

# Gets the URL
URL = 'https://weather.com/weather/tenday/l/829942c703678b8d95048d77f0af52bf207d59c08af1a40f95e55630226ccdfd'


# test get_page
def test_get_page():
    assert get_page(URL)


# test get_details_of_page
def test_get_details_of_page():
    get_details_of_page(get_page(URL))


# test date_time
def test_date_time():
    date_time()


# Begin the test code
if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", "test_climate_checker.py"])
