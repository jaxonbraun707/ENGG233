class Location:
    def __init__(self, loc_name, x, y):
        self.loc_name = loc_name
        self.x = x
        self.y = y

    def calculate_distance(self, other):
        distance = pow(pow((self.x - other.x), 2) + pow((self.y - other.y), 2), 0.5)
        return distance

    def to_string(self):
        return ("Name: " + self.loc_name + ", x-coordinate = " + str(self.x) + ", y-coordinate = " + str(self.y))

class HospitalList:
    def __init__(self):
        self.hospital_list = []

    def print_hospital_at(self, i):
        if i > len(self.hospital_list):
            print("Hospital is not within range")
            return
        else:
            print(self.hospital_list[i].to_string())

    def add_new_hospital(self, loction_new_hospital):
        self.hospital_list.append(loction_new_hospital)

    def get_hospital_at(self, i):
        if i > len(self.hospital_list):
            print("Hospital is not within range")
            pass
        else:
            return(self.hospital_list[i].to_string())

    def to_string(self):
        print(Location.to_string(self.hospital_list[0]), end = "\n")
        print(Location.to_string(self.hospital_list[1]), end = "\n")
        return" "



def find_closest_hospital(x, y):
    distance1 = Location.calculate_distance(x.hospital_list[0], y)
    distance2 = Location.calculate_distance(x.hospital_list[1], y)
    if distance1 < distance2:
        return x.hospital_list[0]
    elif distance2 < distance1:
        return x.hospital_list[1]
    else:
        return (-1)
   
def get_location():
    name = input("Enter the location name of hospital: ")
    x = int(input("Enter x-coordinate of hospital: "))
    y = int(input("Enter y-coordinate of hospital: "))
    location = Location(name, x, y)
    return location

def main():
    hospital_list = HospitalList()
    for _ in range(0, 2):
        location = get_location()
        hospital_list.add_new_hospital(location)

    print(hospital_list.to_string())

    location_accident = Location("A", -12628, 7535)
    print(Location.to_string(location_accident))

    closest_location = find_closest_hospital(hospital_list, location_accident)
    print("The closest hospital to the accident point is: ", closest_location.to_string())


if __name__ == "__main__":
    main()

