import requests
import json
name = input("What is your name? ")
print(f"Hello, {name}!")
byear = input("Enter your Birth Year")  # prompts you to enter your birth year
results = 2018 - int(byear)  # subtract the current year to your birth year
print("you are", results, "years old")  # print the result
api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
city = input("What city do you live in?")
apikey = ""
url = api_endpoint + "?q=" + city + "&appid=" + apikey + "&units=imperial"
print(url)
response =requests.get(url)
parseResponse = response.json()
print(parseResponse)
temperature = parseResponse['main']['temp']
weather = parseResponse['weather'][0]['description']
print(temperature)
print(weather)
