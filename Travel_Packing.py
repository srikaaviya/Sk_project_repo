import requests
import os

def checklist(min_temp, rain):

    dress_cold = """1. A base layer of wool or synthetic thermals
    2. An insulating layer like fleece or down
    3. A waterproof and windproof jacket as your outer layer
    4. Boots, wool socks, gloves and scarf"""

    dress_hot = """1. Cotton or linen fabrics. 
    2. Normal slippers or shoes
    3. Hat/Umbrella, sunglasses and sun protection. """

    dress_warm = """1. Sweaters and cardigan
    2. A waterproof and windproof jacket as your outer layer
    3. Shoes, socks"""

    rain_clothes = """1. An umbrella/ waterproof jacket.
    2. Waterproof shoes and socks"""

    file_name = "checklist.txt"
    with open(file_name, "w") as file:
        file.write("Your List: \n")

    with open(file_name, "a") as file:
        if min_temp <= 15:
            file.write(dress_cold + "\n")
        if 16 <= min_temp <= 25 and rain>0:
            file.write(dress_warm + '\n')
            file.write(rain_clothes + "\n")
        if 16 <= min_temp <= 25 and rain==0:
            file.write(dress_warm + "\n")
        if min_temp > 25:
            file.write(dress_hot + "\n")

    try:
        os.system(f"open {file_name}")
    except Exception as e:
        print("An error occurred while trying to open the file:", e)

def main():
    location = input("Enter Destination: ")
    duration = input("How many days? ")
    print(f"Weather at {location}: ")
    api_key = 'f52bc419b3b1ba185bf570b5f4351466'

    w = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric")
    forecast = requests.get(f" https://api.openweathermap.org/data/2.5/forecast?q={location}&cnt={duration}&appid={api_key}&units=metric")

    min_temp=0
    rain=0

    if w.status_code == 200:
        # print(w.json())
        data = w.json()

        weather_dic = data.get('weather')
        con = weather_dic[0]['description']
        print(f"Condition: {con}")

        temp= int(data['main']['temp'])
        min_temp = int(data['main']['temp_min'])
        max_temp = int(data['main']['temp_max'])
        print(f"Temp: {temp} 'C")
        print(f"Min Temp: {min_temp} 'C, Max Temp: {max_temp} 'C")
        print(f"Humidity: {data['main']['humidity']}%")
    else:
        print("No weather report found. Please specify correct location")
        exit()

    if forecast.status_code == 200:
        # print(forecast.json())
        fdata = forecast.json()

        for f in fdata['list']:
            rain+=1
            pop = f.get("pop", 0)
            pop_value = pop * 100
            if pop_value > 50:
                print(f"There is {pop_value}% chances of Rain on {rain}th day")

    print("\n")

    chk = input("Do you need a checklist (yes/no): ")
    if chk == "yes":
        checklist(min_temp, rain)
    else:
        exit()

if __name__ == "__main__":
    main()