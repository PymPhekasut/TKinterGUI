# Expense.py

from tkinter import *
from tkinter import ttk #theme of tk
#tkinter is library to create GUI

import csv
from datetime import datetime

#record data into csv file

def WriteCSV(data):
	# 'a' is append, 'w' is replace
	dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #strftime.org
	data.insert(0,dt) #insert time when message is recorded
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) #fw is file writer
		fw.writerow(data)
	print('Done!')

def ReadCSV():
	with open('data.csv',newline='',encoding='utf-8') as file:
		fr = csv.reader(file) #file reader
		data = list(fr)

	return data

#######################################


GUI = Tk() #main window of program
GUI.geometry('800x600') #size
GUI.title('MoneyCal')

FONT1 = (None,15)
FONT2 = ('Century Gothic',15,'bold')
FONT3 = ('Candara',15)

########################################


F1 = Frame(GUI)
F1.place(x=50,y=50)

#Label 1
L1 = ttk.Label(F1,text='Expense list',font=FONT2)
L1.pack(pady=5) #gap btw each 5 pixels

#text box1
v_namelist = StringVar() #stringVar is the variable using with only GUI
E1 = ttk.Entry(F1,textvariable=v_namelist,font=FONT3)
E1.pack(pady=5)


########################################
#Label 2
L2 = ttk.Label(F1,text='Expense (AUD)',font=FONT2)
L2.pack(pady=5) #gap btw each 5 pixels

#text box1
v_price = StringVar() #stringVar is the variable using in GUI only
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT3)
E2.pack(pady=5)


#########################################
def UpdateData():
	try: #check error
		alldata = ReadCSV()
		textshow = ''
		alldata.reverse() #reverse recent data into the front
		allprice = []
		for dt in alldata[:10]:
			textshow = textshow + '{} - {} - {}\n'.format(dt[0],dt[1],dt[2])
			allprice.append(int(dt[2]))
		v_history.set(textshow)
		v_summary.set('{:,.2f}'.format(sum(allprice)))
	except:
		v_history.set('-----NO DATA-----')


def SaveData(event=None):
	namelist = v_namelist.get() #.get() data from textbox or v_namelist
	price = v_price.get()
	textshow = 'expense: {} price: {} AUD'.format(namelist,price)
	v_result.set(textshow) 
	product = [namelist,price]
	WriteCSV(product)
	#clear data
	v_namelist.set('')
	v_price.set('')
	E1.focus() #move cursor 
	UpdateData()

E2.bind('<Return>',SaveData) #SaveData(event=None)





#create button from ttk ttk.py 
B1 = ttk.Button(F1,text='Save',command=SaveData) #get data from function SaveData
B1.pack(ipadx=20,ipady=10,pady=5)

########################################

v_result = StringVar()
v_result.set('----------RESULT-----------')
R1 = ttk.Label(F1,textvariable=v_result,font=FONT2,foreground='green')
R1.pack()

##################RIGHT SIDE######################
L1 = ttk.Label(GUI,text='Expense History',font=FONT2)
L1.place(x=450,y=50)

v_history = StringVar()
v_history.set('----------RESULT-----------')
R2 = ttk.Label(GUI,textvariable=v_history,font=FONT2,foreground='green')
R2.place(x=450,y=100)


##################RIGHT SIDE######################
L1 = ttk.Label(GUI,text='-------Total Expense------',font=FONT2)
L1.place(x=60,y=300)

v_summary = StringVar()
v_summary.set('0.00')
R3 = ttk.Label(GUI,textvariable=v_summary,font=FONT2,foreground='green')
R3.place(x=60,y=350)



UpdateData() #Update 10 recent list when open program

GUI.mainloop()