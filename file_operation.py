from land import parse_land_record

def load_land_data(filename):
    lands = {}
    try:
        with open(filename, "r") as file:
            for index, line in enumerate(file, start=1):
                land = parse_land_record(line.strip())
                lands[index] = land
    except FileNotFoundError:
        print("File not found. A new file will be created.")
    except Exception as e:
        print("An error occurred:", e)
    return lands

def save_land_data(filename, lands):
    with open(filename, "w") as file:
        for index, land in lands.items():
            file.write(f"{index}, {land.kitta_number}, {land.city_district}, {land.direction}, {land.area}, {land.price}, {land.availability}\n")
