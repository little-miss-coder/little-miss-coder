#ex table GUI

import tkinter
import random

ROWS = 2
COLS = 3

class MyTable:
    def __init__(self):
        #main window
        self.main_window = tkinter.Tk()

        #create rows
        self.labelR = []
        for i in range(ROWS):
            self.labelR.append([]) #append new item
            self.labelR[i] = tkinter.Label(self.main_window, width = 10,\
                                           text = f'Row {i+1}')
            #use grid to pack and make visible
            self.labelR[i].grid(row= i+1, column = 0)
            

        #create columns
        self.labelC = []
        for i in range(COLS):
            self.labelC.append([])
            self.labelC[i] = tkinter.Label(self.main_window, width = 10,\
                                           text = f'Column {i+1}')
            self.labelC[i].grid(row = 0, column = i+1)


        #initialize cells using cols and rows
        self.cells = [[0]*COLS]*ROWS

        #create stringVar 
        self.vars = []
        for r in range(ROWS):
            self.vars.append([])  #add new row
            for c in range(COLS):
                self.vars[r].append([]) #add new element in row
                self.vars[r][c] = tkinter.StringVar() #add as string var
                self.vars[r][c].set(self.cells[r][c]) #set it to cells

        #create entries
        self.entry = []
        for r in range(ROWS):
            self.entry.append([])
            for c in range(COLS):
                self.entry[r].append([])
                #set using text variable equal to vars [r][c]
                self.entry[r][c] = tkinter.Entry(self.main_window, width = 10,\
                                                 textvariable = self.vars[r][c])
                #make visible using grid
                self.entry[r][c].grid(row = r+1, column = c+1)

        #button
        self.mt_btn = tkinter.Button(self.main_window, text = 'Make Table',\
                                     command = self.makeTable)
        #for grid placement, it is in the lst row, and middle column.
        self.mt_btn.grid(row = ROWS+1, column = int(COLS/2 +1))


        tkinter.mainloop()


    #def make table function
    #will get random numbers and save to cells
    def makeTable(self):
        for r in range(ROWS):
            for c in range(COLS):
                self.cells[r][c] = random.randint(1, 100)
                self.vars[r][c].set(self.cells[r][c])

mygui = MyTable()
