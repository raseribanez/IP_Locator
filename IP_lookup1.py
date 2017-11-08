# Author:      Ben Woodfield
# Description: IP Lookup

import geoip2.database

# Country
def country_lookup():
    users_ip_address = raw_input("Enter the ip address : ")
    
    # Enter YOUR filepath/filename.mmdb below - the database file was too large to upload to github 
    reader = geoip2.database.Reader('GeoLite2-City.mmdb')
    
    #response = reader.city('209.85.202.94')
    response = reader.city(users_ip_address)
    print("Ben Woodfield - IP Lookup - COUNTRY & CITY DETAILS")
    print("================================================================================")
    print(response)
    print("================================================================================")
    print(response.country.iso_code)
    print("================================================================================")
    print(response.country.name)
    print("================================================================================")
    print(response.country.names)
    print("================================================================================")
    print(response.subdivisions.most_specific.name)
    print("================================================================================")
#   print(response.subdivisions.most_specific.iso_code)
    print("================================================================================")
    print("================================================================================")
    print("Latitude :", response.location.latitude)
    print("Longitude :", response.location.longitude)
    print("================================================================================")
    print(response.city.name)
    print(response.postal.code)
    reader.close()

country_lookup()
    
