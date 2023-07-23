import pandas as pd
print(pd.__version__)

#load in bike data
bikes = pd.read_csv(r'DunderData\ReferenceFiles\bikes.csv')
#return first 3 rows
print(bikes.head(3))

#Filtering
filt = bikes['tripduration'] > 5000
print(bikes[filt].head(3))

filt1 = bikes['tripduration'] > 5000
filt2 = bikes['gender'] == 'Female'
#returns tripduratioin >5k AND when female
filtA = filt1 & filt2
print(bikes[filtA].head(3))
#returns tripuduration >5k OR when female
filtB = filt1 | filt2
print(bikes[filtB].head(3))

print(bikes.query('tripduration > 5000').head(3))
print(bikes.query('tripduration > 5000 and gender =="Female"').head(3))
print(bikes.query('tripduration > 5000 or gender=="Female"').head(3))