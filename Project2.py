# Project 2
# Name: Vadym Didukh
# Project 2 will test on topics learned in class so far. You will be creating a contact list program with an external csv file that will store the contacts. MAKE YOUR LIFE EASIER AND ENABLE WORDWRAP! VIEW -> WORD WRAP.
#
# The program will have the following features:
# 1. Add contact
# 2. View contacts
# 3. Delete contact
# 4. Save contacts to csv file
# 5. Next Birthday
# 0. Quit

# Import the csv module, datetime module
import csv
import datetime as dt

# Make sure to show docs strings for each function and include comments in your code. Make sure to include a main function and call the main function at the end of the program.

print("\nWelcome to the Contact List Program\n")

# There is also a contact.csv file that will be used to store the contacts. The csv file will have the following format:
# Name,Phone,Email,Birthday
# The program will be menu driven and will display the menu as shown above.
# The program will run until the user selects option 0 to quit.
# The program will be implemented in a file called Project2.py.
# The program will use the following functions:


# import_csv - This function will import the contacts from the csv file. The function will return a dictionary of contacts.
# The key will be the name of the contact and the value will be a dictionary containing the phone number, email address, and birthday.
# The function will take one parameter, the name of the csv file.
# The function will display an error message if the file does not exist.
# The function will display a message if the file exists and the contacts were imported successfully.
# Hint1: Use the csv module to read the csv file. Use the csv.reader function. IE. reader = csv.reader(file)
# Hint2: You will need to skip the first line of the csv file since it contains the column headers. You can do that with the next function. IE. next(reader)
# Hint3: You will need to create a dictionary of contacts. You can do that by looping through the reader object. IE. for row in reader:
# Hint4: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(row[3], '%m/%d/%Y')
# Hint5: You will need to create a dictionary of the phone number, email address, and birthday. You can do that by creating a dictionary and adding the values to the dictionary. IE. contact[row[0]] = {'Phone': row[1], 'Email': row[2], 'Birthday': dt.datetime.strptime(row[3], '%m/%d/%Y')}
# Hint6: Use the FileNotFoundError exception to catch if the file does not exist.

def import_csv(filename):
    """
    Import contacts from a CSV file.

    """

    contacts = {}

    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print(row)  # Debug print
                name = row[0]
                phone = row[1]
                email = row[2]
                birthday = dt.datetime.strptime(row[3], '%m/%d/%Y')
                contacts[name] = {"Phone": phone, "Email": email, "Birthday": birthday}
        
        print("\nContacts imported successfully.")
        return contacts
    
    except FileNotFoundError:
        print("\nError: File not found.")
        return {}
    

# add_contact(name, phone, email, birthday) - This function will add a contact to the dictionary. The function will take four parameters, the name, phone number, email address, and birthday. The function will return True if the contact was added and False if the contact was not added. The function will display an error message if the contact already exists.
# Hint 1: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(birthday, '%m/%d/%Y')
# Hint 2: To add a contact to the dictionary, you need to use the key as the name and the values as a dictionary that contains the phone number, email address, and birthday. To reference the specific key you can use contact[name]

def add_contact(name, phone, email, birthday, contacts):
    """
    Add a contact to the dictionary.

    Args:
    name (str): Name of the contact.
    phone (str): Phone number of the contact.
    email (str): Email address of the contact.
    birthday (str): Birthday of the contact in format 'mm/dd/yyyy'.
    contacts (dict): Dictionary containing existing contacts.

    Returns:
    bool: True if the contact was added successfully, False otherwise.
    """

    if name in contacts:
        print("Error: Contact already exists.")
        return False
    else:
        contacts[name] = {"Phone": phone, "Email": email, "Birthday": dt.datetime.strptime(birthday, "%m/%d/%Y")}
        print("Contact added successfully.")
        return True

# view_contacts() - This function will display the contacts in the dictionary. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. Use string formatting to display the contacts in a table format. The table should have a header row and each contact should be on a separate row. The table should have the following columns: Name, Phone, Email, Birthday. The birthday should be formatted as mm/dd/yyyy. The table should be sorted by name.
# Hint 1: You will need to loop through the dictionary to display the contacts. IE. for key, value in contact.items():
# Extra Credit: The data is a dictionary of dictionaries.
# You can unpack the dictionary into a list of dictionaries.
# Like in Lab 11 and then use the tabulate library to display the contacts in a table format.
# This is optional and not required. You can use string formatting to display the contacts in a table format.

def view_contacts(contacts):
    """
    Display contacts in a table format.

    Args:
    contacts (dict): Dictionary containing contacts.
    
    """

    if not contacts:
        print("No contacts found.")
    else:
        print("{:<20} {:<15} {:<25} {:<10}".format("Name", "Phone", "Email", "Birthday"))
        print("-" * 70)
        for name, info in sorted(contacts.items()):
            print("{:<20} {:<15} {:<25} {:<10}".format(name, info["Phone"], info["Email"], info["Birthday"].strftime('%m/%d/%Y')))

