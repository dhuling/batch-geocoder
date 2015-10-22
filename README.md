# batch-geocoder
This is a batch geocoder for turning addresses into latitude and longitude using the geopy geocoding library. It demonstrates how it can be used to take a csv of addresses and convert them into lat-long points that can be displayed on a map. 

Takes a csv of addresses, in full format form e.g. 1234 Fake Street, Seattle Wa, 98109. An example is provided in the repo. Because it leverages Google's geocoder, partial addresses are still geocoded, so a response will be recieved regardless of match-strength. Therefore please follow garbage in, garbage out principles, and make sure your addresses are full. As a side note, google's geocoder also will geocode POIs, so if all you have is "Harborview Hospital Seattle", it will likely geocode correctly.

Google allows 2500 maps api requests per day. If the script runs too quickly, it will deny the request. If the script has more than 2500 addresses, the 2501st will be denied. This script pauses 2 seconds between requests. It also tracks exact duplicates

OSMs geocoder is arguably less accurate, but I have not done any kind of comparison. 


