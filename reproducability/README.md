# Reproducability
## Assignment 1 : Machine Learning & Data Mining -- SOFE4620U
### Malek Mustapha-Abdullah 100541476

## Background
For the first assignment of the course, we were given the task of finding an online collection of data, then storing it in a databse or file in order to make the data usable.
I chose to use an API provided by the Toronto Police which contains data on accident-related Killed or Severily Injured persons between 2006 - 2016.
This data could be used to predict and prevent future accidents.

## The KSI API
This dataset includes all traffic collisions events where a person was either Killed or Seriously Injured (KSI) from 2006 – 2016. Database includes a record for every person involved in the collisions regardless of Injury Level. 
The query URL for the API is:
- https://services.arcgis.com/S9th0jAJ7bqgIRjw/arcgis/rest/services/KSI/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json
> The data contains useful information such as lighting and weather conditions, intersections, vehicle type, among other things.
More information can be found here:
- http://data.torontopolice.on.ca/datasets/ksi

## Recovering the Data
In order to recover the data on your local computer, follow these steps:
- Clone the repository
- Create a new virtual environment
```
pip install virtualenv
virtualenv venv
```
- Start the virtual environment
`source venv/bin/activate`
- Download the requirements
`pip install -r requirements.txt`
- Run the code
`python retrieve_data.py`

After following the above steps, you shall see a new folder `ksi_data.csv` which will contain the data in a CSV format.
