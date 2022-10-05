import tkinter
import tkinter.messagebox

class Exercise: 

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('750x300')
        self.main_window.title('Class EC Exercise')

        self.topframe = tkinter.Frame(self.main_window)
        self.middleframe1 = tkinter.Frame(self.main_window)
        self.middleframe2 = tkinter.Frame(self.main_window)
        self.averageframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.topframe, text = 'Enter the score for test 1:')
        self.label2 = tkinter.Label(self.middleframe1, text = 'Enter the score for test 2:')
        self.label3 = tkinter.Label(self.middleframe2, text = 'Enter the score for test 3:')

        self.entry1 = tkinter.Entry(self.topframe, width = 10)
        self.entry2 = tkinter.Entry(self.middleframe1, width = 10)
        self.entry3 = tkinter.Entry(self.middleframe2, width = 10)

        self.label1.pack(side = 'left')
        self.entry1.pack(side = 'right')

        self.label2.pack(side = 'left')
        self.entry2.pack(side = 'right')

        self.label3.pack(side = 'left')
        self.entry3.pack(side = 'right')



        self.topframe.pack()
        self.middleframe1.pack()
        self.middleframe2.pack()
        self.bottomframe.pack()

        self.avgbutton = tkinter.Button(self.main_window, text = 'Average', command=self.average)
        self.quitbutton = tkinter.Button(self.main_window,text = 'Quit', command=self.main_window.destroy)

        self.avgbutton.pack(side = 'left')
        self.quitbutton.pack(side = 'right')

        tkinter.mainloop()

    def average(self):

        value1 = float(self.entry1.get())
        value2 = float(self.entry2.get())
        value3 = float(self.entry3.get())

        average = round((value1 + value2 + value3) / 3)

        
        self.average.set(average)
        #tkinter.messagebox.showinfo('Average Scores', str(average))

my_exercise = Exercise()


