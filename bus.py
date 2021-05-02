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
