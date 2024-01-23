# File where the implemented classes 'InsuredPerson' and 'InsuranceManagement' are reflected
from insured_person import InsuredPerson
from insurance_management import InsuranceManagement

# Creating an instance of 'insurance management':
insurance_management = InsuranceManagement()

# Loading data from a file:
print(insurance_management.load_from_file('insurance_records.pkl'))

choice = ""

while choice != "5":
    print("\n----- Menu -----")
    print("1. Add insured person")
    print("2. Remove insured person")
    print("3. Display list of insured persons")
    print("4. Find insured person")
    print("5. Exit")

    choice = input("Choose action (1-5):\n")

    # Adding insured person:
    if choice == "1":
        while True:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            # Validation of empty first name and last name
            if not first_name.strip() or not last_name.strip():
                print("Error: First name and last name must not be empty.")
                continue  # Continue in the loop to let the user enter the data again.

            # Validation: Check if first name and last name contain only letters
            if not first_name.isalpha() or not last_name.isalpha():
                print("Error: First name and last name must contain only letters. Try again.")
                continue  # Continue in the loop to let the user enter the data again.

            age = input("Enter age: ")
            phone = input("Enter phone number: ")

            # Validation of age as a number
            try:
                age = int(age)
            except ValueError:
                print("Error: Age must be a whole number. Try again.")
                continue  # Continue in the loop to let the user enter the data again.

            # Validation of phone number as a number
            try:
                phone = int(phone)
            except ValueError:
                print("Error: Phone number must be a whole number. Try again.")
                continue  # Continue in the loop to let the user enter the data again.

            new_insured_person = InsuredPerson(first_name, last_name, age, phone)
            insurance_management.add_insured_person(new_insured_person)
            print("Insured person was successfully added.")
            break  # End the loop because the data is valid

        enter = input("To continue, press enter.")

    # Removing insured person:
    elif choice == "2":
        while True:
            first_name_to_remove = input("Enter the first name of the insured person to remove: ")
            last_name_to_remove = input("Enter the last name of the insured person to remove: ")
            #As for third condition to remove insured person I chose phone number, because it is unique data.
            phone_number_to_remove = input("Enter the phone number of the insured person to remove: ")

            # Validating if all fields are filled
            if first_name_to_remove.strip() and last_name_to_remove.strip() and phone_number_to_remove.strip():
                # Try to convert phone number to an integer
                try:
                    phone_number_to_remove = int(phone_number_to_remove)
                    break  # Break out of the loop if all data is valid
                except ValueError:
                    print("Error: Phone number must be a whole number. Try again.")
            else:
                print("Error: All fields must be filled. Try again.")

        print(insurance_management.remove_insured_person(first_name_to_remove, last_name_to_remove,
                                                         phone_number_to_remove))
        enter = input("To continue, press enter.")

    # Displaying the list of insured persons:
    elif choice == "3":
        list_of_insured_people = insurance_management.display_list()
        for item in list_of_insured_people:
            print(item)
        # Prompt for the next action
        enter = input("To continue, press enter.")

    # Finding insured person:
    elif choice == "4":
        first_name_to_find = input("Enter the first name of the person to find: ")
        last_name_to_find = input("Enter the last name of the person to find: ")

        found_insured_people = insurance_management.find_insured_person(first_name_to_find, last_name_to_find)
        if found_insured_people:
            print("Found insured persons:")
            for found_insured_person in found_insured_people:
                print(found_insured_person)
        else:
            print("Insured persons not found.")

        enter = input("To continue, press enter.")

    # Exiting the program:
    elif choice == "5":
        print("End of the program.")
        break

    # Invalid choice:
    else:
        print("Invalid choice. Try again.")

# Saving data when exiting the program:
print(insurance_management.save_to_file('insurance_records.pkl'))
