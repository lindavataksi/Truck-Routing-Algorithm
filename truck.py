class Truck(object):
    def __init__(self, speed, miles, packages, currentLocation, departTime):
        self.speed = speed
        self.miles = miles
        self.packages = packages
        self.currentLocation = currentLocation
        self.departTime = departTime

    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.speed, self.miles, self.packages, self.currentLocation, self.departTime)
