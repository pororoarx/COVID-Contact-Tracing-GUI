# COVID-Contact-Tracing-GUI
A Python script that functions as a COVID Contract Tracing application that have a function of search and add entry that is programmed in an object-oriented-programming-way.

## Table of Contents
- Installation
- Usage
- Contributing
- Conclusion

### Installation
1.	Clone the repository to your local machine: ‘git clone git@github.com:pororoarx/COVID-Contact-Tracing-GUI.git’

### Usage
1.	Open Git Bash and go to the project directory.
2.	Open the folder COVID-Contact-Tracing-GUI with VSCode or any source-code editor for Python and run the program: ‘main_program.py’
3.	 The program will display a window with two buttons: one for adding a new entry and the other one for searching an entry. In order for the information to appear, the user needs to enter the full name of the recorded person. If the name exists, the information will appear; otherwise, an error message will be shown.
4.	If you choose "new entry", a new window will appear with fields for personal information, health declaration form, and data privacy notice and approval.
5.	If the user is a minor, the program will require filling out the information about their guardian. The program will not submit if there are missing or unfilled details.
6.  After clicking the "submit", the window will automatically close.
7.	If you choose "search entry", a new window will appear to search for entries.
8.	In order for the information to appear, the user needs to enter the full name of the recorded person. If the name exists, the information will appear. If it doesn't, an error message will be shown.

### Formulation
1. This program was formulated using Python. The new entry and create entry are separeted into different files for organization. It utilizes various modules to execute the program and tkinter for GUI. Each function has its logic and different functionalities. The program also uses the Python’s try-except feature to handle potential errors that will be made from the user’s invalid responses, such as invalid inputs or missing inputs, by displaying a simple error message to the user. Moreover, it also incorporates specific color formatting to enhance readability of the output in the window. 

### Conclusion
1. This COVID Contact Tracing App is a program designed to collect information from users about their personal information and COVID status. It stores all the data added in a CSV file and is also capable of allowing users to search for information on specific users recorded in the CSV. 
