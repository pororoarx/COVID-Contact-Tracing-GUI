# import tkinter
import tkinter
# import entry functions (add and search)
from add_entry import Create
from search_entry import Read

# main window
main = tkinter.Tk()
main.title("COVID Contact Tracing")
main.geometry("400x300")

# create the instance of a class for add entry
instance_create = Create(main)
# create the instance of a class for search entry
instance_search = Read(main)

# create a button for the add entry
create_button = tkinter.Button(main, text="Add entry", command=instance_create.create_contact, width=10, height=1, font=("Times New Roman", 12),bg="#87CEEB")
# place the add entry button in the middle
create_button.place(relx=0.5, rely=0.30, anchor=tkinter.CENTER)

# create a button for the search entry
search_button = tkinter.Button(main, text="Search entry", command=instance_search.search_contact, width=10, height=1, font=("Times New Roman", 12),bg="#87CEEB")
# place the search entry in the middle
search_button.place(relx=0.5, rely=0.60, anchor=tkinter.CENTER)

# call the main loop to start the app
main.mainloop()
