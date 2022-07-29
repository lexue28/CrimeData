import pandas as pd
import pprint
county = pd.read_csv("https://raw.githubusercontent.com/shadowdragon2805/CrimeData/main/docs/csv/crime_data_w_population_and_crime_rate.csv")
city = pd.read_csv("https://raw.githubusercontent.com/shadowdragon2805/CrimeData/main/docs/csv/uscities.csv")
#for county to city
#print(county.shape)
#see how many rows and columns
#print(county.to_string())
#prints out entire database, test by selecting random county
def findC(name):#finds county info corresponding to name
  countyfind = county[county['county_name'].str.contains(name, regex=False)]
  return countyfind
def cityFind(county, state):#finds cities by inputting county
  cityCon = city[city['county_name'].str.contains(county, regex = False)]#find all counties with inputted name
  temp = cityCon[cityCon['state_id'].str.contains(state, regex = False)]#include only counties in specified state, should only be one
  return temp

enter = input("Input County (full name including suffix) & State: ")
countyfind = findC(enter)

r, c =  countyfind.shape
if r > 1: #if there is more than one county with that name, must input state, if not then pass
  print("Pulling up all results matching",enter, ", Please specify abbreviated state of county")
  #print(countyfind.to_string) - prints all of the counties with that name
  state = input("State of county: ")
  name = enter+", "+state
  countyfind = findC(name)
print(countyfind.to_string)#countyfind should only be one county now

#necessary to make stats more legible
headers = list(countyfind.columns.values)#list of the column names
print(headers)

crimelist = countyfind.values.tolist()#list of column values
print(crimelist)

print(crimelist[0][headers.index("county_name")])#the name

crimedict = {   'Name of County':crimelist[0][headers.index("county_name")],
                'Crime Data Year':2016,
                'Population':crimelist[0][headers.index("population")],
                'Crime Rate per 100000':crimelist[0][headers.index("crime_rate_per_100000")],
                'Crimes Recorded':crimelist[0][headers.index("CPOPCRIM")],
                'Arrests':crimelist[0][headers.index("CPOPARST")],
                'Murder':crimelist[0][headers.index("MURDER")],
                'Rape':crimelist[0][headers.index("RAPE")],
                'Assault':crimelist[0][headers.index("AGASSLT")],
                'Theft/Larceny(no force, no breaking into property)':int(crimelist[0][headers.index("MVTHEFT")])+int(crimelist[0][headers.index("LARCENY")]),
                'Burglary(breaking into property)':crimelist[0][headers.index("BURGLRY")],
                'Robbery(violent crime, force)':crimelist[0][headers.index("ROBBERY")],
                'Arson':crimelist[0][headers.index("ARSON")]

             }
print(crimedict) #dictionary for format

pprint.pprint(crimedict)#printing dictionary with new line with pprint

#this block of code finds the corresponding cities to the county
temp = str(crimelist[0][headers.index("county_name")])
index = temp.find("County")
index = int(index)
cOnly = temp[0:index-1]
state = temp[len(temp)-2 : len(temp)]
cityStr = cityFind(cOnly, state)
citiesIn = list(cityStr["city"])
print(temp, "is in", citiesIn)

def average(countyfind):#returns array to see if the stats are above or below avg
  popM = county["population"].mean()
  cRate100M = county["crime_rate_per_100000"].mean()
  recM = county["CPOPCRIM"].mean()
  arrM = county["CPOPARST"].mean()
  murM = county["MURDER"].mean()
  rapeM = county["RAPE"].mean()
  assM = county["AGASSLT"].mean()
  tlM = county["MVTHEFT"].mean() + county["LARCENY"].mean()#combine means of theft/larceny df[["Fee","Discount"]].mean()
  burM = county["BURGLRY"].mean()
  robM = county["ROBBERY"].mean()
  arsM = county["ARSON"].mean()
  #returns true if the specific county has higher stats than the average
  above = [countyfind["population"]>popM, countyfind["crime_rate_per_100000"]>cRate100M, countyfind["CPOPCRIM"]>recM, countyfind["CPOPARST"]>arrM, countyfind["MURDER"]>murM, countyfind["RAPE"]>rapeM, countyfind["AGASSLT"]>assM, countyfind["MVTHEFT"]+ countyfind["LARCENY"]>tlM, countyfind["BURGLRY"] >burM, countyfind["ROBBERY"]>robM, countyfind["ARSON"]>arsM]

  return above

#if the specific county has more stats than average

above = average(countyfind)#calls to find avg

dictlist = list(crimedict) #convert so you can access the keys

for i in range(2, len(above)):#takes out name and year bc unecessary, than displays if above or below avg in clean manner
  if above[i].bool() == True:
    print(enter, "has more", dictlist[i], "than average")
  else:
    print(enter, "has less", dictlist[i], "than average")
    
