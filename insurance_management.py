import pickle
from insured_person import InsuredPerson

class InsuranceManagement:
    """
    Class managing collections of insured persons.
    Methods:
    - __init__(): Initializes an empty list of insured_people.
    - add_insured_person(insured_person): Adds an InsuredPerson instance to the list.
    - remove_insured_person(first_name, last_name, phone_number): Removes an InsuredPerson from the list based on first_name, last_name, and phone_number.
    - display_list(): Returns a list of string representations of InsuredPerson instances.
    - find_insured_person(first_name, last_name): Finds InsuredPerson instances in the list based on first_name and last_name.
    - save_to_file(file_name): Saves the list of insured_people to a binary file using pickle.
    - load_from_file(file_name): Loads the list of insured_people from a binary file.
    """

    def __init__(self):
        self.insured_people = []

    # Method for adding an insured person
    def add_insured_person(self, insured_person):
        """
        string :param insured_person: Instance of the InsuredPerson class.
        string :return: Success or error message.
        """
        # Check if any column remains empty
        if insured_person.first_name.strip() and insured_person.last_name.strip():
            self.insured_people.append(insured_person)
            return "Insured person was successfully added."
        else:
            return "Error: All data must be provided, otherwise the insured person will not be saved."

    # Method for removing an insured person based on first name, last name, and phone number
    def remove_insured_person(self, first_name, last_name, phone_number):
        """
        string :param first_name: First name of the removed user.
        string :param last_name: Last name of the removed user.
        integer :param phone_number: Phone number of the removed user.
        string :return: Success or error message.
        """
        found_insured_people = []
        for insured_person in self.insured_people:
            if insured_person.first_name == first_name and insured_person.last_name == last_name and insured_person.phone_number == phone_number:
                found_insured_people.append(insured_person)

        if found_insured_people:
            for found_insured_person in found_insured_people:
                self.insured_people.remove(found_insured_person)
            return "Insured person was successfully removed from the records."
        else:
            return "Insured person not found."

    # Method for displaying a list of insured persons
    def display_list(self):
        """
        string :return: List of strings representing InsuredPerson instances.
        """
        list_of_insured_people = []
        for insured_person in self.insured_people:
            list_of_insured_people.append(str(insured_person))
        return list_of_insured_people

    # Method for finding an insured person
    def find_insured_person(self, first_name, last_name):
        """
        string :param first_name: First name to search for.
        string :param last_name: Last name to search for.
        string :return: List of found InsuredPerson instances.
        """
        found_insured_people = []
        for insured_person in self.insured_people:
            if insured_person.first_name == first_name and insured_person.last_name == last_name:
                found_insured_people.append(insured_person)

        return found_insured_people

    # Saving data to a real database:
    def save_to_file(self, file_name):
        """
        string :param file_name: Name of the file to save the data.
        string :return: Success or error message.
        """
        with open(file_name, 'wb') as file:
            pickle.dump(self.insured_people, file)
        return "Data was successfully saved to the file."

    # Loading data from a file:
    def load_from_file(self, file_name):
        """
        string :param file_name: Name of the file to load the data from
        string :return: Success or error message.
        """
        try:
            with open(file_name, 'rb') as file:
                self.insured_people = pickle.load(file)
            return "Data loaded from the file 'insurance_records.pkl'."
        except FileNotFoundError:
            return "File not found. A new record will be created."