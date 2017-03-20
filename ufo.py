import re
import numpy as np
import pandas as pd

# UFO Sightings (scrubbed)
# https://www.kaggle.com/NUFORC/ufo-sightings

# Disasters Data Set (look only at natural disasters from 1909 to 2013)
# https://www.fema.gov/openfema-dataset-disaster-declarations-summaries-v1

# Earthquakes
# http://earthquake.usgs.gov/fdsnws/event/1/#parameters


########################################################################################

ufo_path = '~/Desktop/STA 141B/141B-Final-Project/ufo-sightings/scrubbed.csv'

# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
ufos = pd.read_csv(ufo_path, header=0,

                   names=['date_seen', 'city', 'state', 'country', 'shape', 'duration_sec',
                          'duration_mh', 'comments', 'date_posted', 'lat', 'long'],

                   parse_dates=['date_posted'], infer_datetime_format=True)

# check the data types
print ufos.info()

# change duration in seconds and latitude to numeric
ufos[['duration_sec', 'lat']] = ufos[['duration_sec', 'lat']].apply(pd.to_numeric)

# from the result we see that we need to set values to 3 rows of this instance
print ufos[ufos['duration_sec'].str.contains('`', na=False)]

ufos = ufos.set_value(27822, 'duration_sec', '2')
ufos = ufos.set_value(35692, 'duration_sec', '8')
ufos = ufos.set_value(58591, 'duration_sec', '0.5')


# try again
ufos[['duration_sec', 'lat']] = ufos[['duration_sec', 'lat']].apply(pd.to_numeric)


# we again see that lat has a letter in one of the positions we'll check to
# see how many there are
print ufos[ufos['lat'].str.contains('[a-zA-Z]', na=False)]

ufos = ufos.set_value(43782, 'lat', '33.200088')

# change duration in seconds and latitude to numeric
ufos[['duration_sec', 'lat']] = ufos[['duration_sec', 'lat']].apply(pd.to_numeric)


# upper case words as necessary
ufos['city'] = ufos['city'].str.title()
ufos['state'] = ufos['state'] .str.upper()
ufos['country'] = ufos['country'].str.upper()


# now change the date_seen col to a date_time
ufos['date_seen'] = pd.to_datetime(ufos['date_seen'], errors='coerce')

# set the row indices as the the date_seen
ufos = ufos.set_index('date_seen')



# select sightings in US
ufos = ufos.loc[ufos['country'] == 'US']



# What days of the week were most UFOs seen?

# How quickly does a UFO sighting get posted relative it to being seen?

# What are the top 10 places in CA where most UFOs are seen?

# Is there a difference between the UFO shapes seen in the different regions of the US?

#












#########################################################################################
# https://stackoverflow.com/questions/15891038/pandas-change-data-type-of-columns
# https://stackoverflow.com/questions/14745022/pandas-dataframe-how-do-i-split-a-column-into-two
# https://stackoverflow.com/questions/13411544/delete-column-from-pandas-dataframe
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html

# [l.split(' ') for l in ufos['datetime']]

# ufos = pd.read_csv(file_path, parse_dates=True, index_col='datetime')

# usecols=[0, 1, 2, 3, 4, 5, 6, 8, 9, 10],
# dtype={'date_seen': np.object, 'city': np.object, 'state': np.object,
#        'country': np.object, 'shape': np.object, 'duration_sec': np.object,
#        'duration_mh': np.object, 'date_posted': np.object, 'lat': np.o,
#        'long': np.float64},
#########################################################################################