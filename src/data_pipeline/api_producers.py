# Scripts to fetch from APIs and send to Kafka
import requests

from newsapi import NewsApiClient

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

## AMAZON Product detail Example
def fetch_amazon_product_details():
    

    url = "https://real-time-amazon-data.p.rapidapi.com/product-details"

    querystring = {"asin":"B07ZPKBL9V","country":"US"}

    headers = {
        "x-rapidapi-key": "91ebf5d894mshd420be8da16386ap104b89jsn1b54e3f6792c",
        "x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

## TWITTER API Example
def fetch_twitter_data():
    url = "https://twitter241.p.rapidapi.com/community-tweets"

    querystring = {"communityId":"1601841656147345410","searchType":"Default","rankingMode":"Relevance","count":"20"}

    headers = {
        "x-rapidapi-key": "91ebf5d894mshd420be8da16386ap104b89jsn1b54e3f6792c",
        "x-rapidapi-host": "twitter241.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())


## NEWS API Example

def fetch_news():
    # Init
    newsapi = NewsApiClient(api_key='17fb79df80c04604969590cd6f78ff9b')

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                            sources='bbc-news,the-verge',
                                            category='business',
                                            language='en',
                                            country='us')

    # /v2/everything
    all_articles = newsapi.get_everything(q='bitcoin',
                                        sources='bbc-news,the-verge',
                                        domains='bbc.co.uk,techcrunch.com',
                                        from_param='2017-12-01',
                                        to='2017-12-12',
                                        language='en',
                                        sort_by='relevancy',
                                        page=2)

    # /v2/top-headlines/sources
    sources = newsapi.get_sources()

## Weather API Example
def fetch_weather_data():
    owm = OWM('your free OWM API key')
    mgr = owm.weather_manager()


    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place('London,GB')
    w = observation.weather

    w.detailed_status         # 'clouds'
    w.wind()                  # {'speed': 4.6, 'deg': 330}
    w.humidity                # 87
    w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    w.rain                    # {}
    w.heat_index              # None
    w.clouds                  # 75

    # Will it be clear tomorrow at this time in Milan (Italy) ?
    forecast = mgr.forecast_at_place('Milan,IT', 'daily')
    answer = forecast.will_be_clear_at(timestamps.tomorrow())

    # ---------- PAID API KEY example ---------------------

    config_dict = config.get_default_config_for_subscription_type('professional')
    owm = OWM('your paid OWM API key', config_dict)

    # What's the current humidity in Berlin (Germany) ?
    one_call_object = mgr.one_call(lat=52.5244, lon=13.4105)
    one_call_object.current.humidity