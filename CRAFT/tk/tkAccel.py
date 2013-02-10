'''
Created on 9 Feb 2013

@author: jamie
'''

from Tkinter import Tk, Text, BOTH, W, N, E, S
from ttk import Frame, Button, Label, Style


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()

    def initUI(self):
      
        self.parent.title("MPU6050 Accelerometer")
        t = Text(self, width=40, height=10)





def main():
  
    root = Tk()
    root.geometry("350x300+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  