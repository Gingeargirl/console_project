class InsuredPerson:
    """
    Class representing an insured person with personal information.
    Methods:
    -__init__(): Describes the parameters that the method accepts.
    -__str__(): Returns a formatted string representation of the insured person.
    """
#Initialization for a new instance of the InsuredPerson class
    def __init__(self, first_name, last_name, age, phone_number):
        """
        string :param first_name: The first name of the insured person.
        string :param last_name: The last name of the insured person.
        integer :param age: The age of the insured person.
        integer :param phone_number: The phone number of the insured person.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number

#Method returning a string representation of the insured person
    def __str__(self):
        """
        string :return: Formatted string containing the first name, last name, age, and phone number.
        """
        return f"First Name: {self.first_name},\tLast Name: {self.last_name},\tAge: {self.age} years,\tPhone Number: {self.phone_number}"
