# import necessary modules
import csv
import tkinter 
from tkinter import messagebox

# create a class for search entry
class Read:
    # set constructor for the class
    def __init__(self, main):
        self.main = main

    # define a function to search for a contact information
    def search_contact(self):
        # create a new window for searching
        window = tkinter.Toplevel(self.main)
        window.title("Search Contact")
        window.geometry("150x150")

        # set label for asked input and add field  
        full_name = tkinter.Label(window, text="Enter full name")
        full_name.grid(row=0, column=4, padx=20)
        self.full_name_entry = tkinter.Entry(window)
        self.full_name_entry.grid(row=1, column=4)

        # add the button to start search
        search_button = tkinter.Button(window, text="Search", command=self.contact_info_read)
        search_button.grid(row=2, column=4)

    # define a function to read the information from CSV file
    def contact_info_read(self):
        # take the entered input from the search widget
        # open csv file and store its value in data
        # create the list of all the names from the data

        # execute the following code if name exists in the list
            # if name is available, display the information
                    # create a mew window for the information of searched user

                    # set labels for every contact information
                    # name
                    # age
                    # address
                    # email
                    # contact
                    # guardian name
                    # guardian contact
                    # relationship
                    # question 1
                    # question 2
                    # question 3
                    # question 4
                    # question 5
                    # question 6

            # if the name is not found, display error message


  