# delete_contact(id) - This function will delete a contact from the dictionary.
# The function will take one parameter, the name of the contact to delete.
# The function will return True if the contact was deleted and False if the contact was not deleted.
# The function will display an error message if the contact does not exist.

def delete_contact(name, contacts):
    """
    Delete a contact from the dictionary.
    
    Args:
    name (str): Name of the contact to delete.
    contacts (dict): Dictionary containing existing contacts.

    Returns:
    bool: True if the contact was deleted successfully, False otherwise.
    """    
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
        return True
    else:
        print("Error: Contact not found.")
        return False
    
# next_birthday() - This function will display the next birthday. The function will take no parameters.
# The function will return nothing. The function will display a message if there are no contacts in the dictionary.
# The function will display a message if there are no birthdays in the next 30 days.
# The function will display the next birthday and name if there is a birthday in the next 30 days.
# Use string formatting to display the next birthday.
# The birthdays should be sorted in consecutive order.
# The birthday dates should be formatted as mm/dd/yyyy.
# Hint: We dont care about the year, only the month and day. There are many ways to solve this issue.
# 1: you could replace all the years with the current year.
# 2: you could use the month and day attributes of the datetime object to compare the month and day of the birthday to the current month and day.
    
def next_birthday(contacts):
    """
    Display the next birthday.
    
    """
    today = dt.datetime.now()
    next_birthday_date = None
    next_birthday_name = None

    for name, info in contacts.items():
        contact_birthday = info["Birthday"].replace(year = today.year)
        if contact_birthday < today:
            contact_birthday = contact_birthday.replace(year = today.year + 1)
        if today <= contact_birthday <= today + dt.timedelta(days = 30):
            if next_birthday_date is None or contact_birthday < next_birthday_date:
                next_birthday_date = contact_birthday
                next_birthday_name = name

    if next_birthday_date:
        print(f"Next birthday: {next_birthday_date.strftime('%m/%d')} - {next_birthday_name}")
    else:
        print("No upcoming birthdays in the next 30 days.") 

# save_csv() - This function will save the contacts to the csv file.
# Prompt the user to enter a filename to save the contacts to.
# If the file exists, overwrite the file. If the file does not exist, create the file.
# The function will return True if the contacts were saved and False if the contacts were not saved.
def save_csv(filename, contacts):
    """
    Save contacts to a CSV file.

    Args:
    filename (str): The name of the CSV file to save.
    contacts (dict): Dictionary containing contacts.

    Returns:
    bool: True if the contacts were saved successfully, False otherwise.
    """

    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email", "Birthday"])
            for name, info in contacts.items():
                writer.writerow([name, info["Phone"], info["Email"], info["Birthday"].strftime('%m/%d/%Y')])
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# The main function will be used to run the program.
# The main function will use a while loop to display the menu and get the user's choice.
# The main function will call the appropriate function based on the user's choice.
# The main function will also call the save_csv function to save the contacts to the csv file before the program ends.


def main():
    filename = "contacts.csv"
    contacts = import_csv(filename)

    while True:
        print("\nMenu:")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Delete contact")
        print("4. Save contacts to csv file")
        print("5. Next Birthday")
        print("0. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            birthday = input("Enter birthday (mm/dd/yyyy): ")
            add_contact(name, phone, email, birthday, contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name, contacts)

        elif choice == "4":
            if save_csv(filename, contacts):
                print("Contacts saved successfully.")

        elif choice == "5":
            next_birthday(contacts)

        elif choice == "0":
            if save_csv(filename, contacts):
                print("\nContacts saved successfully.\n")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 5.")
    return contacts

    
    # After you are done with the program, answer the following questions using code (show your code and output):
    # How many names start with the letter A?

    # How many emails are yahoo emails?

    # How many .org emails are there?

    # How many contacts have a birthday in January?
    
def answer_questions(contacts):            
             
    names_starting_with_A = sum(1 for name in contacts.keys() if name.startswith('A'))
    print("\nNames starting with A:", names_starting_with_A)

    yahoo_emails = sum(1 for info in contacts.values() if info["Email"].endswith("@yahoo.com"))
    print("Yahoo emails:", yahoo_emails)

    org_emails = sum(1 for info in contacts.values() if info["Email"].endswith(".org"))
    print("Organization emails:", org_emails)

    january_birthdays = sum(1 for info in contacts.values() if info["Birthday"].month == 1)
    print("Contacts with a birthday in January:", january_birthdays)       


# Final Note: You will want to utilize code from other labs, homeworks, and projects. The Bank Account Program will be a good resource for the menu and main function. Use try except statements when possible.


if __name__ == "__main__":
    contacts = main() 
    answer_questions(contacts)
   

    


