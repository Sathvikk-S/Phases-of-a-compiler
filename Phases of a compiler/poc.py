import sys
import shlex
import csv
import tkinter as tk
import keyword
from infix import PostfixResult
from tkinter import *
from tkinter import filedialog as fd 

#GUI Implementation
def GUI():
	global output,win
	win=tk.Tk()	
	win.configure(background="gray")
	win.title("Phases Of Compiler")
	win.geometry("1300x650")
	# win.resizable(False,False)
	label=tk.Label(win,text="Phases Of Compiler")
	label.config(font=("Arial",20),background="gray")
	label.pack()
	
	InputBtn=tk.Button(win,width="20",text="Open Input File",command=lambda:GetFiles(1)).place(x=50,y=100)
	GrammarBtn=tk.Button(win,width="20",text="Open Grammar File",command=lambda:GetFiles(2)).place(x=50,y=150)
	TableBtn=tk.Button(win,width="20",text="Open Table File",command=lambda:GetFiles(3)).place(x=50,y=200)
	SubmitBtn=tk.Button(win,width="20",text="Submit",command=ShowOutput).place(x=50,y=250)
	win.mainloop()
	

#Show Output
def ShowOutput():
	frame=tk.Frame(win,bd=3,background="gray")
	tk.Label(win,text="Parsed Strings",font=("Arial",15),background="gray").place(x=250,y=70)
	scrollx=tk.Scrollbar(frame,orient=HORIZONTAL)
	scrolly=tk.Scrollbar(frame)
	LB=tk.Listbox(frame,font=(40),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set,width=30)
	scrollx.config(command=LB.xview)
	scrollx.pack(side=BOTTOM,fill=X)
	scrolly.config(command=LB.yview)
	scrolly.pack(side=RIGHT,fill=Y)
	frame.place(x=250,y=100)
	LB.pack()
	rows=open(InputFile,'r')
	for j,i in enumerate(rows):
		try:
			LB.insert(j,"{0:40}{1}".format(i,main(i)))
				
		except:
			LB.insert(j,"{0:38}Rejected".format(i))
	
	Tokenization() 
	OperatorCodeGeneration() 
	CodeGeneration()  
	Semantic() 

#Lexical Analysis Symbol Table
def Tokenization():
	frame=tk.Frame(win,bd=3,background="gray")
	LB=Listbox(frame,font=("Arial",40),background="gray")
	tk.Label(win,text="Tokens",font=("Arial",15),background="gray").place(x=950,y=70)
	scrollx=tk.Scrollbar(frame,orient=HORIZONTAL)
	scrolly=tk.Scrollbar(frame)
	LB=tk.Listbox(frame,font=(40),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set,width=30)
	scrollx.config(command=LB.xview)
	scrollx.pack(side=BOTTOM,fill=X)
	scrolly.config(command=LB.yview)
	scrolly.pack(side=RIGHT,fill=Y)
	frame.place(x=950,y=100)
	LB.pack()
	Reserved=keyword.kwlist
	Operators=["*","%","/","+","-","<",">","==","<=",">=","="]
	Identifers=[]
	Tokens=open(InputFile,'r')	
	Inserted=[]	
	LB.insert(END,"{0:30}{1}".format("Lexeme","Token"))
	for j in Tokens:
		for i in j:
			i=i.strip()
			if  i.isnumeric() and i not in Inserted:
				LB.insert(END,"{0:40}{1}".format(i,"number"))
				Inserted.append(i)		
			if i in Reserved and i not in Inserted:
				LB.insert(END,"{0:40}{1}".format(i,i))
				Inserted.append(i)
			elif i in Operators and i not in Inserted:
				LB.insert(END,"{0:40}{1}".format(i,"relation"))
				Inserted.append(i)
			elif i not in Inserted  and len(i)>0:
				LB.insert(END,"{0:40}{1}".format(i,"id"))	
				Identifers.append(i)				
				Inserted.append(i)
	SymbolTable(Identifers)

#Symbol Table
def SymbolTable(identifers):
	frame=tk.Frame(win,bd=3,background="gray")
	LB=Listbox(frame,font=("Arial",40),background="gray")
	tk.Label(win,text="Symbol Table",font=("Arial",15),background="gray").place(x=600,y=70)
	scrollx=tk.Scrollbar(frame,orient=HORIZONTAL)
	scrolly=tk.Scrollbar(frame)
	LB=tk.Listbox(frame,font=(40),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set,width=30)
	scrollx.config(command=LB.xview)
	scrollx.pack(side=BOTTOM,fill=X)
	scrolly.config(command=LB.yview)
	scrolly.pack(side=RIGHT,fill=Y)
	frame.place(x=600,y=100)
	LB.pack()
	LB.insert(END,'{0:<10} {1:>8} {2:>8}'.format("Symbol","Type","Scope"))

	for i in identifers:
		typeval=""
		if i.isnumeric():
			typeval="int"
		else:
			typeval="string"
		LB.insert(END,'{0:<10} {1:>15} {2:>11}'.format(i,typeval,"global"))
		
	

#Machine Code Generation
def CodeGeneration():	
	frame=tk.Frame(win,bd=3,background="gray")
	tk.Label(win,text="Machine Code Generation",font=("Arial",15),background="gray").place(x=250,y=320)
	scrollx=tk.Scrollbar(frame,orient=HORIZONTAL)
	scrolly=tk.Scrollbar(frame)
	LB=tk.Listbox(frame,font=(40),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set,width=30)
	scrollx.config(command=LB.xview)
	scrollx.pack(side=BOTTOM,fill=X)
	scrolly.config(command=LB.yview)
	scrolly.pack(side=RIGHT,fill=Y)
	frame.place(x=250,y=360)
	LB.pack()
	rows=open(InputFile,'r')					
	for i in rows:
		LB.insert(END,''.join(format(ord(x), 'b') for x in i))
	

