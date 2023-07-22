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
        # Add entry field for last name
        # Add entry field for middle name
        # Add entry field for age
        age = tkinter.Label(window, text="Age")
        age.grid(row=2, column=0, sticky="e")
        self.age_entry = tkinter.Entry(window)
        self.age_entry.grid(row=2, column=1)
        # Add entry field for address
        # Add entry field for email
        # Add entry field for contact
        # if minor:
        # Add entry field for guardian's name 
        # Add entry field for guardian's contact number
        # Add entry field for their relationship

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

        # save the window ref


    # define a function for contact infos
        # collect all inputs of user in every field

        # add error message if required fields were not answered

            # add exception handling for age
            # handle errors like missing field for guardian's info if user is minor

                # open csv file to to save all inputs of user

                # print a message every time a new user submit a file

        # add error message if data privacy is not checked

        # close the window


