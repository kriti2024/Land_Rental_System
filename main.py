from file_operation import load_land_data
from rental_operation import rent_land, return_land

def main():
    filename = "rental_land.txt"
    lands = load_land_data(filename)

    while True:
        print('''
        ╔══════════════════════════════════════════════════════════╗
        ║                                                          ║
        ║           Welcome to the Land Rental Management System   ║
        ║                                                          ║
        ║   1. View All Lands                                      ║
        ║   2. Rent Land                                           ║
        ║   3. Return Land                                         ║
        ║   4. Exit                                                ║
        ║                                                          ║
        ╚══════════════════════════════════════════════════════════╝
        ''')
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            for index, land in lands.items():
                print(f"Index: {index} | {land}")
        elif choice == '2':
            customer_name = input("Enter your full name: ")
            if customer_name:
                rent_land(lands, customer_name, filename)
            else:
                print("Name cannot be empty!")
        elif choice == '3':
            customer_name = input("Enter your full name: ")
            if customer_name:
                return_land(lands, customer_name, filename)
            else:
                print("Name cannot be empty!")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
