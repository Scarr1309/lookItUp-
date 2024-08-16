from newsapi import NewsApiClient
import pycountry

newsapi = NewsApiClient(api_key = 'f3bc8e93e84446508cea5b89fcbc4395')

input_country = input("Country: ")
input_countries = [f'{input_country.strip}']
countries = {}

for country in pycountry.countries:
    countries[country.name] = country.alpha_2

codes = [countries.get(country.title(),'Unknown code') for country in input_countries]



