# IP_Locator
A simple program written in Python that enables the user to enter an Ipv4 IP address and track it's location to City, Country and also return Longitude&amp;Latitude values. You will need the GeoIP module, and I have included the Database file for this program to access the required information about the IP (2017 database). 

NOTE The database is a free version and is pretty accurate, but may need updating each year at least to allow for any changes made. 

I tested this database with a few websites (of known location and address), then entered the Longitude and Latitude values into this website to obtain a map location: https://www.latlong.net/. I managed to track worldwide within (on average) 1 square mile. If you purchase a geolocation database service you may get even more accurate results, and may also get the required annual location updates included (it is only as accurate as the database)
