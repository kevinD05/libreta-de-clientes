from tkinter import ttk
from tkinter import *
from database import *
from tkinter import messagebox



class app:

    def __init__(self,master):
        self.ventana = master
        self.DibujarLabel()
        self.DibujarEntry()
        self.Dibujarboton()
        self.Dibujarlista("")

    def DibujarLabel(self):
        self.lbl_name = Label(self.ventana, foreground='white', background="#314252", text="Nombre", font=(8)).place(x=60, y=110)
        self.lbl_telefono = Label(self.ventana, foreground='white', background="#314252", text="Telefono",font=(8)).place(x=60, y=160)
        self.lbl_empresa = Label(self.ventana, foreground='white', background="#314252", text="Empresa", font=(8)).place(x=60, y=210)



    def DibujarEntry(self):
        self.nombre = StringVar()
        self.telefono = StringVar()
        self.empresa = StringVar()
        self.buscar_ = StringVar()
        self.txt_nombre = Entry(self.ventana, font=('Arial', 12), textvariable=self.nombre).place(x=140, y=110)
        self.txt_nombre = Entry(self.ventana, font=('Arial', 12), textvariable=self.telefono).place(x=140, y=160)
        self.txt_nombre = Entry(self.ventana, font=('Arial', 12), textvariable=self.empresa).place(x=140, y=210)
 
        #agregado de buscar 
        self.txt_buscar = Entry(self.ventana, font=('Arial', 12), textvariable= self.buscar_).place(x=60, y=340)
    

    def Dibujarboton(self):
        self.btn_guardar = Button(self.ventana, text='Guadar', relief='flat', background="#0051C8", cursor="hand1", foreground="white", command= lambda:self.guardar()).place(x=750, y=340, width=90)
        self.btn_cancelar = Button(self.ventana, text='Cancelar', relief='flat', background="red", cursor="hand1", foreground="white").place(x=850, y=340, width=90)
    
        #agregado de buscar
        self.btn_guardar = Button(self.ventana, text='Filtrar', relief='flat', background="Green", cursor="hand1", foreground="white", command=lambda:self.buscar(self.buscar_.get())).place(x=260, y=340, width=90)


    def buscar(self,ref):
        self.LimpiarLista()
        self.Dibujarlista("")


    def guardar(self):
        arr = [self.nombre.get(), self.telefono.get(), self.empresa.get()]
        d = Data()
        d.InsertItems(arr)
        self.nombre.set("")
        self.telefono.set("")
        self.empresa.set("")
        self.LimpiarLista()
        self.Dibujarlista("")


    def LimpiarLista(self):
        self.lista.delete(*self.lista.get_children())



    def Dibujarlista(self, ref):
        self.lista = ttk.Treeview(self.ventana, columns=(1, 2 ,3),  show="headings", height='8')
        #Estilo
        estilo = ttk.Style()
        estilo.theme_use('clam')

        estilo.configure('Treeview.Headings', background='#0051C8', relief='flat', foreground='white')
        self.lista.heading(1, text='Nombre')
        self.lista.heading(2, text='Telefono')
        self.lista.heading(3, text='Empresa')
        self.lista.column(2, anchor=CENTER)


        #evento
        self.lista.bind("<Double 1>", self.obtenerFila)



        if ref =="":
            #fill list
            d = Data()
            elements = d.returnAllElements()
            for i in elements:
                self.lista.insert('','end', values=i)

        else:
             #fill list
            d = Data()
            elements = d. Returnempresa(ref)
            for i in elements:
                self.lista.insert('','end', values=i)


        self.lista.place(x=340, y=90)

    def obtenerFila(self, event):
        na = StringVar()
        tel = StringVar()
        em =StringVar()
        NombreFila = self.lista.identify_row(event.y)
        elemento = self.lista.item(self.lista.focus())
        n = elemento['values'][0]
        t = elemento['values'][1]
        e = elemento['values'][2]
        na.set(n)
        tel.set(t)
        em.set(e)

        pop = Toplevel(self.ventana)
        pop.geometry('400x200')
        txt_n =Entry(pop, textvariable=na).place(x=40, y=40)
        txt_t =Entry(pop, textvariable=tel).place(x=40, y=80)
        txt_e =Entry(pop, textvariable=em).place(x=40, y=120)
        #Botones
        btn_cambiar = Button(pop, text='Actualizar', relief='flat', background='#00CE54', foreground='white', command=lambda:self.editar(n, na.get(), tel.get(),em.get())).place(x=180, y=160, width=90)
        btn_eliminar = Button(pop, text='Eliminar', relief='flat', background='red', foreground='white', command=lambda:self.eliminar(na.get())).place(x=290, y=160, width=90)


    def editar(self, n, na, t, e):
        d =Data()
        arr = [na, t, e]
        d.UpdateItem(arr, n)
        messagebox.showinfo(title="Actualizacion", message='Se ha actulizado la base de datos')
        self.LimpiarLista()
        self.Dibujarlista("")


    def eliminar(self, n):
        d = Data()
        d.Delete(n)
        messagebox.showinfo(title="Actualizacion", message='Se ha actulizado la base de datos')
        self.LimpiarLista()
        self.Dibujarlista("")



root = Tk()
root.title('Libreta de clientes')   
root.geometry("1000x400")
root.config(background="#314252")
aplicacion = app(root)
root.mainloop()