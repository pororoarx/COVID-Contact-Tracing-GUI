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
                    age = tkinter.Label(display_info, text="Age: " + str(data[x][1]))
                    age.pack(anchor='w')
                    # address
                    address = tkinter.Label(display_info, text="Address: " + str(data[x][2]))
                    address.pack(anchor='w')
                    # email
                    email = tkinter.Label(display_info, text="Email: " + str(data[x][3]))
                    email.pack(anchor='w')
                    # contact
                    contact = tkinter.Label(display_info, text="Contact Number: " + str(data[x][4]))
                    contact.pack(anchor='w')
                    # guardian name
                    guardian_name = tkinter.Label(display_info, text="Guardian's Name: " + str(data[x][5]))
                    guardian_name.pack(anchor='w')
                    # guardian contact
                    guardian_contact = tkinter.Label(display_info, text="Guardian's Contact No.: " + str(data[x][6]))
                    guardian_contact.pack(anchor='w')
                    # relationship
                    relationship = tkinter.Label(display_info, text="Relationship: " + str(data[x][7]))
                    relationship.pack(anchor='w')
                    # question 1
                    vaccination_status = tkinter.Label(display_info, text="Vaccination(Yes/No): " + str(data[x][8]))
                    vaccination_status.pack(anchor='w')
                    # question 2
                    symptoms = tkinter.Label(display_info, text="Symptoms (Fever, Cough, Sore throat, Loss of taste/smell): " + str(data[x][9]))
                    symptoms.pack(anchor='w')
                    # question 3
                    exposure = tkinter.Label(display_info, text="Exposed? (Yes/No): " + str(data[x][10]))
                    exposure.pack(anchor='w')
                    # question 4
                    contact = tkinter.Label(display_info, text="Have been in contact to someone with COVID? (Yes/No): " + str(data[x][11]))
                    contact.pack(anchor='w')
                    # question 5
                    positive = tkinter.Label(display_info, text="Tested positive in COVID? (Yes/No): " + str(data[x][12]))
                    positive.pack(anchor='w')
                    # question 6
                    places = tkinter.Label(display_info, text="Visited places: " + str(data[x][13]))
                    places.pack(anchor='w')
                    print(data[x][0])

            # if the name is not found, display error message


  