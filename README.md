  # Dependencies:

  $ pip install geoip2

  # On Raspbian (I used):
  $ pip install python-geoip2

  # And:

  $ pip install geolite2

  # On Raspbian (I used):
  $ pip install python-geoilite2

===========================================================================================

# IP_Locator
A simple program written in Python that enables the user to enter an Ipv4 IP address and track it's location to City, Country and also return Longitude&amp;Latitude values. You will need the GeoIP module, and I have included the Database file for this program to access the required information about the IP (2017 database). 

If you want to obtain an IP to try this out, open a command terminal (DOS, CMD, BASH etc) and enter:
  $ host www.AnyWebsiteName.com

NOTE The database is a free version and is pretty accurate, but may need updating each year at least to allow for any changes made. 

I tested this database with a few websites (of known location and address), then entered the Longitude and Latitude values into this website to obtain a map location: https://www.latlong.net/. I managed to track worldwide within (on average) 1 square mile. If you purchase a geolocation database service you may get even more accurate results, and may also get the required annual location updates included (it is only as accurate as the database)

===========================================================================================

NOTE: I was unable to upload my database file for this program due to the size being over 25mb. Please obtain your own copy of the database here for free:
https://dev.maxmind.com/geoip/geoip2/geolite2/

And you will need to edit the filepath/filename.mmdb in the program where #commented. If you place the .py program and the .mmdb database file in the same directory, you will only need to state the filename.mmdb

Although it is named as a Country lookup,  I found good results with the City database and therefore added that version to my code. Feel free to try whatever works best for you.

PLANS: This is a very crude version written to get a basic understanding of GeoIP2 within Python. I plan to make the whole thing neater, and more efficient, and maybe write it into a Tkinter GUI for User friendliness.

Please feel free to send me any comments or ideas, and please feel free to make any changes and improvements
