# C950- Data Structures and Algorithms 2- Western Governers University
# Linda Vataksi
# STUDENT ID = 011273373
# 02/ 25/ 2024

import csv
import datetime
from hashTable import ChainingHashTable
from package import Package
from truck import Truck

# open and read the provided distance table file
with open('./CSV/distance.csv') as csvfile1:
    distanceCSV = csv.reader(csvfile1)
    distanceCSV = list(distanceCSV)

# open and read the provided package table file
with open('./CSV/package.csv') as csvfile2:
    packageCSV = csv.reader(csvfile2)
    packageCSV = list(packageCSV)

# open and read the address table file
with open('./CSV/address.csv') as csvfile3:
    addressCSV = csv.reader(csvfile3)
    addressCSV = list(addressCSV)

# Creating loadPackageData() to read packages from packagesCSV file and insert into defined hash function

# OVERALL: Time complexity is O(N) and space complexity is O(M)


def loadPackageData(filename):
    # Opening file= time and space complexity of O(1)
    with open(filename) as packagess:
        packageInfo = csv.reader(packagess, delimiter=',')
        next(packageInfo)
        # Space complexity- O(M) and time complexity O(N)
        for package in packageInfo:
            # Space complexity- O(1) and time complexity O(1)
            pID = int(package[0])
            pStreet = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pNotes = package[7]
            pStatus = "At the Hub"
            pDepartureTime = None
            pDeliveryTime = None

            # Inserting Package info into the hash
            # Time and space complexity of O(1)
            p = Package(pID, pStreet, pCity, pState, pZip, pDeadline,
                        pWeight, pStatus, pDepartureTime, pDeliveryTime)
            packageHashTable.insert(pID, p)


# Hash table for the packages
packageHashTable = ChainingHashTable()

# Load package data into the hash table
loadPackageData('./CSV/package.csv')

# function to return an address based off address.csv file

# Time complexity- O(N) and and space complexity - O(1)


def address(address):
    # checks each row in address file
    # for loop has time complexity of O(N), while within the time complexity is O(1)
    for row in addressCSV:
        # if there is a string present in the third row item, return the first row item
        if address in row[2]:
            return int(row[0])

# function to return the distance between two addresses.

# Time and space complexity is O(1)


def distanceBetween(address1, address2):
    try:
        # Time complexity- O(1)
        distanceBtwn = distanceCSV[address1][address2]
        # if empty, flip the addresses
        # Time complexity- O(1)
        if distanceBtwn == '':
            distanceBtwn = distanceCSV[address2][address1]
        return float(distanceBtwn)
    except ValueError:
        # Handle the case where distance cannot be converted to float
        return None
    except IndexError:
        # Handle the case where addresses are out of range
        return None


# initiate three truck objects using the given assumptions:
# -Each truck can carry a maximum of 16 packages
# -The trucks travel at an average speed of 18 miles per hour
# manually load the trucks and assign departure times

truck1 = Truck(18, 0, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34,
               37, 40], "4001 South 700 East", datetime.timedelta(hours=8))
truck2 = Truck(18, 0, [6, 3, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], "4001 South 700 East",
               datetime.timedelta(hours=10, minutes=20))
truck3 = Truck(18, 0, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], "4001 South 700 East",
               datetime.timedelta(hours=9, minutes=5))

# Time complexity- O(N^2) and space complexity of O(M)


def truckDeliverPackages(truck):
    # initialize an empty array for in transit packages
    # space complexity- O(M)
    inTransit = []
    # Time complexity- O(N)
    for packageID in truck.packages:
        package = packageHashTable.search(packageID)
        if package is not None:  # Check if package is found
            # add all packages from hash table to the in transit array
            inTransit.append(package)
    # clear packages from truck hash, since they are now in transit
    truck.packages.clear()
    # entire while loop= time complexity of O(N^2)
    while inTransit:
        # arbitrary value greater than distance_to_package
        nextStop = float('inf')
        next_package = None
        # for loop- time complexity O(N)
        for package in inTransit:
            distance_to_package = distanceBetween(
                address(package.street), address(truck.currentLocation))
            # if distance to package  is less, that will determine the next stop for delivery
            if distance_to_package < nextStop:
                nextStop = distance_to_package
                next_package = package

        # append
        truck.packages.append(next_package.ID)
        # remove from inTransit array
        inTransit.remove(next_package)
        truck.miles += nextStop
        truck.currentLocation = next_package.street
        truck.departTime += datetime.timedelta(hours=nextStop / 18)
        next_package.deliveryTime = truck.departTime
        next_package.departureTime = truck.departTime

    return truck.miles


# Tallies the total distance travelled by each truck, as well as the total of all three trucks
total_distance_truck1 = truckDeliverPackages(truck1)
total_distance_truck2 = truckDeliverPackages(truck2)
total_distance_truck3 = truckDeliverPackages(truck3)
total = total_distance_truck1 + total_distance_truck2 + total_distance_truck3

print("Western Governer's University: WGUPS ROUTING PROGRAM IMPLEMENTATION")
print("Total distance traveled by the Trucks:", total, "miles")

# Part D- UI
# Overall time complexity is O(N)
# Space complexity is O(1)

user_input_time = input(
    "Please enter a time to check status of all the packages. Use the provided format, HH:MM:SS ")
(h, m, s) = user_input_time.split(":")

user_time = datetime.timedelta(
    hours=int(h), minutes=int(m), seconds=int(s))

# The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m.
# WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the
# correct address (410 S. State St., Salt Lake City, UT 84111) until 10:20 a.m.
specific_package = packageHashTable.search(9)
if specific_package.ID == 9 and user_time >= datetime.timedelta(hours=10, minutes=20):
    specific_package.street = "410 S. State St.,"
    specific_package.city = "Salt Lake City"
    specific_package.state = "UT"
    specific_package.zip = " 84111"

package_truck_mapping = {}
for pckgeID in range(1, 41):
    pckge = packageHashTable.search(pckgeID)
    if pckge.ID in [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]:
        truckNum = "1"
    elif pckge.ID in [6, 3, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39]:
        truckNum = "2"
    elif pckge.ID in [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33]:
        truckNum = "3"
    package_truck_mapping[pckgeID] = truckNum

# range includes package with id 40
for packageID in range(1, 41):
    package = packageHashTable.search(packageID)
    truckNum = package_truck_mapping[packageID]
    if package.deliveryTime is not None and user_time < package.deliveryTime:
        # print(f"Package {package.ID}: In Transit as of {
        #       package.deliveryTime}")
        print(f"Package {package.ID} on Truck {truckNum}: Delivery To: {package.street}, {package.city}, {package.state}, {package.zip}, Deadline: {package.deadline}, Status: In Transit, Delivery Time: {
            package.deliveryTime}")
    elif package.deliveryTime is not None and user_time > package.deliveryTime:
        print(f"Package {package.ID} on Truck {truckNum}: Delivery To: {package.street}, {package.city}, {package.state}, {package.zip}, Deadline: {package.deadline}, Status: Delivered, Delivery Time: {
            package.deliveryTime}")
    else:
        print(f"Package {package.ID} on Truck {truckNum}: Delivery To: {package.street}, {package.city}, {package.state}, {package.zip}, Deadline: {package.deadline}, Status: At the Hub, Delivery Time:{
            package.deliveryTime}")
