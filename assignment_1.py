import json

# ---------- Part 1 -------------

with open("stations.csv") as file:
    stations = file.read()


with open ("precipitation.json") as file:
    precip = json.load(file)

seattle_measures = []

monthly_rain = [0] * 12

# select for station and month
for measurement in precip:
    if measurement["station"] == "GHCND:US1WAKG0038":
        date = measurement["date"].strip().split("-")
        monthly_rain[int(date[1])-1] += measurement["value"]
        # [1] accesses the month value

with open('monthly_rain_seattle.json', 'w') as file:
    json.dump(monthly_rain, file)








# ------------ BLOOPERS ------------------

# my beautiful attempt at doing monthly totals without usnig split()
# spoiler: i couldn't get it to work and also wasted an hour trying to make it work 
# when Dorian reminded me that split() does in fact exist
# seattle_measures was a variable which contained a list of dictionarys for all measurements in Seattle

#m=1 # for january to september
#d=1 
#n=0 # for october to december

#for measurement in seattle_measures:
#    while d<32 and f"-0{m}-0{d}" in measurement["date"]:
#        monthly_tot+=(measurement["value"])
#        print(monthly_tot)
#        d=d+1
#    while n<4 and f"-1{n}-" in measurement["date"]:
#        monthly_tot+=(measurement["value"])
#        print(monthly_tot)





