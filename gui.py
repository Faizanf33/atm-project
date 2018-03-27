########################
# GUI-Author: Nauman Afsar
# Date: 27-03-2018
#########################

#########################
# importing Libraries
#########################
import tkinter
import tkinter as tk        # Python 3: "t" lower-case
from tkinter import Menu
from tkinter import ttk

top = tkinter.Tk()


def windows_size():
    win.update()                        # to get runtime size
    print('width  =', win.winfo_width())
    print('height =', win.winfo_height())

def resize_window():
    win.minsize(width=500, height=500)
    # disable resizing the GUI
    win.resizable(0,0)
def quit():
    win.quit()
    win.destroty()
    exit()


win = tk.Tk()
win.title("ATM Project")

# Menu Bar
menuBar = Menu()
win.config(menu = menuBar)

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
tabControl = ttk.Notebook(win)          # Create Tab Control

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

main = ttk.LabelFrame(tab1, text="Please Read the Instructions before Login! \n Login:")
ttk.Label(main, text="This Block is Underconstruction :)").grid(column=0, row=0, sticky='W')

ttk.Label(tab1, text="Login:").grid(column=0, row=0, sticky='W')

# ---------------------------------------------------------------


#======================
# Start GUI
#======================
windows_size()
resize_window()
print()
windows_size()
win.mainloop()
