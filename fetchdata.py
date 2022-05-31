#import
import csv
import numpy as np
import pandas as pd

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
    return area_dict

global areadictionary
areadictionary = getAreaDictionary() #areadictioary from zipcodecsv. {zip int, city str}

####################################
#Get something from csv, given something
####################################
def getCityGivenZip(zipcode, areadictionary): #returns city str given ZIP int
    return areadictionary[zipcode]

def getZipGivenCity(city, dct): #returns zip int given city str
    dct = reverseDictionary(dct)
    return dct[city]

####################################
#utility quality of life functions
####################################
def reverseDictionary(dct): #simple reverse dictionary function
    dct = {v: k for k, v in dct.items()}
    return dct

####################################
#Test execute functions gonna delete later
####################################
print (getCityGivenZip(99926, areadictionary))
print (getZipGivenCity("Metlakatla", areadictionary))