#code operator generation
def OperatorCodeGeneration():
	frame=tk.Frame(win,bd=3,background="gray")
	tk.Label(win,text="Mathemtical Expression Generation",font=("Arial",15),background="gray").place(x=950,y=320)
	scrollx=tk.Scrollbar(frame,orient=HORIZONTAL)
	scrolly=tk.Scrollbar(frame)
	LB=tk.Listbox(frame,font=(40),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set,width=30)
	scrollx.config(command=LB.xview)
	scrollx.pack(side=BOTTOM,fill=X)
	scrolly.config(command=LB.yview)
	scrolly.pack(side=RIGHT,fill=Y)
	frame.place(x=950,y=360)
	LB.pack()
	rows=open(InputFile,'r')					
	for i in rows:
		i=i.replace("*","x")
		i=i.replace("/","\u00f7")
		LB.insert(END,i)
	
		 
	

# Semantic Analysis
def Semantic():
	frame=tk.Frame(win,bd=3,background="gray")
	tk.Label(win,text="Semantic Analysis",font=("Arial",15),background="gray").place(x=600,y=320)
	scrollx=tk.Scrollbar(frame,orient=HORIZONTAL)
	scrolly=tk.Scrollbar(frame)
	LB=tk.Listbox(frame,font=(40),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set,width=30)
	scrollx.config(command=LB.xview)
	scrollx.pack(side=BOTTOM,fill=X)
	scrolly.config(command=LB.yview)
	scrolly.pack(side=RIGHT,fill=Y)
	frame.place(x=600,y=360)
	LB.pack()
	rows=open(InputFile,'r')
	try:
		for i in rows:
			for j in i:
				if j.isnumeric()==False:
					continue		
			result=PostfixResult(i)
			if len(result)==1:
				LB.insert(END,result)		

	except:
		if LB.size()==0:
			LB.insert(END,"Semantically incorrect input")


#Opening Files Method
def GetFiles(i):
	if i==1 :
		global InputFile
		InputFile=fd.askopenfilename(filetypes=[("text file", "*.txt")],
                    title = "Select Input File" )
	if i==2:
		global GrammarFile
		GrammarFile=fd.askopenfilename(filetypes=[("text file", "*.txt")],
                    title = "Select Grammar File" )
	if i==3:
		global TableFile
		TableFile=fd.askopenfilename(filetypes=[("csv", "*.csv")],
                    title = "Select Parsing Table File" )
    


#Syntax Analyzer Parser
def main(input_string):	
	input_ind = list(shlex.shlex(input_string))
	input_ind.append('$')
	master = {}
	master_list = []
	new_list = []
	non_terminals = []
	grammar = open(GrammarFile, 'r')
	
	for row2 in grammar:
		
		if '->' in row2:
			#new production
			if len(new_list) == 0:
				start_state = row2[0]
				non_terminals.append(row2[0])
				new_list = []
				new_list.append(row2.rstrip('\n'))
			else:
				master_list.append(new_list)
				del new_list
				new_list = []
				new_list.append(row2.rstrip('\n'))
				non_terminals.append(row2[0])
				
		
		elif '|' in row2:
			new_list.append(row2.rstrip('\n'))	
	
	master_list.append(new_list)
	
	
	for x in range(len(master_list)):
		for y in range(len(master_list[x])):
			master_list[x][y] = [s.replace('|', '') for s in master_list[x][y]]
			master_list[x][y] = ''.join(master_list[x][y])
			master[master_list[x][y]] = non_terminals[x] 
	for key, value in master.items():
		if '->' in key:
			length = len(key)
			for i in range(length):
				if key[i] == '-' and key[i + 1] == ">":
					index =  i+2
					break
			var_key = key
			new_key = key[index:]
	
	
	var = master[var_key]
	del master[var_key]
	master[new_key] = var	
	order_table = []
	with open(TableFile, 'r') as file2:
		order = csv.reader(file2)

		for row in order:
			order_table.append(row)
	
	operators = order_table[0]
	stack = []

	stack.append('$') 
	
	vlaag = 1
	while vlaag:
		if input_ind[0] == '$' and len(stack)==2:
			vlaag = 0

		length = len(input_ind)

		buffer_inp = input_ind[0] 
		temp1 = operators.index(str(buffer_inp))
		# print "stack",stack, stack[-1]
		if stack[-1] in non_terminals:
			buffer_stack = stack[-2]
		else:
			buffer_stack = stack[-1]
		

		temp2 = operators.index(str(buffer_stack))
		#print buffer_inp, buffer_stack
					
		precedence = order_table[temp2][temp1]
			
		if precedence == '<':
			action = 'shift'
		elif precedence == '>':
			action = 'reduce'
				
		# print stack, "\t\t", input_ind, "\t\t", precedence, "\t\t", action, "\n"
		
		if action == 'shift':
			stack.append(buffer_inp)
			input_ind.remove(buffer_inp)
		elif action == 'reduce':
			for key, value in master.items():
				var1 = ''.join(stack[-1:])
				var2 = ''.join(stack[-3:])

				if str(key) == str(buffer_stack):	
					stack[-1] = value
					break
				elif key == var1 or stack[-3:]==list(var1):
					stack[-3:] = value
					break
				elif key == var2:
					stack[-3:] = value	
		del buffer_inp, temp1, buffer_stack, temp2, precedence
		
		if vlaag == 0:
			return "Accepted"
			
			
	
	
if __name__ == "__main__":
	# sys.exit(main())
	GUI()
