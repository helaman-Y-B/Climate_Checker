# Climate_Checker
A web scraping program, made with python, which get weather information from a city in Brazil

This code gets information from the following website: https://weather.com/weather/tenday/l/829942c703678b8d95048d77f0af52bf207d59c08af1a40f95e55630226ccdfd
The code was made for a assigment at BYU-Idaho CSE 111 course, which they asked us(The students) to create our own program, and my choice was a web scraping program.

The program uses 3 libraries in total: datetime, requests and beautifulsoup4
And in total has 6 functions named: main(), get_page(URL), get_details_of_page(soup), removing_string(lists), get_celcius(fahrenheit) and date_time().

I also made a test program with a library named pytest

OBS: The web site might change in the future, which it will make necessary to change all information related to HTML adn URL in the code.
