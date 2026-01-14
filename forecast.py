import requests

def main():
    location = input("Enter Location: ")
    api_key = "f52bc419b3b1ba185bf570b5f4351466"

    result = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q="
                          f"{location}&appid={api_key}&units=metric")
    if result.status_code == 200:
        data = result.json()
        min_temp, max_temp = 0, 0
        for items in data['list']:
            date = items['dt_txt']
            temp = int(items['main']['temp'])
            min_temp +=  int(items['main']['temp_min'])
            max_temp += int(items['main']['temp_max'])

        print(f"min: {(min_temp//40)}'C , max: {(max_temp//40)} 'C")
    else:
        print("Error:", result.status_code)

if __name__ == "__main__":
    main()