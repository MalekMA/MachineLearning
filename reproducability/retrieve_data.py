#
# This program fetches accident-related Killed or Seriously Injured (KSI) data from the Toronto Police API via an HTTP URL GET request
# After the JSON data is retrieved, the data is stored into a .csv file
#
# Done by Malek Mustapha-Abdullah 100541476
# January 28, 2018
# SOFE4620U Machine Learning and Data Mining
#

import json
import requests

# This function checks if the data from an attribute is 'null' or not and then converts the data to a string
def check_if_not_null(x, attr):
    if json_data["features"][x]["attributes"][attr] == None:
        return "False"
    else:
        return str(json_data["features"][x]["attributes"][attr])

url = 'https://services.arcgis.com/S9th0jAJ7bqgIRjw/arcgis/rest/services/KSI/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'
response = requests.get(url)
print response
json_data = json.loads(response.text)

file = open("ksi_data.csv", "a")
file.write("YEAR,DATE,TIME,Hour,STREET1,STREET2,OFFSET,ROAD_CLASS,District,"
            +"LATITUDE,LONGITUDE,LOCCOORD,ACCLOC,TRAFFCTL,VISIBILITY,LIGHT,"
            +"RDSFCOND,ACCLASS,IMPACTYPE,INVTYPE,INVAGE,INJURY,FATAL_NO,INITDIR,"
            +"VEHTYPE,MANOEUVER,DRIVACT,DRIVCOND,PEDTYPE,PEDACT,PEDCOND,CYCLISTYPE,"
            +"CYCACT,CYCCOND,PEDESTRIAN,CYCLIST,AUTOMOBILE,MOTORCYCLE,TRUCK,TRSN_CITY_VEH,"
            +"EMERG_VEH,PASSENGER,SPEEDING,AG_DRIV,REDLIGHT,ALCOHOL,DISABILITY,Division,"
            +"Ward_Name,Hood_Name\n")

output = ""
size = len(json_data["features"])
for x in range(0, size-1):
     output = check_if_not_null(x,"YEAR") + ","+check_if_not_null(x,"DATE") + ","+check_if_not_null(x,"TIME") + ","+check_if_not_null(x,"Hour") + ","+check_if_not_null(x,"STREET1") + ","+check_if_not_null(x,"STREET2") + ","+check_if_not_null(x,"OFFSET") + ","+check_if_not_null(x,"ROAD_CLASS") + ","+check_if_not_null(x,"District") + ","+check_if_not_null(x,"LATITUDE") + ","+check_if_not_null(x,"LONGITUDE") + ","+check_if_not_null(x,"LOCCOORD") + ","+check_if_not_null(x,"ACCLOC") + ","+check_if_not_null(x,"TRAFFCTL") + ","+check_if_not_null(x,"VISIBILITY") + ","+check_if_not_null(x,"LIGHT") + ","+check_if_not_null(x,"RDSFCOND") + ","+check_if_not_null(x,"ACCLASS") + ","+check_if_not_null(x,"IMPACTYPE") + ","+check_if_not_null(x,"INVTYPE") + ","+check_if_not_null(x,"INVAGE") + ","+check_if_not_null(x,"INJURY") + ","+check_if_not_null(x,"FATAL_NO") + ","+check_if_not_null(x,"INITDIR") + ","+check_if_not_null(x,"VEHTYPE") + ","+check_if_not_null(x,"MANOEUVER") + ","+check_if_not_null(x,"DRIVACT") + ","+check_if_not_null(x,"DRIVCOND") + ","+check_if_not_null(x,"PEDTYPE") + ","+check_if_not_null(x,"PEDACT") + ","+check_if_not_null(x,"PEDCOND") + ","+check_if_not_null(x,"CYCLISTYPE") + ","+check_if_not_null(x,"CYCACT") + ","+check_if_not_null(x,"CYCCOND") + ","+check_if_not_null(x,"PEDESTRIAN") + ","+check_if_not_null(x,"CYCLIST") + ","+check_if_not_null(x,"AUTOMOBILE") + ","+check_if_not_null(x,"MOTORCYCLE") + ","+check_if_not_null(x,"TRUCK") + ","+check_if_not_null(x,"TRSN_CITY_VEH") + ","+check_if_not_null(x,"EMERG_VEH") + ","+check_if_not_null(x,"PASSENGER") + ","+check_if_not_null(x,"SPEEDING") + ","+check_if_not_null(x,"AG_DRIV") + ","+check_if_not_null(x,"REDLIGHT") + ","+check_if_not_null(x,"ALCOHOL") + ","+check_if_not_null(x,"DISABILITY") + ","+check_if_not_null(x,"Division") + ","+check_if_not_null(x,"Ward_Name") + ","+check_if_not_null(x,"Hood_Name")+"\n"
     file.write(output)
     
print "'ksi_data.csv' file created"
