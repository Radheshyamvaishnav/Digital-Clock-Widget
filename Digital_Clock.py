from time import strftime
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Clock')
#Microsoft Himalaya


def time():
	string = strftime('%H:%M.%S  %p')
	string2 = strftime("%d %B, %Y")
	lbl.config(text = string)
	lbl1.config(text = string2)
	lbl.after(1000, time)  
	#lbl1.after(1000, time)  



lbl = Label(root, font = ('Ds-Digital', 120),	
			background= "#6D8299" ,
			foreground = '#A6F6F1',
			)

lbl1 = Label(root, font = ('Ds-Digital', 30),	
			background= "#6D8299" ,
			foreground = '#A6F6F1',
			)
lbl.pack(anchor = 'center')
lbl1.pack(fill = 'both')

root.attributes('-alpha',0.8)
root.wm_attributes('-transparentcolor', '#6D8299')

root.overrideredirect(True)
time()
mainloop()

