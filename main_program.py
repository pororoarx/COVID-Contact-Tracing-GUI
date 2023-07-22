# import tkinter
import tkinter
# import entry functions (add and search)
from add_entry import Create

# main window
main = tkinter.Tk()
main.title("COVID Contact Tracing")
main.geometry("400x300")

# create the instance of a class for add entry
instance_create = Create(main)
# create the instance of a class for search entry

# create a button for the add entry
# place the add entry button in the middle
# create a button for the search entry
# place the search entry in the middle

# call the main loop to start the app
main.mainloop()