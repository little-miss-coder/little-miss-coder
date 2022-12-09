#GUI entries
#using label to display instead of dialog box

import tkinter
import tkinter.messagebox

class KiloConvertGUI:
    def __init__(self):
        #main window set up
        self.main_window = tkinter.Tk()
        self.main_window.title('Conversion')
        self.main_window.geometry('300x300')

        #frames set up
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #attributes set up
        self.prompt_label = tkinter.Label(self.top_frame, \
                                          text = "Enter a distance in kilometers: ")

        self.kilo_entry = tkinter.Entry(self.top_frame, width = 10)

        self.desc_label = tkinter.Label(self.mid_frame, text = "Converted to miles: ")

        #result label using text variable and self.value
        self.value = tkinter.StringVar()
        self.result_label = tkinter.Label(self.mid_frame, textvariable = self.value)

        self.conv_button = tkinter.Button(self.bottom_frame, \
                                          text = "Covert", command = self.convert)

        self.quit_button = tkinter.Button(self.bottom_frame, \
                                          text = "Quit", command = self.main_window.destroy)

        #pack items in top frame
        self.prompt_label.pack(side = 'left')
        self.kilo_entry.pack(side = 'left')
        #pack items in mid frame
        self.desc_label.pack(side = 'left')
        self.result_label.pack(side = 'left')
        #pack items in bottom frame
        self.conv_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')
        #pack frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()


        #main loop
        tkinter.mainloop()

    #create convert function
    def convert(self):
        #1 km = 0.6124 miles
        #use .get() to get result in string format, add float to convert
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.6124

        #set miles to self.value, must be string
        self.value.set(f'{miles:.2f}')


#call gui
my_gui = KiloConvertGUI()
        
