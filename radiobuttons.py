import tkinter
import tkinter.messagebox

class myGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
#Radio buttons are mutually exclusive, you can only select one at a time
        self.rb1 = tkinter.Radiobutton(self.topframe, text = 'Option 1', variable = self.radio_var, value = 10)
        self.rb2 = tkinter.Radiobutton(self.topframe, text = 'Option 2', variable = self.radio_var, value = 20)
        self.rb3 = tkinter.Radiobutton(self.topframe, text = 'Option 3', variable = self.radio_var, value = 30)

        self.rb2.select()
            #This automatically selects a dfault option in the GUI output

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
 
        self.topframe.pack(side = 'top')
        self.bottomframe.pack(side = 'top')

        self.mybutton = tkinter.Button(self.main_window, text='Click Me!', command=self.do_something)
        self.quitbutton = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)
        
        self.mybutton.pack(side='left')
        self.quitbutton.pack(side='right')

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Selection', 'The value is ' + str(self.radio_var.get()))

my_gui = myGUI()

print("I am done.")