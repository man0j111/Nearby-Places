The file (FINAL_get_locations) is used to get places based on it's coordinates and keyword for which the places are to be fetched and store them in a csv file.
Another file (unique.py) by giving the output csv as an input confirms that there is no reptition of places fetched.


API - Google Maps API

Note: Since there is a limitation of only 20 places that can fetched per iteration using this API there may be a chance of getting duplicate values, so that's the reason why 
we use unique.py to check the repetitions.
