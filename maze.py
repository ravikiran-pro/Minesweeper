import tkinter
from random import randint
variable=[]
variable1=[]
Buttons=[]
row=8
col=8
bombs=10
def dummy_variable(row,col,bombs,values):
	axis=[]
	for i in range(row):
		joint=[]
		for j in range(col):
			joint.append('')
		values.append(joint)
	for i in range(bombs):
		rand=randint(0,row*col-1)
		while rand in axis:
			rand=randint(0,row*col-1)
		axis.append(rand)
	final=[]
	for i in axis:
		final.append([i//row,i%row])
	for i in range(len(final)):
		values[final[i][0]][final[i][1]]='B'
	for i in range(row):
		for j in range(col):
			if(values[i][j]!='B'):
				count=0
				try:
					if(values[i-1][j-1]=='B'):
						count+=1
					if(values[i-1][j]=='B'):
						count+=1
					if(values[i-1][j+1]=='B'):
						count+=1
					if(values[i][j-1]=='B'):
						count+1
					if(values[i][j+1]=='B'):
						count+=1
					if(values[i-1][j-1]=='B'):
						count+=1
					if(values[i+1][j]=='B'):
						count+=1
					if(values[i+1][j+1]=='B'):
						count+=1
				except:
					count=0
				values[i][j]=count
class Variable:
	def __init__(self,win,text):
		self.win=win
		self.text=text
	def create(self):
		self.var=tkinter.StringVar(self.win)
		self.var.set(self.text)
		return self.var

class Button:
	def __init__(self,win,var):
		self.win=win
		self.var=var
	def create(self,val):
		self.val=val
		self.button=tkinter.Button(win,textvariable=self.var,width=10,height=2,bg="silver",fg="red",command=lambda:match(self.val))
		self.button.bind('<Button-3>', lambda x:right(self.button))
		return self.button
def match(val):
	for i in range(row):
		for j in range(col):
			if variable1[i][j]==val:
				free(i,j)
				break
def right(event):
	event.config(background="green")
	
def free(i,j):
	if variable1[i][j].get()=='B':
		for i in range(row):
			for j in range(col):
				variable[i][j].set(variable1[i][j].get())
				if(variable1[i][j].get()=='B'):
					Buttons[i][j].configure(bg="black",fg="black")
				else:
					Buttons[i][j].configure(bg="red")
		tkinter.Label(text="game over",bg="white").grid(row=row//2,column=col//2)
	else:
		#sides
		k=j
		while True:
			if k is  -1 or variable1[i][k].get() is 'B':
				break
			else:
				variable[i][k].set(variable1[i][k].get())
				Buttons[i][k].configure(bg="white")
				k-=1


		k=j
		while True:
			if k is col or variable1[i][k].get() is 'B':
				break
			else:
				variable[i][k].set(variable1[i][k].get())
				Buttons[i][k].configure(bg="white")
				k+=1
		#slide	
		k=i	
		while True:
			if k is row or variable1[k][j].get() is 'B':
				break
			else:
				variable[k][j].set(variable1[k][j].get())
				Buttons[k][j].configure(bg="white")
				k+=1
		k=i
		while True:
			if k is -1 or variable1[k][j].get() is 'B':
				break
			else:
				variable[k][j].set(variable1[k][j].get())
				Buttons[k][j].configure(bg="white")
				k-=1
		#right diagonal
		l=i
		k=j
		while True:
			if k is -1 or l is -1 or variable1[l][k].get() is 'B':
				break
			else:
				variable[l][k].set(variable1[l][k].get())
				Buttons[l][k].configure(bg="white")
				k-=1
				l-=1
		l=i
		k=j
		while True:
			if k is col or l is row or variable1[l][k].get() is 'B':
				break
			else:
				variable[l][k].set(variable1[l][k].get())
				Buttons[l][k].configure(bg="white")
				k+=1
				l+=1
		l=i
		k=j
		while True:
			if k is -1 or l is row or variable1[l][k].get() is 'B':
				break
			else:
				variable[l][k].set(variable1[l][k].get())
				Buttons[l][k].configure(bg="white")
				k-=1
				l+=1
		l=i
		k=j
		while True:
			if k is -1 or l is row or variable1[k][l].get() is 'B':
				break
			else:
				variable[k][l].set(variable1[k][l].get())
				Buttons[k][l].configure(bg="white")
				k-=1
				l+=1
		count=0
		for i in range(row):
			for j in range(col):
				if(Buttons[i][j]["bg"]=="white"):
					count+=1
		if(count==row*col-bombs):
			tkinter.Label(text="You won",bg="red").grid(row=row//2,column=col//2)
win=tkinter.Tk()
win.config(background="white")
count=0
values=[]
dummy_variable(row,col,bombs,values)
for i in range(row):
	joint=[]
	for j in range(col):
		v=Variable(win,values[i][j])
		joint.append(v.create())
	variable1.append(joint)
for i in range(row):
	joint=[]
	for j in range(col):
		v=Variable(win," ")
		joint.append(v.create())
	variable.append(joint)
for i in range(row):
	joint=[]
	for j in range(col):
		but=Button(win,variable[i][j])
		button=but.create(variable1[i][j])
		joint.append(button)
	Buttons.append(joint)

for i in range(row):
	for j in range(col):
		Buttons[i][j].grid(row=i,column=j,padx=1,pady=1)	

win.mainloop()