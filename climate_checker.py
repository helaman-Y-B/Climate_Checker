# Firts I imported datetime, requests and BeutifulSoup.
import datetime
import requests
from bs4 import BeautifulSoup


def main():
    """Function main(), calls two functions, which is 'get_page' and 'get_details_of_page'.
    get_page takes one paramenter, which is the URL from the website, and the it's stored
    into a varible called soup, which is used as a parameter from get_details_of_page."""

    # URL is the website which the program will get weather information
    # This URL gets the weather from a city in Brazil
    URL = 'https://weather.com/weather/tenday/l/829942c703678b8d95048d77f0af52bf207d59c08af1a40f95e55630226ccdfd'
    soup = get_page(URL)
    get_details_of_page(soup)


def get_page(URL):
    """This function gets the permission from the URL
    Then it prints the permission
    and then it parse the HTML from the URL, it also return soup."""

    # Send a request
    permission = requests.get(URL)

    # Print the answer
    print(permission)
    print()

    # Parse the web page
    soup = BeautifulSoup(permission.text, 'html.parser')

    # Return the parsed information
    return soup


def get_details_of_page(soup):
    """The function 'get_details_of_page' takes one parameter called soup.
    Here we separate the the information that I want from the soup and
    then, the code store the information inside a list.
    After, this function calls another 3 functions, one called removing_string, another called get_celsius
    and one called date_time.
    After, it prints the information."""

    # Search for the correct informations
    titles = soup.findAll(
        'h2', attrs={'class': 'DetailsSummary--daypartName--2FBp2'})

    max_temp = soup.findAll(
        'span', attrs={'class': 'DetailsSummary--highTempValue--3Oteu'})

    min_temp = soup.findAll(
        'span', attrs={'class': 'DetailsSummary--lowTempValue--3H-7I'})

    weather_data = soup.findAll(
        'span', attrs={'class': 'DetailsSummary--extendedData--365A_'})

    wind_data = soup.findAll(
        'span',
        attrs={'class': 'Wind--windWrapper--3aqXJ DailyContent--value--37sk2'})

    # Store the information into the correct list
    title = [title.get_text() for title in titles if title]
    max_tempe = [max_tempe.get_text() for max_tempe in max_temp if max_tempe]
    min_tempe = [min_tempe.get_text() for min_tempe in min_temp if min_tempe]
    weather = [weather.get_text() for weather in weather_data if weather]
    wind = [wind.get_text() for wind in wind_data if wind]

    def removing_string(lists):
        """The removing_string gets 1 parameter called lists, which are the lists
        that has the information from the website.
        The main purpouse of this function is to convert the numbers that are
        a string, to a integer.
        It also remove the "--" sign that appears everyday in a
        specific time."""

        # Lists to store the modified data
        new_number_list = []
        integer_list = []

        # Substitute the "--" sign, to 0
        for num in lists:
            if num == "--":

                integer_list.append(0)
                pass

            # Remove the "°" sign and then store a clean number
            elif num != "--":

                result = num.replace("°", "")
                new_number_list.append(result)

        # Makes every number from new_number_list become a integer
        for integer in new_number_list:

            convertion = int(integer)
            integer_list.append(convertion)

        # Return the integer list
        return integer_list

    def get_celsius(fahrenheit):
        """get_celsius gets one parameter called fahrenheit, which is a list of numbers
        that were get from the function called removing_string.
        This function converts the fahrenheit list to a celsius list."""

        # The list when the Celcius will be stored
        celcius_list = []

        # Get each fahrenheit value from a list
        for fahren in fahrenheit:

            # If fahrenheit 0, that means it didn't had any value before
            if fahren == 0:

                # If fahrenheit didn't have a value, then celcius just become 0
                celcius_list.append(0)
                pass

            elif fahren != 0:

                # convert fahrenheit into celcius
                celcius = (fahren - 32) * 5.0 / 9.0
                celcius_list.append(celcius)

        # Return the celcius list
        return celcius_list

    # call the functions to get the celcius values
    max_numbers = removing_string(max_tempe)
    max_celcius = get_celsius(max_numbers)
    min_numbers = removing_string(min_tempe)
    min_celcius = get_celsius(min_numbers)

    for i in range(len(titles)):

        # Print the informations of a 10 days.
        print(
            f"Date--> {title[i]}\n\tMax temperature: {max_celcius[i]:.0f} C°\n\tMin temperature: {min_celcius[i]:.0f} C°\n\tWeather condition: {weather[i]}\n\tWind direction and velocity: {wind[i]}\n"
        )

    # Calls date_time function
    date_time()


def date_time():
    """This function takes no parameters,
    and it gets the date and time
    from the user computer"""

    # Get all the current date and time information
    now = datetime.datetime.now()
    year = '{:02d}'.format(now.year)
    month = '{:02d}'.format(now.month)
    day = '{:02d}'.format(now.day)
    hour = '{:02d}'.format(now.hour)
    minute = '{:02d}'.format(now.minute)

    # Prints the current date and time
    print(f'This program was used at: {day}/{month}/{year} at {hour}:{minute}')


# Calls the function main, which begins the program
if __name__ == "__main__":
    main()
