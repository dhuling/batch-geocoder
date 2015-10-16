# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:37:27 2015

@author: Derek Huling
"""
#importing geopy
from geopy.geocoders import GoogleV3, Nominatim
import csv, time

#Geocode file is simply a list of addresses in CSV format.
my_address_list = "add_list.csv" #path to input csv

output = "output.csv" #path to output file
#empty containers we'll use later for comparing list items
add_list = [] #empty address list
rand_list = []

#creating a list of addresses we want to geocode from a CSV file
with open(my_address_list, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        add_list.append(row[0])
print add_list
add_list.sort()
print add_list
#match is used to check if we've already geocoded the address
match = []
add = 0
lat = 0
longitude = 0

#This is the file we are writing to
with open(output, 'wb') as cs_out:
    writer = csv.writer(cs_out, delimiter=',')
    for i in add_list:
        #if the current address matches the previous one, we use the same
        #geocoding info so we don't spam the API needlessly
        print "previous address: {0}".format(add)
        print "current address: {0}".format(i)
        if add == i:
            print "Matched"
            writer.writerow([add, lat, longitude])
            
        else:
            try:
                #first we'll try google's api, but if they reject our request
                #then it will throw an exception, and the "except" statement
                #below will catch it and change our geocoder to the OSM one
                geolocator = GoogleV3()
                location = geolocator.geocode(i)
                writer.writerow([i, location.latitude, location.longitude])
                print "using Google Geocoder"
                print "{2}: Latitude = {0}, longitude = {1}".format(location.latitude, location.longitude, location.address)
            except:
                geolocator = Nominatim()
                location = geolocator.geocode(i)
                writer.writerow([i, location.latitude, location.longitude])
                print "Using OSM"
                print "{2}: Latitude = {0}, longitude = {1}".format(location.latitude, location.longitude, location.address)
            #We include a finally statement because no matter which geocoder we
                #use we want to sleep for 5 seconds to not spam the API, and we
                #need to write our locations to the disc, in this case a CSV
            finally: 
                time.sleep(2)
                add = i
                lat = location.latitude
                longitude = location.longitude
          
