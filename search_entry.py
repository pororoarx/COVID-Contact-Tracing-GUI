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
        window.geometry("250x250")
        window.configure(bg="#ADD8E6")
        backdrop = tkinter.Frame(window, bg="white", width=225, height=225)
        backdrop.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # set label for asked input and add field  
        full_name = tkinter.Label(window, text="Enter full name")
        full_name.grid(row=0, column=4, padx=90, pady=50, sticky="w")
        self.full_name_entry = tkinter.Entry(window)
        self.full_name_entry.grid(row=1, column=4, sticky="w", padx=70, pady=10)

        # add the button to start search
        search_button = tkinter.Button(window, text="Search", command=self.contact_info_read)
        search_button.grid(row=2, column=4)

    # define a function to read the information from CSV file
    def contact_info_read(self):
        # take the entered input from the search widget
        name = self.full_name_entry.get().lower()

        # handle error if user entered submit with unfilled info
        if not name.strip():
            messagebox.showerror("Error", "Please enter a name")
            return

        data = []
        # open csv file and store its value in data
        with open("COVID_info.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)

        # create the list of all the names from the data
        list_info = [x[0].lower() for x in data if x]

        # execute the following code if name exists in the list
        if name in list_info:
            # if name is available, display the information
            for x in range(0, len(data)):
                if data[x] and name == data[x][0].lower():
                    # create a mew window for the information of searched user
                    display_info = tkinter.Toplevel(self.main)
                    display_info.title("Information")
                    display_info.geometry("500x400")
                    display_info.configure(bg="#ADD8E6")
                    backdrop = tkinter.Frame(display_info, bg="white", width=475, height=375)
                    backdrop.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

                    # set labels for every contact information
                    # name
                    name = tkinter.Label(display_info, text="Full Name: " + str(data[x][0]))
                    name.pack(anchor='w', padx=20, pady=20)
                    # age
                    age = tkinter.Label(display_info, text="Age: " + str(data[x][1]))
                    age.pack(anchor='w', padx=20)
                    # address
                    address = tkinter.Label(display_info, text="Address: " + str(data[x][2]))
                    address.pack(anchor='w', padx=20, pady=2)
                    # email
                    email = tkinter.Label(display_info, text="Email: " + str(data[x][3]))
                    email.pack(anchor='w', padx=20, pady=2)
                    # contact
                    contact = tkinter.Label(display_info, text="Contact Number: " + str(data[x][4]))
                    contact.pack(anchor='w', padx=20, pady=2)
                    # guardian name
                    guardian_name = tkinter.Label(display_info, text="Guardian's Name: " + str(data[x][5]))
                    guardian_name.pack(anchor='w', padx=20, pady=2)
                    # guardian contact
                    guardian_contact = tkinter.Label(display_info, text="Guardian's Contact No.: " + str(data[x][6]))
                    guardian_contact.pack(anchor='w', padx=20, pady=2)
                    # relationship
                    relationship = tkinter.Label(display_info, text="Relationship: " + str(data[x][7]))
                    relationship.pack(anchor='w', padx=20, pady=2)
                    # question 1
                    vaccination_status = tkinter.Label(display_info, text="Vaccination(Yes/No): " + str(data[x][8]))
                    vaccination_status.pack(anchor='w', padx=20, pady=2)
                    # question 2
                    symptoms = tkinter.Label(display_info, text="Symptoms (Fever, Cough, Sore throat, Loss of taste/smell): " + str(data[x][9]))
                    symptoms.pack(anchor='w', padx=20, pady=2)
                    # question 3
                    exposure = tkinter.Label(display_info, text="Exposed? (Yes/No): " + str(data[x][10]))
                    exposure.pack(anchor='w', padx=20, pady=2)
                    # question 4
                    contact = tkinter.Label(display_info, text="Have been in contact to someone with COVID? (Yes/No): " + str(data[x][11]))
                    contact.pack(anchor='w', padx=20, pady=2)
                    # question 5
                    positive = tkinter.Label(display_info, text="Tested positive in COVID? (Yes/No): " + str(data[x][12]))
                    positive.pack(anchor='w', padx=20, pady=2)
                    # question 6
                    places = tkinter.Label(display_info, text="Visited places: " + str(data[x][13]))
                    places.pack(anchor='w', padx=20, pady=2)
                    print(data[x][0])

            # if the name is not found, display error message
        else:
            # if the name is not found, display error message
            messagebox.showerror("Error", "Data not found")
            print("Not available")
            

  