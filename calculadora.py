from tkinter import *
calcu = Tk()
calcu.title("calculadora perrona")

e = 0

#funciones 
def click_boton(valor):
   global e
   et.insert(e,valor)
   e += 1 
def borrar():
    et.delete(0,END)
    e = 0

def resultado():
   ecuacion = et.get()
   resultado = eval(ecuacion)
   et.delete(0,END)
   et.insert(0,resultado)
   e = 0

#interfaz entrada de texto
et = Entry(calcu,font=("calibri 20"))
#calumnspan es la cantidad de columnas,padx el espacio entre la ventana,
et.grid(row=0,column=0,columnspan=4,padx=50,pady=5)

#botones

bot1 = Button(calcu,text = "1", width =5, height= 2 ,command=lambda:click_boton(1))
bot2 = Button(calcu,text = "2", width =5, height= 2 ,command=lambda:click_boton(2))
bot3 = Button(calcu,text = "3", width =5, height= 2 ,command=lambda:click_boton(3))
bot4 = Button(calcu,text = "4", width =5, height= 2 ,command=lambda:click_boton(4))
bot5 = Button(calcu,text = "5", width =5, height= 2 ,command=lambda:click_boton(5))
bot6 = Button(calcu,text = "6", width =5, height= 2 ,command=lambda:click_boton(6))
bot7 = Button(calcu,text = "7", width =5, height= 2 ,command=lambda:click_boton(7))
bot8 = Button(calcu,text = "8", width =5, height= 2 ,command=lambda:click_boton(8))
bot9 = Button(calcu,text = "9", width =5, height= 2 ,command=lambda:click_boton(9))
bot0 = Button(calcu,text = "0", width =15, height= 2 ,command=lambda:click_boton(0))

#funciones

botsum = Button(calcu,text = "+", width =5, height= 2 ,command=lambda:click_boton("+"))
botres = Button(calcu,text = "-", width =5, height= 2 ,command=lambda:click_boton("-"))
botdiv = Button(calcu,text = "/", width =5, height= 2 ,command=lambda:click_boton("/"))
botmult = Button(calcu,text = "*", width =5, height= 2 ,command=lambda:click_boton("*"))
botigual = Button(calcu,text = "=", width =5, height= 2 ,command=lambda:resultado())

botparentesise= Button(calcu,text = "(", width =5, height= 2 ,command=lambda:click_boton("("))
botparentesiss = Button(calcu,text = ")", width =5, height= 2 ,command=lambda:click_boton(")"))
botpunto= Button(calcu,text = ".", width =5, height= 2 ,command=lambda:click_boton("."))
botdel= Button(calcu,text = "ac", width =5, height= 2 ,command=lambda:borrar())
#agregar en pantalla

botdel.grid(row=1 ,column=0 ,padx=5,pady=5)
botparentesise.grid(row=1 ,column=1 ,padx=5,pady=5)
botparentesiss.grid(row=1 ,column=2 ,padx=5,pady=5)


bot1.grid(row=4 ,column=0 ,padx=5,pady=5)
bot2.grid(row=4 ,column=1 ,padx=5,pady=5)
bot3.grid(row=4 ,column=2 ,padx=5,pady=5)


bot4.grid(row=3 ,column=0 ,padx=0,pady=5)
bot5.grid(row=3 ,column=1 ,padx=5,pady=5)
bot6.grid(row=3 ,column=2 ,padx=5,pady=5)


bot7.grid(row=2 ,column=0 ,padx=5,pady=5)
bot8.grid(row=2 ,column=1 ,padx=0,pady=5)
bot9.grid(row=2 ,column=2 ,padx=0,pady=5)

bot0.grid(row=5 ,column=0,columnspan=2 ,padx=5,pady=5)
botpunto.grid(row=5 ,column=2 ,padx=0,pady=5)


botdiv.grid(row=1 ,column=3 ,padx=0,pady=5)
botmult.grid(row=2 ,column=3 ,padx=0,pady=5)
botsum.grid(row=3 ,column=3 ,padx=0,pady=5)
botres.grid(row=4 ,column=3 ,padx=0,pady=5)
botigual.grid(row=5 ,column=3 ,padx=5,pady=5)

calcu.mainloop()


