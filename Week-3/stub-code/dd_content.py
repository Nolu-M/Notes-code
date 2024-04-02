import csv
import random
from urllib import request
import json
import datetime

# Retrieve a random quote from the specified CSV file.
quotes_file = 'quotes.csv'

def get_random_quote():
    try: # load motivational quotes from csv
        with open(quotes_file) as csvfile:
            quotes = [{'author': line[0],
                       'quote': line[1]} for line in csv.reader(csvfile, delimiter='|')]
    
    except Exception as e: # use a default quote to help thins turn out for the best
        quotes = [{'author': 'Eric Idle',
                   'quote': 'Always look on the Bright Side of Life.'}]
        
    return random.choice(quotes)

# Retrieve the current weather forecast from OpenWeatherMap.

def get_weather_forecast(coords={'lat': 28.4717, 'lon': -80.5378}): # default location at Cape Canaveral, FL
    try: # retrieve forecast for specified coordinates.
        api_key = '3ac045cf6a1ddebf2eb35d86e32b5955' # my API key
        url = f'https://api.openweathermap.org/data/3.0/onecall?lat={coords["lat"]}&lon={coords["lon"]}&appid={api_key}'
        data = json.load(request.urlopen(url))

        return data
    
    except Exception as e:
        print(f"Error: {e}. Using default location.")
        # Use default location
        default_coords = {'lat': 28.4717, 'lon': -80.5378}
        default_url = f'https://api.openweathermap.org/data/3.0/onecall?lat={default_coords["lat"]}&lon={default_coords["lon"]}&appid={api_key}'
        default_data = json.load(request.urlopen(default_url))

        return default_data
    
 

def get_twitter_trends():
    pass

def get_wikipedia_article():
    pass

if __name__ == '__main__':
    ##### test get_random_quote() #####
    print('\nTesting quote generation...')

    quote = get_random_quote()
    print(f' - Random quote is "{quote["quote"]}" - {quote["author"]}')

    quote = get_random_quote(quotes_file = None)
    print(f' - Default quote is "{quote["quote"]}" - {quote["author"]}')

    print(get_weather_forecast())