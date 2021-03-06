

class Street(object):
    def __init__(self, from_int, to_int, name, length):
        self.from_int = from_int
        self.to_int = to_int
        self.name = name
        self.length = length

    def String(self):
        print("street", self.name, self.from_int, self.to_int, self.length)

class Car(object):
    def __init__(self, id, route):
        self.id = id
        self.route = route

    def String(self):
        print("car", self.route)

class StopLight(object):
    def __init__(self, s_intersection, s_street, s_cars):
        self.s_intersection = s_intersection
        self.s_street = s_street
        self.s_cars = s_cars

    def add_car(self, car):
        self.s_cars.append(car)

    def String(self):
        print("intersection", self.s_intersection, "street", self.s_street, "cars", self.s_cars)

class Schedule(object):
    def __init__(self):




class Intersection(object):
    def __init__(self, name):
        self.name = name
        self.to_street = []
        self.from_street = []

    def add_to(self,street):
        self.to_street.append(street)

    def add_from(self,street):
        self.from_street.append(street)

    def String(self):
        print("intersection", self.name, "from:", self.from_street, "to", self.to_street)

def read_from_file(file):
    f = open(file, "r")
    time, intersection_len, streets_len, cars_len, score = f.readline().split()
    streets = []
    cars = []

    for _ in range(int(streets_len)):
        from_int, to_int, name, length = f.readline().split()
        streets.append(Street(int(from_int), int(to_int), name, int(length)))

    for id in range(int(cars_len)):
        _, route = f.readline().split(maxsplit=1)
        cars.append(Car(id, route.split()))
    intersections = []
    for i in range(int(intersection_len)):
        intersections.append(Intersection(i))
    for street in streets:
        intersections[street.from_int].add_from(street.name)
        intersections[street.to_int].add_to(street.name)



    return (streets, cars, intersections, score)



streets, cars, intersections, score = read_from_file("a.txt")

for street in streets:
    street.String()
for car in cars:
    car.String()
for intersection in intersections:
    intersection.String()


def write_solution():