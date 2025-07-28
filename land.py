class Land:
    def __init__(self, kitta_number, city_district, direction, area, price, availability):
        self.kitta_number = kitta_number
        self.city_district = city_district
        self.direction = direction
        self.area = area
        self.price = price
        self.availability = availability

    def __str__(self):
        return f"{self.kitta_number}, {self.city_district}, {self.direction}, {self.area}, {self.price}, {self.availability}"

def parse_land_record(record):
    parts = record.split(", ")
    return Land(parts[1], parts[2], parts[3], parts[4], int(parts[5]), parts[6])
