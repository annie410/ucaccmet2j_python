import json

choice = input("Which city would you like to study? Press 1 for Seattle, 2 for Cincinnati, 3 for Maui and 4 for San Diego ")

# --------------------- SEATTLE ----------------------------

if  choice == "1":
    station_code = "GHCND:US1WAKG0038"

    city = "seattle"

    with open("stations.csv") as file:
        stations = file.read()


    with open ("precipitation.json") as file:
        precip = json.load(file)

    monthly_rain = [0] * 12

    for measurement in precip:

        # picks the correct station
        if measurement["station"] == station_code:

            # splits the dates to [dd, mm, yyyy] by splitting on the - 
            date = measurement["date"].strip().split("-")

            # add all the values from one month together
            monthly_rain[int(date[1])-1] += measurement["value"]
            # [1] accesses the month value
            # -1 bc python indexes from 0

    # saving the monthly rain totals to their own json file
    with open(f'monthly_rain_{city}.json', 'w') as file:
        json.dump(monthly_rain, file)

    # ----------- Part 2 ---------------------

    # calculating total year rainfall
    rain_year = sum(monthly_rain)

    # empty relative rain variable
    relative_rain = []

    # adding the relative rain for each month to the empty list
    for month_rain in monthly_rain:
        relative_rain.append((month_rain/rain_year)*100)

    # saving the relative rain for each month to their own file
    with open(f'relative_rain_{city}.json', 'w') as file:
        json.dump(relative_rain, file)

# --------------------- CINCINNATI -------------------------

elif choice == "2":
    station_code = "GHCND:USW00093814"

    city = "cincinnati"

    with open("stations.csv") as file:
        stations = file.read()

    with open ("precipitation.json") as file:
        precip = json.load(file)

    monthly_rain = [0] * 12

    for measurement in precip:
        if measurement["station"] == station_code:
            date = measurement["date"].strip().split("-")
            monthly_rain[int(date[1])-1] += measurement["value"]

    with open(f'monthly_rain_{city}.json', 'w') as file:
        json.dump(monthly_rain, file)

    rain_year = sum(monthly_rain)

    relative_rain = []

    for month_rain in monthly_rain:
        relative_rain.append((month_rain/rain_year)*100)

    with open(f'relative_rain_{city}.json', 'w') as file:
        json.dump(relative_rain, file)

# ------------------------ MAUI ----------------------------

elif choice == "3":
    station_code = "GHCND:USC00513317"

    city = "maui"

    with open("stations.csv") as file:
        stations = file.read()

    with open ("precipitation.json") as file:
        precip = json.load(file)

    monthly_rain = [0] * 12

    for measurement in precip:

        if measurement["station"] == station_code: 
            date = measurement["date"].strip().split("-")
            monthly_rain[int(date[1])-1] += measurement["value"]

    with open(f'monthly_rain_{city}.json', 'w') as file:
        json.dump(monthly_rain, file)

    rain_year = sum(monthly_rain)

    relative_rain = []

    for month_rain in monthly_rain:
        relative_rain.append((month_rain/rain_year)*100)

    with open(f'relative_rain_{city}.json', 'w') as file:
        json.dump(relative_rain, file)

# --------------------- SAN DIEGO --------------------------

elif choice == "4":
    station_code = "GHCND:US1CASD0032"

    city = "san_diego"

    with open("stations.csv") as file:
        stations = file.read()

    with open ("precipitation.json") as file:
        precip = json.load(file)

    monthly_rain = [0] * 12

    for measurement in precip:
        if measurement["station"] == station_code:
            date = measurement["date"].strip().split("-")
            monthly_rain[int(date[1])-1] += measurement["value"]

    with open(f'monthly_rain_{city}.json', 'w') as file:
        json.dump(monthly_rain, file)

    rain_year = sum(monthly_rain)

    relative_rain = []

    for month_rain in monthly_rain:
        relative_rain.append((month_rain/rain_year)*100)

    with open(f'relative_rain_{city}.json', 'w') as file:
        json.dump(relative_rain, file)

else:
    print("I'm sorry, I don't quite understand what you mean")












