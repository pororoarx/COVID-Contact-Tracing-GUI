# import all the required modules (csv, tkinter, mesagebox, re, font, etc.)
import csv
import tkinter
import re
from tkinter import font
from tkinter import messagebox

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
        bold_font = font.Font(weight="bold", size=11)
        name = tkinter.Label(window, text=" II. Health Declaration Form", font=bold_font)
        name.grid(row=7, column=0, columnspan=3, sticky="w")

        # question 1 - vaccination
        question_1 = tkinter.Label(window, text="Have you been vaccinated for COVID-19?")
        question_1.grid(row=8, column=0, sticky="w")
        # set radio button for q1
        self.vaccination_var = tkinter.StringVar()
        # default selection
        self.vaccination_var.set("Not yet")  
        vaccinations = ["Not yet", "1st dose", "2nd Dose"]
        for i, vaccination in enumerate(vaccinations):
            radiobutton = tkinter.Radiobutton(window, text=vaccination, variable=self.vaccination_var, value=vaccination)
            radiobutton.grid(row=9, column=0+i, columnspan=3, sticky="w")

        # question 2 - symptoms
        question_2 = tkinter.Label(window, text="Are you experiencing any symptoms for the past 14 days? (Check all that apply. If none, leave it blank)")
        question_2.grid(row=12, column=0, columnspan=3, sticky="w")
        # set checkbutton for q2
        self.symptoms_var1 = tkinter.BooleanVar()
        self.symptoms_var2 = tkinter.BooleanVar()
        self.symptoms_var3 = tkinter.BooleanVar()
        self.symptoms_var4 = tkinter.BooleanVar()
        self.symptoms_var1.set(False)
        self.symptoms_var2.set(False)
        self.symptoms_var3.set(False)
        self.symptoms_var4.set(False)

        symptoms_options = ["Fever", "Cough", "Sore throat", "Loss of taste/smell"]
        for i, symptom in enumerate(symptoms_options):
            checkbutton = tkinter.Checkbutton(window, text=symptom, variable=self.symptoms_var1 if i == 0 else self.symptoms_var2 if i == 1 else self.symptoms_var3 if i == 2 else self.symptoms_var4)
            checkbutton.grid(row=13, column=0+i, columnspan=3, sticky="w")

        # question 3 - exposure
        question_3 = tkinter.Label(window, text="Have you had exposure to a probable or confirmed case of COVID-19 in the last 14 days?")
        question_3.grid(row=16, column=0, columnspan=3, sticky="w")
        # set radio button for q3
        self.exposure_var = tkinter.StringVar()
        self.exposure_var.set("Not yet")  
        # Default selection
        exposure = ["No", "Yes", "Not sure"]
        for i, options in enumerate(exposure):
            radiobutton = tkinter.Radiobutton(window, text=options, variable=self.exposure_var, value=options)
            radiobutton.grid(row=17, column=0+i, columnspan=3, sticky="w")

        # question 4 - contact
        question_4 = tkinter.Label(window, text="Have you been in contact with somebody who has symptoms in the last 14 days?")
        question_4.grid(row=19, column=0, columnspan=3, sticky="w")
        # set radio button for q4
        self.contact_var = tkinter.StringVar()
        self.contact_var.set("Not yet")  
        # Default selection
        in_contact = ["No", "Yes"]
        for i, options in enumerate(in_contact):
            radiobutton = tkinter.Radiobutton(window, text=options, variable=self.contact_var, value=options)
            radiobutton.grid(row=20, column=0+i, columnspan=3, sticky="w")

        # question 5 - positive
        question_5 = tkinter.Label(window, text="Have you been tested positive for COVID-19?")
        question_5.grid(row=22, column=0, columnspan=3, sticky="w")
        # set radio button for q5
        self.positive_var = tkinter.StringVar()
        self.positive_var.set("Not yet")  # Default selection
        positive_test = ["No", "Yes"]
        for i, options in enumerate(positive_test):
            radiobutton = tkinter.Radiobutton(window, text=options, variable=self.positive_var, value=options)
            radiobutton.grid(row=23, column=0+i, columnspan=3, sticky="w")

        # question 6 - places
        question_6 = tkinter.Label(window, text="What places have you been (besides of your home) in the last 14 days?")
        # Add entry field for places q6
        question_6.grid(row=24, column=0, sticky="e")
        self.question_6_entry = tkinter.Entry(window)
        self.question_6_entry.grid(row=24, column=1)

        # Set the title for data privacy section

        # add a text box for the data privacy agreememt
        # set checkbutton for data privacy

        # add the submit button 
        submit_button = tkinter.Button(window, text="Submit", command=self.contact_info)
        submit_button.grid(row=28, column=2)

        # save the window ref
        self.window = window


    # define a function for contact infos
    def contact_info(self):
        # collect all inputs of user in every field
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        middle_name = self.middle_name_entry.get()
        age = self.age_entry.get()
        address = self.address_entry.get()
        email = self.email_entry.get()
        contact = self.contact_entry.get()
        guardian_name = self.guardian_name_entry.get()
        guardian_contact = self.guardian_contact_entry.get()
        relationship = self.relationship_entry.get()
        question_1 = self.vaccination_var.get()
        question_3 = self.exposure_var.get()
        question_4 = self.contact_var.get()
        question_5 = self.positive_var.get()
        question_6 = self.question_6_entry.get()
        question_2 = [self.symptoms_var1.get(), self.symptoms_var2.get(), self.symptoms_var3.get(), self.symptoms_var4.get()]

        # add error message if required fields were not answered
        if not first_name or not last_name or not middle_name or not age or not address or not email or not contact or not question_1 or not question_2 or not question_3 or not question_4 or not question_5:
            messagebox.showerror("Error", "Please fill out all the required fields.")
        else:
            # add exception handling 
            try:
                age = int(age)
                if age < 0 or age > 150:
                    raise ValueError("Invalid age")
                # handle errors like missing field for guardian's info if user is minor
                if age < 18 and (not guardian_name or not guardian_contact or not relationship):
                    raise ValueError("Missing information")
                # handle contact number error
                

                # open csv file to to save all inputs of user

                # print a message every time a new user submit a file

            except Exception as e:
                if str(e) == "Invalid age":
                    messagebox.showerror("Error", "Invalid age")
                elif str(e) == "Missing information":
                    messagebox.showerror("Error", "Missing information. Please fill out all the required fields.")


            

        # add error message if data privacy is not checked

        # close the window


