#GUI canvas with buttons

import tkinter
import tkinter.font

class MyGUI:
    def __init__(self):
        #main window set up
        self.main_window=tkinter.Tk()
        self.main_window.title('Canvas Demo')

        #set up canvas
        self.canvas = tkinter.Canvas(self.main_window, width = 300, height = 200)
        
        #frame set up
        self.button_frame = tkinter.Frame(self.main_window)


        #pack
        self.canvas.pack()
        self.button_frame.pack()

        #buttons, set to display in button frame
        self.btn_rect = tkinter.Button(self.button_frame, text = 'Rectangle',\
                                       command = self.displayRect)
        self.btn_oval = tkinter.Button(self.button_frame, text = 'Oval',\
                                       command = self.displayOval)
        self.btn_arc = tkinter.Button(self.button_frame, text = 'Arc',\
                                       command = self.displayArc)
        self.btn_poly = tkinter.Button(self.button_frame, text = 'Polygon',\
                                       command = self.displayPoly)
        self.btn_line = tkinter.Button(self.button_frame, text = 'Line',\
                                       command = self.displayLine)
        self.btn_txt = tkinter.Button(self.button_frame, text = 'Text',\
                                       command = self.displayTxt)
        self.btn_clear = tkinter.Button(self.button_frame, text = 'Clear',\
                                       command = self.displayClear)
        
        #pack in grid
        self.btn_rect.grid(row = 1, column = 1)
        self.btn_oval.grid(row = 1, column = 2)
        self.btn_arc.grid(row = 1, column = 3)
        self.btn_poly.grid(row = 1, column = 4)
        self.btn_line.grid(row = 1, column = 5)
        self.btn_txt.grid(row = 1, column = 6)
        self.btn_clear.grid(row = 1, column = 7)

        
        tkinter.mainloop()
        
    #button method definitions
    def displayRect(self):
        self.displayClear()
        self.canvas.create_rectangle(20, 20, 300, 200, fill = 'green', outline = 'red',\
                                       width = 5, tags = 'rect')
    def displayOval(self):
        self.displayClear()
        self.canvas.create_oval(20, 20, 280, 180, dash = (2, 2), fill = 'yellow',\
                                  outline = 'black', width = 2, tags = 'oval')
    def displayArc(self):
        self.displayClear()
        self.canvas.create_arc(30, 30, 250, 150, start = 45, extent = 30,\
                                     style=tkinter.PIESLICE, fill = 'red', tags = 'arc')
    def displayPoly(self):
        self.displayClear()
        self.canvas.create_polygon(80, 40, 120, 40, 160, 80, 160, 120,\
                                      120, 160, 80, 160, 40, 120, 40, 80, tags = 'polygon')
    def displayLine(self):
        self.displayClear()
        self.canvas.create_line(0,0, 299, 199, arrow=tkinter.BOTH, dash = (5,2), tags = 'line')
    def displayTxt(self):
        self.displayClear()
        myfont = tkinter.font.Font(family = 'Helvetica', size = 24, weight = 'bold')
        self.canvas.create_text(160, 100, text='Merry Christmas', font = myfont,\
                                   fill ='red', tags = 'text')
    def displayClear(self):
        #delete using tags
        self.canvas.delete('rect', 'oval', 'arc', 'polygon', 'line', 'text')

mycanvas = MyGUI()


            


        
