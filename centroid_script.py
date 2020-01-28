# Script for calculating centroid of a triangle

'''
# This is the traditional code, with no UI
print("Enter 6 values, x1, y1, x2, y2, x3, y3")
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

xcentroid = (x1+x2+x3)/3
ycentroid = (y1+y2+y3)/3
print(x1, y1, x2, y2, x3, y3)
print("Centroid: " + str(xcentroid) + str(ycentroid))
'''


from tkinter import *
from tkinter import ttk


def calculate(*args):

    centroid = str(x3y3.get())
    centroid_list = centroid.split(",")
    x1 = int(centroid_list[0])
    x2 = int(centroid_list[2])
    x3 = int(centroid_list[4])
    y1 = int(centroid_list[1])
    y2 = int(centroid_list[3])
    y3 = int(centroid_list[5])
    xans = (x1 + x2 + x3)/3
    yans = (y1 + y2 + y3)/3
    answer = ("(" + str(xans) + ", " + str(yans) + ")")
    finalanswer.set(answer)


root = Tk()
root.title("Calculating The Centroid")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


x3y3 = StringVar()
finalanswer = StringVar()

x3y3_entry = ttk.Entry(mainframe, width=7, textvariable=x3y3)
x3y3_entry.grid(column=1, row=3, sticky=(W, S))

ttk.Label(mainframe, textvariable=finalanswer).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


x3y3_entry.focus()
root.bind('<Return>', calculate)
root.mainloop()
