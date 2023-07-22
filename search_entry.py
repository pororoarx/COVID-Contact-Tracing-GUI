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
        name = self.full_name_entry.get()
        data = []
        # open csv file and store its value in data
        with open("file1.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        # create the list of all the names from the data
        list_info = [x[0] for x in data]

        # execute the following code if name exists in the list
        if name in list_info:
            # if name is available, display the information
            for x in range(0, len(data)):
                if name == data[x][0]:
                    # create a mew window for the information of searched user
                    display_info = tkinter.Toplevel(self.main)
                    display_info.title("Information")
                    display_info.geometry("500x300")

                    # set labels for every contact information
                    # name
                    name = tkinter.Label(display_info, text="Full Name: " + str(data[x][0]))
                    name.pack(anchor='w')
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


  