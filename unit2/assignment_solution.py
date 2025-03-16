# Import necessary modules for optional file handling
import json

# Predefined dataset of parcels
parcel = {
    "parcel_1": {
        "location": "NYARUTARAMA",
        "type": "urban",
        "size": 300,
        "master_plan": "Agriculture",
        "price": "1500000"
    },
    "parcel_2": {
        "location": "Rwamagana",
        "type": "rural",
        "size": 400,
        "master_plan": "Residential",
        "price": "2500000"
    },
    "parcel_3": {
        "location": "Huye",
        "type": "urban",
        "size": 500,
        "master_plan": "Residential",
        "price": "3500000"
    }
}

# Display the main menu to the user
def display_menu():
    print("\nPlease select one of the options below:")
    print("1. Check/search for an entry")
    print("2. Update an entry")
    print("3. Add a new entry")
    print("4. Delete an existing entry")
    print("5. View all records")  # New option to view all records
    print("6. Exit")

# Search for a specific parcel in the dataset
def search_parcel(parcel_dict):
    parcel_id = input("Enter the parcel ID to search for (e.g., parcel_1): ")
    if parcel_id in parcel_dict:
        print(f"Details for {parcel_id}: {parcel_dict[parcel_id]}")
    else:
        print("Parcel not found.")

# Update an existing parcel entry
def update_parcel(parcel_dict):
    parcel_id = input("Enter the parcel ID to update: ")
    if parcel_id in parcel_dict:
        field = input("Which field would you like to update? (location, type, size, master_plan, price): ")
        if field in parcel_dict[parcel_id]:
            new_value = input(f"Enter new value for {field}: ")
            parcel_dict[parcel_id][field] = new_value
            print(f"{field} updated successfully.")
        else:
            print(f"{field} not found in parcel data.")
    else:
        print("Parcel not found.")

# Add a new parcel entry
def add_parcel(parcel_dict):
    parcel_id = input("Enter the new parcel ID: ")
    if parcel_id not in parcel_dict:
        location = input("Enter parcel location: ")
        parcel_type = input("Enter parcel type: ")
        size = input("Enter parcel size: ")
        master_plan = input("Enter parcel master plan: ")
        price = input("Enter parcel price: ")
        parcel_dict[parcel_id] = {
            "location": location,
            "type": parcel_type,
            "size": size,
            "master_plan": master_plan,
            "price": price
        }
        print("New parcel added successfully.")
    else:
        print("Parcel ID already exists.")

# Delete an existing parcel entry
def delete_parcel(parcel_dict):
    parcel_id = input("Enter the parcel ID to delete: ")
    if parcel_id in parcel_dict:
        del parcel_dict[parcel_id]
        print("Parcel deleted successfully.")
    else:
        print("Parcel not found.")

# View all records in the dataset
def view_all_records(parcel_dict):
    if parcel_dict:
        print("\nAll Parcel Records:")
        for parcel_id, details in parcel_dict.items():
            print(f"{parcel_id}: {details}")
    else:
        print("No parcels available in the dataset.")

# Save dataset to a JSON file for persistence
def save_to_json(parcel_dict, filename="parcel_data.json"):
    with open(filename, 'w') as json_file:
        json.dump(parcel_dict, json_file, indent=4)
    print("Data saved to JSON file successfully.")

# Load dataset from a JSON file
def load_from_json(filename="parcel_data.json"):
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        print("Data loaded from JSON file successfully.")
        return data
    except FileNotFoundError:
        print("JSON file not found. Starting with an empty dataset.")
        return {}

# Main function to run the program
def main():
    # Load data from JSON file (if available)
    parcel_data = load_from_json()

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            search_parcel(parcel_data)
        elif choice == '2':
            update_parcel(parcel_data)
        elif choice == '3':
            add_parcel(parcel_data)
        elif choice == '4':
            delete_parcel(parcel_data)
        elif choice == '5':
            view_all_records(parcel_data)
        elif choice == '6':
            # Save data to JSON before exiting
            save_to_json(parcel_data)
            print("Thank you for using the parcel management system.")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()
