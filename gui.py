########################
# GUI-Author: Nauman Afsar
# Date: 27-03-2018
#########################

#########################
# importing Libraries
#########################
# import tkinter as tk        # Python 3: "t" lower-case
from tkinter import Menu
from tkinter import ttk
from tkinter import *


root = Tk()


def windows_size():
    root.update()                        # to get runtime size
    print('width  =', root.winfo_width())
    print('height =', root.winfo_height())

def resize_window():
    root.minsize(width=500, height=500)
    # disable resizing the GUI
    root.resizable(0,0)
def quit():
    root.quit()
    root.destroty()
    exit()
    
root.title("ATM Project")

# Menu Bar
menuBar = Menu()
root.config(menu = menuBar)

# Menu Items

filemenu = Menu(menuBar, tearoff = 0)
filemenu.add_command(label = "New")
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = quit) #Calling the quit function
menuBar.add_cascade(label = "File", menu = filemenu)

# Add another Menu to the Menu Bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)
# ---------------------------------------------------------------

# Tab Control / Notebook introduced here ------------------------
tabControl = ttk.Notebook(root)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab
tabControl.add(tab1, text='My ATM')      # Add the tab

tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='Instructions')      # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible
# ---------------------------------------------------------------
instr = ttk.LabelFrame(tab2, text='This Tab will be containing all the Instruction we are going to have for our program!')

# using the tkinter grid layout manager
instr.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(instr, text="All The Instructions are as follows: \n 1. If you are reading this then it means that you have downloaded this file. \n 2. Install Python3 on your system if you haven't already. \n 3. Install tkinter module in order to run the GUI of this program \n 4. The default username is abc xyz \n 5. The Default password is 1234 \n 6. If you are having any issues than please report it so we can fix it!").grid(column=0, row=0, sticky='W')

ttk.Label(tab1,text="Please Enter Your Username: ").grid(row=0, sticky="W")
Entry(tab1).grid(row=0, column=1)
ttk.Label(tab1, text="Please Enter Your Secret PIN: ").grid(row=1, sticky="W")
Entry(tab1).grid(row=1, column=1)
# ---------------------------------------------------------------


#======================
# Start GUI
#======================
# windows_size()
resize_window()
# print()
# windows_size()
root.mainloop()