from tkinter import Tk, Frame, Button,PhotoImage, Entry, Label
from tkinter import ttk

class MyGUI():

	def __init__(self, root, frame):
		self.root = root
		self.frame = frame
		self.root.title("FenixEFF")
		self.root.resizable(0,0)		
		self.root.iconbitmap("./icons/icon.ico")
		self.root.overrideredirect(True)
		self.frame.pack()

		# -----------  Events  -----------
		p_x = p_y = 0
		def posicion(event):
			global p_x
			global p_y
			p_x = event.x
			p_y = event.y

		def move_event(event):
			global p_x
			global p_y
			x = self.root.winfo_pointerx() - p_x
			y = self.root.winfo_pointery() - p_y
			self.root.geometry('+{x}+{y}'.format(x=x,y=y))
		
		def decoration(event):
			self.root.overrideredirect(True)


		def minimizeWindow():
			self.root.withdraw()
			self.root.overrideredirect(False)
			self.root.iconify()			

		self.root.bind('<Enter>', decoration)
		#  =================================
		#  =          NavBar               =
		#  =================================
		
		#----------  Load Icons  ----------				
		
		self.img = PhotoImage(file="./icons/folder.png")
		self.img2 = PhotoImage(file="./icons/convert.png")
		self.img3 = PhotoImage(file="./icons/save.png")
		self.img4 = PhotoImage(file="./icons/setting.png")
		self.img5 = PhotoImage(file="./icons/exit.png")
		self.img6 = PhotoImage(file="./icons/search.png")
		self.img7 = PhotoImage(file="./icons/logo.png")
		self.img8 = PhotoImage(file="./icons/preview.png")
		self.img9 = PhotoImage(file="./icons/fenix.png")
		self.img10 = PhotoImage(file="./icons/minimize.png")
		self.img11 = PhotoImage(file="./icons/close.png")

		#----------  End of Load Icons  ----------
		
		self.panel1 = Frame(frame)
		self.panel1.config(bg="#01011d", width="75", height="500")
		self.panel1.place(x=0, y=0)

		#----------  Button Icons  ----------
		
		self.bt1 = Button(self.panel1, image=self.img, width=64, height="64", activebackground="#01011d")
		self.bt1.config(bg="#01011d", bd=0, highlightthickness=0, relief='flat')
		self.bt1.place(x=5, y=10)
		self.bt2 = Button(self.panel1, image=self.img2, width=64, height="64", activebackground="#01011d")
		self.bt2.config(bg="#01011d", bd=0, highlightthickness=0, relief='flat')
		self.bt2.place(x=5, y=85)
		self.bt3 = Button(self.panel1, image=self.img3, width=64, height="64", activebackground="#01011d")
		self.bt3.config(bg="#01011d", bd=0, highlightthickness=0, relief='flat')
		self.bt3.place(x=5, y=160)
		self.bt4 = Button(self.panel1, image=self.img4, width=64, activebackground="#01011d")

		self.bt4.config(bg="#01011d", bd=0, highlightthickness=0, relief='flat')
		self.bt4.place(x=5, y=405)
		self.bt5 = Button(self.panel1, image=self.img5, width=64, activebackground="#01011d", command=lambda:root.destroy())
		self.bt5.config(bg="#01011d", bd=0, highlightthickness=0, relief='flat')
		self.bt5.place(x=5, y=450)

		#----------  End of Button Icons  ----------		

		#=====  End of NavBar  ======
		
		#  =================================
		#  =            Header Bar         =
		#  =================================

		# -----------  Parent container  -----------
		
		self.panel2 = Frame(frame)
		self.panel2.config(bg="#FCFCFC", width="725", height="45")
		self.panel2.place(x=75, y=0)
		self.panel2.bind('<Button-1>', posicion)
		self.panel2.bind('<B1-Motion>', move_event)
		# -----------  End of Parent container  -----------

		# -----------  Button Search  -----------	

		# Button
		self.bt6 = Button(self.panel2, image=self.img6, width=64, activebackground="#FCFCFC")
		self.bt6.config(bg="#FCFCFC", bd=0, highlightthickness=0, relief='flat')
		self.bt6.place(x=0, y=8)

		# Input search
		self.input_search = Entry(self.panel2, bd=0, highlightthickness=0, relief='flat', bg="#FCFCFC", width=30)
		self.input_search.place(x=60, y=12)

		# -----------  End of Button Search  -----------
		
		# -----------  Logo and Horizontal line  -----------
		
		# Logo User
		self.logo = Label(self.panel2, image=self.img7, width=48, height=46, bg="#FCFCFC")
		self.logo.place(x=525, y=0)
		self.logo_lb = Label(self.panel2, text="FenixEFF", bg="#FCFCFC", foreground="black", font=('Arial', 12))
		self.logo_lb.place(x=575, y=10)

		# close and minimize button
		self.bt9 = Button(self.panel2, image=self.img10, width=32, activebackground="#FCFCFC", command=lambda:minimizeWindow())
		self.bt9.config(bg="#FCFCFC", bd=0, highlightthickness=0, relief='flat')
		self.bt9.place(x=650, y=5)
		self.bt10 = Button(self.panel2, image=self.img11, width=32, activebackground="#FCFCFC", command=lambda:self.root.destroy())
		self.bt10.config(bg="#FCFCFC", bd=0, highlightthickness=0, relief='flat')
		self.bt10.place(x=680, y=5)


		# Horizontal linear
		self.input_label = Frame(self.panel2, bg="#01011d", height=3, width=195)
		self.input_label.place(x=60, y=32)

		# ----------- End of Logo and Horizontal line  -----------

		#=====  End of Header Bar  ======

		# ==================================
		# =           Footer Bar           =
		# ==================================
		
		# -----------  Parent container  -----------
		
		self.panel3 = Frame(frame)
		self.panel3.config(bg="#002160", width="725", height="455")
		self.panel3.place(x=75, y=45)

		# ----------- End of Parent container  -----------

		# -----------  Container 1  -----------
		
		self.subpanel1 = Frame(self.panel3, width="725", height="120", bg="#E1EBED")
		self.subpanel1.place(x=0, y=0)

		self.label_efect= Label(self.subpanel1, text="Welcome to the Fenix Effect program", font=('Arial', 22), bg="#E1EBED", foreground="black")
		self.label_efect.place(x=10, y=15)

		self.logo_img2 = Label(self.subpanel1, image=self.img9, width=229, bg="#E1EBED")
		self.logo_img2.place(x=510, y=0)

		self.label_comment= Label(self.subpanel1, text="APPLY AN EFFECT TO ANY IMAGE AND CHANGE ITS RESOLUTION", font=('Arial', 8, 'bold'), bg="#E1EBED", foreground="black")
		self.label_comment.place(x=10, y=55)

		# ----------- End of Container 1  -----------

		# -----------  Container 2  -----------
		self.subpanel2 = Frame(self.panel3, width="225", height="140", bg="#012770")
		self.subpanel2.place(x=10, y=135)

		self.label1= Label(self.subpanel2, text="1.- Load the image and \nselect the effect", font=('Arial', 10, 'bold'), bg="#012770", foreground="white")
		self.label1.place(x=10, y=15)

		self.label_img = Label(self.subpanel2, image=self.img, width=48, height=48, bg="#012770")
		self.label_img.place(x=75, y=65)

		# ----------- End of Container 2  -----------

		# -----------  Container 3  -----------

		self.subpanel3 = Frame(self.panel3, width="225", height="140", bg="#012770")
		self.subpanel3.place(x=250, y=135)
		self.label2= Label(self.subpanel3, text="2.- Convert the image with \nthe selected effect and resolution", font=('Arial', 10, 'bold'), bg="#012770", foreground="white")
		self.label2.place(x=10, y=15)
		self.label_img2 = Label(self.subpanel3, image=self.img2, width=48, height=48, bg="#012770")
		self.label_img2.place(x=75, y=65)

		# ----------- End of Container 3  -----------

		# -----------  Container 4  -----------

		self.subpanel4 = Frame(self.panel3, width="225", height="140", bg="#012770")
		self.subpanel4.place(x=490, y=135)
		self.label3= Label(self.subpanel4, text="3.- Save the image", font=('Arial', 10, 'bold'), bg="#012770", foreground="white")
		self.label3.place(x=10, y=15)
		self.label_img3 = Label(self.subpanel4, image=self.img3, width=48, height=48, bg="#012770")
		self.label_img3.place(x=75, y=65)

		# ----------- End of Container 4  -----------

		# -----------  Panel Effect  -----------
		
		self.subpanel5 = Frame(self.panel3, width="705", height="55", bg="#012770")
		self.subpanel5.place(x=10, y=295)
		self.list= Label(self.subpanel5, text="Select Effect:", font=('Arial', 12, 'bold'), bg="#012770", foreground="white")
		self.list.place(x=10, y=15)

		# Drop-down List 
		self.combo = ttk.Combobox(self.subpanel5, width=50, state="readonly")
		self.combo.place(x=125, y=15)
		self.combo["values"] = ["GRAYSCALE", "BLUR", "CONTOUR", "DETAIL", "EDGE ENHANCE", "EMBOSS", "FIND EDGES"  , "SHARPEN" , "SMOOTH"]

		# ----------- End of Panel Effect  -----------

		self.subpanel6 = Frame(self.panel3, width="705", height="55", bg="#012770")
		self.subpanel6.place(x=10, y=365)

		self.label_resolt= Label(self.subpanel6, text="Resolution:", font=('Arial', 12, 'bold'), bg="#012770", foreground="white")
		self.label_resolt.place(x=10, y=15)

		# Drop-down List 
		self.combo1 = ttk.Combobox(self.subpanel6, width=25, state="readonly")
		self.combo1.place(x=125, y=15)
		self.combo1["values"] = ["DEFAULT",72 , 96, 300]

		self.label_preview= Label(self.subpanel6, text="Image preview", font=('Arial', 12, 'bold'), bg="#012770", foreground="white")
		self.label_preview.place(x=475, y=15)
		self.bt8 = Button(self.subpanel6, image=self.img8, width=48, height="48", activebackground="#012770")
		self.bt8.config(bg="#012770", bd=0, highlightthickness=0, relief='flat')
		self.bt8.place(x=600, y=3)


		# ======  End of Footer Bar  =======
		

if __name__=='__main__':
	root = Tk()
	frm = Frame(root, width="800", height="500")
	gui = MyGUI(root, frm)
	root.mainloop()