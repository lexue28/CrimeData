#import
import csv
import numpy as np
import pandas as pd

####################################
#utility quality of life functions
####################################
def invertDictionary(dct): #simple invert dictionary function, returns inverted dictionary
    dct = {v: k for k, v in dct.items()}
    return dct

def checkIfKey(key, dct): #Checks if a key is in a dictionary, returns True/False
    if key in dct:
        return True
    else:
        return False

####################################
#CSV FILE DIRECTORY NAMES
####################################
global crimepopulationcsv
global reportcsv
global zipcodecsv
crimepopulationcsv = "docs/csv/crime_data_w_population_and_crime_rate.csv"
reportcsv = "docs/csv/report.csv"
zipcodecsv = "docs/csv/zip_code_database.csv"

####################################
#CSV into dictionaries
####################################
def getAreaDictionary(): #turns zipcodecsv into a dictionary with ZIP CODE int, CITY str
    column_list = ["zip","type","decommissioned","primary_city","acceptable_cities","unacceptable_cities","state","county","timezone","area_codes","world_region","country","latitude","longitude","irs_estimated_population"]
    df = pd.read_csv(zipcodecsv, usecols=column_list)
    x = 0
    area_dict = dict(zip(df["zip"], df["primary_city"]))
    area_dict = invertDictionary(area_dict)
    #print(area_dict)
    area_dict =  {k.lower(): v for k, v in area_dict.items()} #NOTE: ALL CITIES IN THIS LIST ARE LOWERCASE STRINGS
    area_dict = invertDictionary(area_dict)
    return area_dict

global areadictionary
areadictionary = getAreaDictionary() #areadictioary from zipcodecsv. {zip int, city str}
inverseareadictionary = invertDictionary(areadictionary)

####################################
#Get something from csv, given something
####################################
def getCityGivenZip(zipcode, areadictionary): #returns city str given ZIP int
    check = checkIfKey(zipcode, areadictionary)
    if check == True:
        return areadictionary[zipcode]
    else:
        print("Error - zip not found. Did you spell it correctly?")
        return False

def getZipGivenCity(city, dct): #returns zip int given city str
    city = city.lower()
    check = checkIfKey(city, invertDictionary(dct))
    dct = invertDictionary(dct)
    if check == True:
        return dct[city]
    else:
        print("Error - city not found. Did you spell it correctly?")
        return False

####################################
#Test execute functions gonna delete later
####################################
#print (getCityGivenZip(99926, areadictionary)) #ignore these comments
#print (getZipGivenCity("MetLakatla", areadictionary)) #ignore these comments
