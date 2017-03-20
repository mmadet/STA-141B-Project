<div align = 'right'>
Nicholas Alonzo - 998455301 <br>
Ethan Bell - <br>
Hanxiaoxin Wang - 913459751 <br>
Madeline Ye - 998108849 <br>
</div>

# UFO Sightings & Natural Disasters: A Coincidence?

In this analysis, we'll be looking at two data sets, UFO sightings in the United States and declated natural disasters from the years 1965 to 2013. We'll first be exploring the data sets indivdually before investigating whether sightings overlap with disaters. The UFO sightings data was scraped from the [National UFO Reporting Center Database](http://www.nuforc.org/webreports.html) and uploaded to [Kaggle](https://www.kaggle.com/NUFORC/ufo-sightings) for download. The download came with 2 files (complete and scrubbed); We'll be working with the scrubbed version with complete reports. The disasters data was downloaded from the [Federal Emergency Management Agency (FEMA)](https://www.fema.gov/openfema-dataset-disaster-declarations-summaries-v1) and has full documenation.

## Data Description:

UFO Sightings (ufos\_complete.csv) <br>
__date seen__: date/timestamp of UFO seen <br>
__date posted__: date/timestamp posted on the NUFORC page <br>
__shape__: shape of UFO reported <br>
__duration min__: how many minutes the UFO was seen <br>
__comments__: brief comments from person who reported incident <br>
__city raw__: city sighting fell under from orignal Kaggle download <br>
__city__: city sighting fell under from reverse geocoding latitude/longitude <br>
__county__: county the city is in from FIPS download <br>
__county fip__: unique FIPS code for each county by state from FIPS download (matches to disasters) <br>
__zip code__: zip code of city from reverse geocoding latitude/longitude <br>
__state__: US state sighting occured in <br>
__state abbr__: US state abbreviation sighting occured in <br>
__division name__: division US state is in, taken from https://statetable.com/ <br>
__region name__: region US State is in, taken from State Download <br>
__latitude__: latitude of sighting <br>
__longitude__: longitude of sighting <br>

Disasters Declaration (disasters.csv) <br>
__date started__: date the diaster itself began <br>
__date ended__: date the disaster itself ended <br>
__declaration type__: type of disaster that was declared <br>
__disaster type__: type of disaster <br>
__disaster title__: title/phrase for the disaster <br>
__days lasted__: days after the disaster occured (date ended - date started) <br>
__county__: county the city is in from FIPS download <br>
__county fip__: unique FIPS code for each county by state from FIPS download (matches to UFOs) <br>
__state__: US state disaster occured in <br>
__state abbr__: US state abbreviation disaster occured in <br>
__division name__: division US state is, taken from State Download <br>
__region name__: region US State is in, taken from State Download <br>
__latitude__: latitude of county affected by disaster from geocoding county and state <br>
__longitude__: longitude of county affected by disaster from geocoding county and state <br>

## Pre-Processing Summary

NOTE: Full pre-processing steps are in PreProcessUFO\_nick.ipynb and PreProcessDisaster\_nick.ipynb <br>
The following was done to match data sets by state regions, divisions, or counties. <br>

__UFO Sightings__
- Reverse geocoded latitude and longitude to get zip code using Google's Geocoding API
- Used zip code to match in zip code database and get county names
- Used county names to match county names and FIPS from FIPS download
- Added state region and division attributes

__Disasters Declaration__
- Geocoded county and state to get latitude and longitude using Google's Geocoding API
- Used county names to match county names and FIPS from FIPS download
- Added state region and division attributes

__Downloaded Resource List__
- [Google's Geocoding API via Python Package](https://github.com/DenisCarriere/geocoder): Latitude/longitude & zip code
- [Zip Code Database Download](https://www.unitedstateszipcodes.org/zip-code-database/): County
- [FIPS Download](https://www.census.gov/geo/reference/codes/cou.html): County names and FIPS
- [State Download](https://statetable.com/): State region and division attributes


## Goal:

For each question include your findings, what you think the result means, how might the question relate to the other/both data sets, and if you think there's anything left to explore from it. <br>

__UFO Sightings__
- How quickly does a UFO sighting get posted relative to it being seen? (M)
    - Show with a time series plot
- What are the top 5 states with most UFO sightings? (M)
    - Show a map of all sightings by state using color intensity
    - What are the top 5 UFO shapes seen in these states?
- During what month(s) are most UFO sightings seen? (M)
    - Show with a time series plot
    - Of those month(s) with most UFO sightings what are the top 3 regions reporting those sightings?
- Is there a difference between UFO shapes seen in the different regions of the US? (M)
    - Use subplots for regions with horizontal barplots of the UFO shape counts in descending order

__Disasters Declaration__
- What are the top 5 states with most declared disasters? (Z)
    - Show a map of all disasters affecting counties using color intensity
    - What are the top 3 disasters that affected these states?
- During what month(s) are disasters declared most? (Z)
    - Show with a time series plot
    - Of those month(s) with most disasters declared what top 3 regions were affected?
- What's the top 5 divisions with most declared disasters (Z)
    - Use subplots for divisons with horizontal barplots of types of disaster counts in descending order

__UFO Sightings & Disasters__
- Show a bubble map of all sightings and disasters (Z)
- Show a time series of average count of UFO sightings and count of disasters by month (Z)
- What top county has been affected most by disasters (E)
    - What kinds of UFO shapes have been reported there? Show with a descending horizontal barplot
- What county has the most reported UFO sightings (E)
    - What are the types of disasters that happen there? Show with a descending horizontal barplot
- Choose the state with the longest declared disaster on a given month/year (E)
    - What counties were affected?
    - Match all the counties in the UFO sightings to those of in the disasters
    - Are there any reported sightings that fall between that month/year?
    - If so, how many sightings were reported and what types of UFO shapes were seen?
- What is the top UFO sighting that was reported by multiple people on a given day? (E)
    - What county was it in?
    - What kind of disasters happen in that county?
    - What shape of UFOs are being seen in that county 5 years before after that incident? Show with a time series plot
