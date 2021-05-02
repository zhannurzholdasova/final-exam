from tkinter import *
import csv

file = 'bus_stop.csv'
open_file = open(file)
read_file = csv.reader(open_file, delimiter=';')
d = list(read_file)
del (d[0])
bus = []
bus2 = []
num_bus = []
stop_bus = []
stop = []
for x in range(len(d)):
    bus.append(d[x][1])
    stop.append(d[x][0])

win = Tk()
win.geometry('500x300')
win.title('ATYRAU-BUS')
win['bg'] = 'moccasin'


def begin():
    la1.grid(row=0, column=0,pady=50)
    e1.grid(row=1, column=0, padx=155, pady=10)
    b1.grid(row=2, column=0)
def search():
    if e1.get() in bus:
        e1.grid_forget()
        b1.grid_forget()
        la1.grid_forget()
        la2.grid(row=0, column=0, pady=10)
        l1.grid(row=1, column=0, padx=155, pady=10)
        b2.grid(row=2, column=0)
        for i, y in enumerate(bus):
            if e1.get() == y:
                stop_bus.append(stop[i])
                var2 = StringVar(value=stop_bus)
                l1.config(listvariable=var2)

    else:
        begin()
def stopbus():
    b2.grid_forget()
    la3.grid(row=3, column=0, pady=10)
    l2.grid(row=4, column=0, padx=155)
    i = l1.curselection()[0]
    print(stop_bus[i])
    for x, y in enumerate(stop):
        if y == stop_bus[i]:
            bus2.append(bus[x])

            var2 = StringVar(value=bus2)
            l2.config(listvariable=var2)
la1 = Label(win, text='CHOOSE BUS NUMBER', bg='moccasin', font='ArialBlack')
l1 = Listbox(win, listvariable='', width=30, height=5)
l2 = Listbox(win, listvariable='', width=30, height=5)

b1 = Button(win, text='SEARCH', bg='white', command=search
b2 = Button(win, text='SEARCH', bg='white', command=stopbus)

la1 = Label(win, text='CHOOSE BUS NUMBER', bg='moccasin', font='ArialBlack')
la2 = Label(win, text='BUS STOPS', bg='moccasin', font='ArialBlack')
la3 = Label(win, text='OTHER BUSES THAT GO THERE', bg='moccasin', font='ArialBlack')
e1 = Entry(win, width=30)
b1 = Button(win, text='SEARCH', bg='white', command=search)
begin()
win.mainloop()
   
