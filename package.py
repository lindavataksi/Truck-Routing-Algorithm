class Package(object):
    # ID,STREET,CITY,STATE,ZIP,DEADLINE,WEIGHT,NOTES
    def __init__(self, ID, street, city, state, zip, deadline, weight, notes, status, departureTime=None, deliveryTime=None):
        self.ID = ID
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.departureTime = departureTime
        self.deliveryTime = deliveryTime

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.street, self.city, self.state, self.zip, self.deadline, self.weight, self.notes, self.status, self.departureTime, self.deliveryTime)

    def package_status(self, user_time):
        if self.deliveryTime < user_time:
            self.status = "Delivered"
        elif self.departureTime > user_time:
            self.status = "In Transit"
        else:
            self.status = "At Hub"
