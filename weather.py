import requests
from datetime import datetime
# import pytz

def main():
    location = input("Enter the location: ")
    api_key = "f52bc419b3b1ba185bf570b5f4351466"

    x = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric")
    if x.status_code == 200:
        print(x.json())
        data = x.json()

        print(f"latitude: {data['coord']['lat']}, longitude: {data['coord']['lon']}" )

        weather_dic = data.get('weather')
        con = weather_dic[0]['description']
        print(f"Condition: {con}")

        print(f"Temp: {int(data['main']['temp'])} 'C")
        print(f"Min Temp: {int(data['main']['temp_min'])} 'C, Max Temp: {int(data['main']['temp_max'])} 'C")
        print(f"Humidity: {data['main']['humidity']}%")

        mtomiles = round((data.get('visibility')*0.000621371),2)
        print(f"Visibility: {mtomiles}mi")

        # print(f"Sunrise: {data['sys']['sunrise']}, Sunset: {data['sys']['sunset']}")
    else:
        print("Error:", x.status_code)



if __name__ == "__main__":
    main()