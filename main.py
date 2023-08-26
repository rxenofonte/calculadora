from tkinter import *

# Funções dos botões

def limpar():
    display.delete(0,END)

def inserir(valor):
    display.insert(END,valor)

def igual():
    var = display.get()
    limpar()
    display.insert(END,eval(var))


window = Tk()
window.title("Calculadora")
window.geometry("600x600")

display = Entry(window, font="Arial 20 bold", bg="#1c3ec7",
                fg="white", width=19)
display.pack()

panel = Frame(window)
# Todos os botões vão ficar dentro deste panel
panel.pack()

bt_0 = Button(panel, bg='orange', bd=0, text="0",
              font="Arial 16 bold", width=5, height=5, command=lambda: inserir('0'))
bt_1 = Button(panel, bg='orange', bd=0, text="1",
              font="Arial 16 bold", width=5, height=5, command=lambda: inserir('1'))
bt_2 = Button(panel, bg='orange', bd=0, text="2",
              font="Arial 16 bold", width=5, height=5, command=lambda: inserir('2'))
bt_3 = Button(panel, bg='orange', bd=0, text="3",
              font="Arial 16 bold", width=5, height=5, command=lambda: inserir('3'))
bt_4 = Button(panel, bg='orange', bd=0, text="4",
              font="Arial 16 bold", width=5, height=5, command=lambda: inserir('4'))
bt_5 = Button(panel, bg='orange', bd=0, text="5",
              font="Arial 16 bold", width=5, height=5, command=lambda: inserir('5'))
bt_6 = Button(panel, bg='orange', bd=0, text="6",
              font="Arial 16 bold", width=5, height=5, command=lambda: inserir('6'))
bt_7 = Button(panel, bg='orange', bd=0, text="7",
              font="Arial 16 bold", width=5, height=5, command=lambda: inserir('7'))
bt_8 = Button(panel, bg='orange', bd=0, text="8",
              font="Arial 16 bold", width=5, height=5, command=lambda: inserir('8'))
bt_9 = Button(panel, bg='orange', bd=0, text="9",
              font="Arial 16 bold", width=5, height=5, command=lambda: inserir('9'))
bt_Soma = Button(panel, bg='orange', bd=0, text="+",
              font="Arial 16 bold", width=5, height=5, command=lambda: inserir('+'))
bt_Sub = Button(panel, bg='orange', bd=0, text="-",
              font="Arial 16 bold", width=5, height=5, command=lambda: inserir('-'))
bt_Div = Button(panel, bg='orange', bd=0, text="/",
              font="Arial 16 bold", width=5, height=5, command=lambda: inserir('/'))
bt_Mult = Button(panel, bg='orange', bd=0, text="*",
              font="Arial 16 bold", width=5, height=5, command=lambda: inserir('*'))
bt_Igual = Button(panel, bg='orange', bd=0, text="=",
              font="Arial 16 bold", width=5, height=5, command=igual)
bt_Clear = Button(panel, bg='orange', bd=0, text="C",
              font="Arial 16 bold", width=5, height=5, command=limpar)


bt_7.grid(row=0,column=0)
bt_8.grid(row=0,column=1)
bt_9.grid(row=0,column=2)
bt_Div.grid(row=0,column=3)
bt_4.grid(row=1,column=0)
bt_5.grid(row=1,column=1)
bt_6.grid(row=1,column=2)
bt_Mult.grid(row=1,column=3)
bt_1.grid(row=2,column=0)
bt_2.grid(row=2,column=1)
bt_3.grid(row=2,column=2)
bt_Soma.grid(row=2,column=3)
bt_Clear.grid(row=3,column=0)
bt_0.grid(row=3,column=1)
bt_Igual.grid(row=3,column=2)
bt_Sub.grid(row=3,column=3)




window.mainloop()
