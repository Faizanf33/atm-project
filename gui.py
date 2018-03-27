########################
# GUI-Author: Nauman Afsar
# Date: 27-03-2018
#########################

#########################
# importing Libraries
#########################
import tkinter as tk        # Python 3: "t" lower-case


win = tk.Tk()
win.title("ATM Project")

def windows_size():
    win.update()                        # to get runtime size
    print('width  =', win.winfo_width())
    print('height =', win.winfo_height())

def increase_window_width():
    win.minsize(width=500, height=500)
    # disable resizing the GUI
    win.resizable(0,0)

#======================
# Start GUI
#======================
windows_size()
increase_window_width()
print()
windows_size()
win.mainloop()
