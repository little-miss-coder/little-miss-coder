#recursive sierpinkski triangle

import tkinter
class STriangle:
    def __init__(self):
        #main set up
        self.main_window = tkinter.Tk()
        self.width = 200
        self.height = 200

        #canvas set up
        self.canvas = tkinter.Canvas(self.main_window, width = self.width,\
                                     height = self.height)
        self.canvas.pack()

        #frame set up
        self.frame = tkinter.Frame(self.main_window)
        self.frame.pack()

        #label, order, and button in frame
        self.label = tkinter.Label(self.frame, text = 'Enter an order: ')
        self.order = tkinter.StringVar()
        self.entry = tkinter.Entry(self.frame, textvariable = self.order, justify = 'right')
        self.btn = tkinter.Button(self.frame, text = 'Display Triangle',\
                                  command = self.displayCanvas)

        #pack into frame
        self.label.pack(side = 'left')
        self.entry.pack(side = 'left')
        self.btn.pack(side = 'left')

        self.main_window.mainloop()


    def displayTriangle(self, order, p1, p2, p3):
        #base case
        if order == 0: 
            self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1], p1[0], p1[1],\
                                    tags = 'line')
        #recursive case
        else:
            p12 = self.findMidpoint(p1, p2)
            p23 = self.findMidpoint(p2, p3)
            p31 = self.findMidpoint(p3, p1)

            self.displayTriangle(order-1, p1, p12, p31)
            self.displayTriangle(order-1, p12, p2, p23)
            self.displayTriangle(order-1, p31, p23, p3)


    def findMidpoint(self, p1, p2):
        p = [0, 0]

        p[0] = (p1[0] + p2[0])/2
        p[1] = (p1[1] + p2[1])/2

        return p

    def displayCanvas(self):
        #first delete any old triangles
        self.canvas.delete('line')
        p1 = [self.width/2, 10]
        p2 = [10, self.height-10]
        p3 = [self.width-10, self.height-10]

        self.displayTriangle(int(self.order.get()), p1, p2, p3)
        

if __name__ == '__main__':
    my_triangle = STriangle()
        
