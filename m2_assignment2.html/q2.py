from tkinter import *
master = Tk() 
Label(master, text='First Name').grid(row=0) 
Label(master, text='Last Name').grid(row=1) 
e1 = Entry(master) 
e2 = Entry(master) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
mainloop()





from tkinter import *
  
root = Tk() 
frame = Frame(root) 
frame.pack() 
bottomframe = Frame(root) 
bottomframe.pack( side = BOTTOM ) 
redbutton = Button(frame, text = 'Red', fg ='red') 
redbutton.pack( side = LEFT) 
greenbutton = Button(frame, text = 'Brown', fg='brown') 
greenbutton.pack( side = LEFT ) 
bluebutton = Button(frame, text ='Blue', fg ='blue') 
bluebutton.pack( side = LEFT ) 
blackbutton = Button(bottomframe, text ='Black', fg ='black') 
blackbutton.pack( side = BOTTOM) 
root.mainloop()
