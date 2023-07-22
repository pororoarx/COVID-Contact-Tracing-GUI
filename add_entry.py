# import all the required modules (csv, tkinter, mesagebox, re, font, etc.)
import csv
import tkinter
from tkinter import font

# define the Create class
class Create:
    def __init__(self, main):
        # initiliaze main window 
        self.main = main
        # BooleanVar for data privacy agreement
        self.data_privacy_agree = tkinter.BooleanVar()
        self.data_privacy_agree.set(False)

    # define the function for add entry
    def create_contact(self):
        window = tkinter.Toplevel(self.main)
        # new window for add entry
        window.title("Add a new contact")
        window.geometry("1000x600")

        # Set the title for personal information entry
        bold_font = font.Font(weight="bold", size=11)
        name = tkinter.Label(window, text=" I. Personal Information", font=bold_font)
        name.grid(row=0, column=0, columnspan=3, sticky="w")

        # Add entry field for first name
        first_name = tkinter.Label(window, text="First Name")
        first_name.grid(row=1, column=0, sticky="e")
        self.first_name_entry = tkinter.Entry(window)
        self.first_name_entry.grid(row=1, column=1)

        # Add entry field for last name
        last_name = tkinter.Label(window, text="Last Name")
        last_name.grid(row=1, column=2, sticky="e")
        self.last_name_entry = tkinter.Entry(window)
        self.last_name_entry.grid(row=1, column=3)

        # Add entry field for middle name
        middle_name = tkinter.Label(window, text="Middle Name")
        middle_name.grid(row=1, column=4, sticky="e")
        self.middle_name_entry = tkinter.Entry(window)
        self.middle_name_entry.grid(row=1, column=5)

        # Add entry field for age
        age = tkinter.Label(window, text="Age")
        age.grid(row=2, column=0, sticky="e")
        self.age_entry = tkinter.Entry(window)
        self.age_entry.grid(row=2, column=1)

        # Add entry field for address
        address = tkinter.Label(window, text="Address")
        address.grid(row=2, column=2, sticky="e")
        self.address_entry = tkinter.Entry(window)
        self.address_entry.grid(row=2, column=3)

        # Add entry field for email
        email = tkinter.Label(window, text="Email")
        email.grid(row=2, column=4, sticky="e")
        self.email_entry = tkinter.Entry(window)
        self.email_entry.grid(row=2, column=5)

        # Add entry field for contact
        contact = tkinter.Label(window, text="Contact No.:")
        contact.grid(row=3, column=0, sticky="e")
        self.contact_entry = tkinter.Entry(window)
        self.contact_entry.grid(row=3, column=1)

        # if minor:
        # Add entry field for guardian's name 
        guardian_name = tkinter.Label(window, text="Guardian's name:")
        guardian_name.grid(row=3, column=2, sticky="e")
        self.guardian_name_entry = tkinter.Entry(window)
        self.guardian_name_entry.grid(row=3, column=3)

        # Add entry field for guardian's contact number
        guardian_contact = tkinter.Label(window, text="Guardian's contact no.:")
        guardian_contact.grid(row=3, column=4, sticky="e")
        self.guardian_contact_entry = tkinter.Entry(window)
        self.guardian_contact_entry.grid(row=3, column=5)

        # Add entry field for their relationship
        relationship_name = tkinter.Label(window, text="Relationship:")
        relationship_name.grid(row=4, column=0, sticky="e")
        self.relationship_entry = tkinter.Entry(window)
        self.relationship_entry.grid(row=4, column=1)

        # Set the title for health declaration form entry

        # question 1 - vaccination
        # set radio button for q1
        # question 2 - symptoms
        # set checkbutton for q2
        # question 3 - exposure
        # set radio button for q3
        # question 4 - contact
        # set radio button for q4
        # question 5 - positive
        # set radio button for q5
        # question 6 - places
        # Add entry field for places q6

        # Set the title for data privacy section

        # add a text box for the data privacy agreememt
        # set checkbutton for data privacy

        # add the submit button 
        submit_button = tkinter.Button(window, text="Submit", command=self.contact_info)
        submit_button.grid(row=28, column=2)

        # save the window ref
        self.window = window


    # define a function for contact infos
        # collect all inputs of user in every field

        # add error message if required fields were not answered

            # add exception handling for age
            # handle errors like missing field for guardian's info if user is minor

                # open csv file to to save all inputs of user

                # print a message every time a new user submit a file

        # add error message if data privacy is not checked

        # close the window


