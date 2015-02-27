from Tkinter import Tk, Label, BOTH, RIGHT, RAISED, IntVar
from Tkinter import N, E, S, W, StringVar, Listbox, END, LEFT, Radiobutton
from Tkinter import SUNKEN
from ttk import Frame, Style, Button
import random
import Tkinter as tk

class Example(Frame):
  
  def __init__(self, parent):
    Frame.__init__(self, parent)   
     
    self.parent = parent
    
    self.initUI()
    self.centerWindow()
    

    
  
  def initUI(self):
    
    self.parent.title("Kenneth's Game")
    self.pack(fill=BOTH, expand=1)
    style = Style()
    style.configure("TFrame", background="grey")

    closeButton = Button(self, text="Close", command=self.destroy)
    closeButton.place(x=479, y=345)
    okButton = Button(self, text="OK", command=self.ClickOK)
    okButton.place(x=400, y=345)


    self.choice = StringVar()
    self.button1 = Radiobutton(self, text="Rock       ", value =1, variable=self.choice,
                               fg = "blue", font="bold", relief=RAISED, command=self.Selection)
    self.button1.place(x=40, y=250)

    self.button2 = Radiobutton(self, text="Paper     ", value =2, variable=self.choice,
                               fg = "blue", font="bold", relief=RAISED, command=self.Selection)
    self.button2.place(x=40, y=280)

    self.button3 = Radiobutton(self, text="Scissors ", value =3, variable=self.choice,
                               fg = "blue", font="bold", relief=RAISED, command=self.Selection)
    self.button3.place(x=40, y=310)
    
    
    
    self.vsLabel = tk.Label(self,text="VS", bg ="yellow", fg = "black", font = "Verdana 18 bold",
                             relief=SUNKEN)
    self.vsLabel.place(x=280, y=130)

   
# Match result
    self.result = StringVar()
    self.resultDisplay = tk.Label(self, text=0, textvariable=self.result, relief=RAISED,bg='white',
                             font = "Arial 20 bold" )
#    self.cpu2label.place(x=275, y=100)

#CPU choice display
    self.cpuDisplay = StringVar()
    self.cpuDisplaylabel = tk.Label(self, text=0, textvariable=self.cpuDisplay, bg='white',fg='red',
                                    relief=RAISED, font = "Arial 14 bold")
#    self.cpuDisplaylabel.place(x=500, y=200)


    
# Score    
    self.scoreDisplay1 = tk.Label(self, text=0, font = "Arial 35 bold",
                                     relief=RAISED, bg='blue', fg='white')
    self.scoreDisplay1.place(x=20, y=20)

    
    self.scoreDisplay2 = tk.Label(self, text=0, font = "Arial 35 bold",
                                     relief=RAISED, bg='red', fg='white')
    self.scoreDisplay2.place(x=540, y=20)

# Initializing score
    self.UserScore = 0
    self.cpuScore =  0

    

  def Selection(self):

    if int(self.choice.get()) == 1:
      self.select ="Rock"
      self.display1 = tk.Label(self, text="Rock      ",bg='white',fg='blue',
                               font = "Arial 14 bold")
      self.display1.place(x=50, y=200)
    elif int(self.choice.get()) == 2:
      self.select ="Paper"
      self.display1 = tk.Label(self, text="Paper      ",bg='white',fg='blue',
                               font = "Arial 14 bold")
      self.display1.place(x=50, y=200)    
    elif int(self.choice.get()) == 3:
      self.select ="Scissors"
      self.display1 = tk.Label(self, text="Scissors",bg='white',fg='blue',
                               font = "Arial 14 bold")
      self.display1.place(x=50, y=200)
    else:
      pass
    
  def centerWindow(self):    
    w = 600
    h = 400

    sw = self.parent.winfo_screenwidth()
    sh = self.parent.winfo_screenheight()
    
    x = (sw - w)/2
    y = (sh - h)/2
    self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

  def ClickOK(self):
    
    cpuList = ['Rock', 'Paper', 'Scissors', 'Rock', 'Paper', 'Scissors',
               'Rock', 'Paper', 'Scissors']
    cpuSelect1 = random.choice(cpuList) # computer random selection

    self.cpuDisplay.set(cpuSelect1)


    if self.select == 'Rock' and cpuSelect1 == 'Scissors':
      self.result.set("Rock wins")
      self.UserScore = self.UserScore + 1

    elif self.select == 'Rock' and cpuSelect1 == 'Rock':
      self.result.set("    Draw    ")
    elif self.select == 'Rock' and cpuSelect1 == 'Paper':
      self.result.set("Paper wins")
      self.cpuScore =  self.cpuScore + 1


    elif self.select == 'Paper' and cpuSelect1 == 'Rock':
      self.result.set("Paper wins")
      self.UserScore = self.UserScore + 1
    elif self.select == 'Paper' and cpuSelect1 == 'Paper':
      self.result.set("    Draw    ")
    elif self.select == 'Paper' and cpuSelect1 == 'Scissors':
      self.result.set("Scissors win")
      self.cpuScore =  self.cpuScore + 1

    elif self.select == 'Scissors' and cpuSelect1 == 'Paper':
      self.result.set("Scissors win")
      self.UserScore = self.UserScore + 1
    if self.select == 'Scissors' and cpuSelect1 == 'Scissors':
      self.result.set("    Draw    ")
    elif self.select == 'Scissors' and cpuSelect1 == 'Rock':
      self.result.set("Rock wins")
      self.cpuScore =  self.cpuScore + 1
    else:
      pass



    self.scoreDisplay1 = tk.Label(self, text=self.UserScore , font = "Arial 35 bold",
                                     relief=RAISED, bg='blue', fg='white')
    self.scoreDisplay1.place(x=20, y=20)

    
    self.scoreDisplay2 = tk.Label(self, text=self.cpuScore, font = "Arial 35 bold",
                                     relief=RAISED, bg='red', fg='white')
    self.scoreDisplay2.place(x=540, y=20)

    self.cpuDisplaylabel.place(x=500, y=200)# CPU choice display
    self.resultDisplay.place(x=235, y=85) # Match result display


    if self.UserScore == 10:
      self.gameresult = "GAME OVER \n BLUE WINS"
      self.gameresultDisplay = tk.Label(self, text=self.gameresult, relief=RAISED,bg='white',
                             fg='blue', font = "Arial 20 bold" )
      self.gameresultDisplay.place(x=235, y=250)

      okButton = Button(self, text="OK")
      okButton.place(x=400, y=345)
      
    elif self.cpuScore == 10:
      self.gameresult = "GAME OVER \n RED WINS"
      self.gameresultDisplay = tk.Label(self, text=self.gameresult, relief=RAISED,bg='white',
                             fg='red', font = "Arial 20 bold" )
      self.gameresultDisplay.place(x=235, y=250)

      okButton = Button(self, text="OK")
      okButton.place(x=400, y=345)
    else:
      pass
      
  

    
def main():
  
  root = Tk()
  root.geometry("600x400+300+300")
  app = Example(root)
  root.mainloop()  


if __name__ == '__main__':
  main()
