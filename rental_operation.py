from land import Land
from file_operation import save_land_data

def display_lands(lands):
    print("\nAvailable Lands:")
    for index, land in lands.items():
        print(f"Index: {index} | {land}")

def rent_land(lands, customer_name, filename):
    total_price = 0
    rented_land = []

    while True:
        display_lands(lands)
        
        all_rented = True
        for land in lands.values():
            if land.availability.lower() != "not available":
                all_rented = False
                break

        if all_rented:
            print("All lands are currently rented.")
            break

        try:
            index = int(input("Enter the index of the land you want to rent or '0' to exit: "))
            if index == 0:
                break
            if index not in lands:
                print("Invalid index!")
                continue
            if lands[index].availability.lower() == "not available":
                print("The land is not available to rent.")
                continue

            months = int(input("Enter the number of months you want to rent the land: "))
            total_price += lands[index].price * months
            lands[index].availability = "Not Available"
            rented_land.append(lands[index])

            if input("Do you want to rent another land? (y/n): ").lower() != 'y':
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if rented_land:
        save_land_data(filename, lands)
        generate_bill(customer_name, rented_land, total_price, "Rented")

def return_land(lands, customer_name, filename):
    total_price = 0
    returned_land = []

    while True:
        display_lands(lands)

        all_retruned = True
        for land in lands.values():
            if land.availability.lower() != "available":
                all_retruned = False
                break

        if all_retruned:
            print("You havent rented any lands form us!.")
            break

        try:
            index = int(input("Enter the index of the land you want to return or '0' to exit: "))
            if index == 0:
                break
            if index not in lands:
                print("Invalid index!")
                continue
            if lands[index].availability.lower() == "available":
                print("The land was not rented from us.")
                continue

            months_rented = int(input("Enter the number of months you rented the land: "))
            return_month = int(input("Enter the return month: "))

            if return_month >= months_rented:
                total_price += lands[index].price * months_rented
            else:
                total_price += lands[index].price * months_rented + 0.2 * lands[index].price
                print("You have incurred a late fee of 20% of the price.")

            lands[index].availability = "Available"
            returned_land.append(lands[index])

            if input("Do you want to return another land? (y/n): ").lower() != 'y':
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if returned_land:
        save_land_data(filename, lands)
        generate_bill(customer_name, returned_land, total_price, "Returned")

def generate_bill(customer_name, lands, total_price, action):
    bill_filename = f"{customer_name}_{action}_Land_Bill.txt"
    with open(bill_filename, "w", encoding="utf-8") as file:
        file.write(f"Customer Name: {customer_name}\n")
        file.write(f"Action: {action}\n")
        file.write("══════════════════════════════════════════════════════════\n")
        file.write(f"{'Kitta Number':<15} {'City/District':<20} {'Direction':<15} {'Area':<10} {'Price':<15}\n")
        file.write("══════════════════════════════════════════════════════════\n")
        for land in lands:
            file.write(f"{land.kitta_number:<15} {land.city_district:<20} {land.direction:<15} {land.area:<10} {land.price:<15}\n")
        file.write("══════════════════════════════════════════════════════════\n")
        file.write(f"Total Price: {total_price}\n")
