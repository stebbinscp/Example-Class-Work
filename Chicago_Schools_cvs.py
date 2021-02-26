from math import asin, sin, cos, sqrt, radians, degrees
import csv
from webbrowser import open_new_tab
EARTH_RADIUS = 3961

class School:
    def __init__(self, data):
        self.id = data.get("School_ID")
        self.name = data.get("Short_Name")
        self.network = data.get("Network")
        self.address = data.get("Address")
        self.zip = data.get("Zip")
        self.phone = data.get("Phone")
        self.grades = data.get("Grades").split(", ")
        self.location = Coordinate(data.get("Lat"), data.get("Long"))
        return

    def open_website(self):
        """Take in the School object and open the url with the specified school ID."""
        url = "http://schoolinfo.cps.edu/schoolprofile/SchoolDetails.aspx?SchoolId="
        open_new_tab(url+self.id)
    
    def distance(self,coordinate):
        """Take the distance between the School object and another's coordinate."""
        coord_lat = radians(coordinate.lat)
        coord_long = radians(coordinate.long)
        lat = radians(self.location.lat)
        longi = radians(self.location.long)
        distance = 2*EARTH_RADIUS*asin( sqrt( sin( ( coord_lat-lat)/2)**2 + \
            cos(longi)*cos(coord_long)*sin((coord_long-longi)/2)**2))
        return distance

    def full_address(self):
        """Returns the full address of the School object"""
        address = self.address + "\nChicago" + "\nIllinois" + f"\n{self.zip}"
        return address

class Coordinate:
    def __init__(self, latitude, longitude):
        self.lat = float(latitude)
        self.long = float(longitude)
        self.lat_long = self.as_degrees()
        return

    def distance(self, coordinate):
        """Function employs the as_degrees function to convert the coordinates given 
        from degrees to radians in order to employ the Haversine formula to calculate
        and return the distance between two schools"""
        distance = 2*EARTH_RADIUS*asin( sqrt( sin( ( coordinate.lat_long[0]-self.lat_long[0])/2)**2 + \
            cos(self.lat_long[0])*cos(coordinate.lat_long[0])*sin((coordinate.lat_long[1]-self.lat_long[1])/2)**2))
        return distance

    def as_degrees(self):
        """Employs the math radians function to return a tuple of radian (lat,long)"""
        latitude = radians(self.lat)
        longitude = radians(self.long)
        return (latitude, longitude)

    def show_map(self):
        url = "http://maps.google.com/maps?q="
        open_new_tab(url+str(self.lat)+","+str(self.long))

class CPS:
    def __init__(self, filename):
        school_dictionaries = []
        schools = []

        with open(filename, newline='\n') as f:
            reader = csv.DictReader(f)
            # # for i in range()
            for row in reader: 
                school_dictionaries.append(row)
                # each row is a dictionary with the school's info
        for item in school_dictionaries:
            schools.append(School(item))
        # print(schools[1].location.lat)
        self.schools = schools

    def nearby_schools(self, coordinate, radius=1.0):
        """Function returns a list of school instances within the radius
        of the given instance coordinate. The coordinate must
        be of the class Coordinate"""
        result = []
        for school in self.schools:
            if school.location.distance(coordinate) <= 1.0:
                result.append(school)
        return result

    def get_schools_by_grade(self, *grades):
        """Function returns a list of school instances which offer all
        the grades listed in the grades argument. Grades must be strings."""
        result = []
        grades_wanted = list(grades)
        for school in self.schools:
            if all(item in grades for item in grades_wanted) == True:
                result.append(school)
        return result

    def get_schools_by_networks(self, network):
        """Function returns a list of school instances which are within the listed
        network. Network must be a string"""
        result = []
        for school in self.schools:
            network = school.network
            if network == network:
                result.append(school) # doesn't append the school name
        return result


if __name__ == "__main__":
    obj = CPS("schools.csv")