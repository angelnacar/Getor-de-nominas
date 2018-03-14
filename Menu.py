from tkinter import *
from tkinter.messagebox import showinfo, showerror, askquestion
import datetime
import sqlite3



#clase menu principal
class Menu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=None)
        self.master.title("Gestor RRHH")
        self.master.geometry("800x500")
        self.master.resizable(False,False)
        Label(root,text="Gestor Nóminas", fg="gray", font=("Times New Roman",40,"bold")).place(x=200,y=5)
        Button(root,text="Alta - Baja",fg="white",background="red",font=("Times New Roman",20,"bold"),command=self.alta).place(x=100,y=300)
        Button(root, text="Gestor", fg="white", background="red", font=("Times New Roman", 20, "bold"),command=self.gestor).place(x=350, y=180)
        Button(root, text="Recibos", fg="white", background="red", font=("Times New Roman", 20, "bold"), command=self.calculo).place(x=560, y=300)
        root.mainloop()
    def alta(self): #llama a la clase alta y baja de empleados
        a = AltaBaja()
        root.wait_window(a.top)
    def gestor(self): #llama a la clase gestor
        b = Gestor()
        root.wait_window(b.top)
    def calculo(self): #llama a la clase calculo
        c = Recibos()
        root.wait_window(c.top)

#clase para el alta y baja de empleados
class AltaBaja():
    def __init__(self):
        self.codigo = StringVar()
        self.apelNom = StringVar()
        self.fechaAlta = StringVar()
        self.categoria = StringVar()
        self.descripcionCategoria = StringVar()
        self.retribucion = StringVar()
        self.complemento = StringVar()
        self.irpf = StringVar()
        self.fechaBaja = StringVar()
        self.top = Toplevel()
        self.top.transient()
        self.top.grab_set()
        self.top.geometry("900x600")
        self.top.resizable(False,False)
        self.top.title("Alta / Baja")
        Label(self.top, text="ALTA / BAJA", fg="white",background="orange", font=("Times New Roman", 40, "bold")).place(x=250, y=5)
        Label(self.top, text="Codigo", fg="black",font=("Times New Roman", 13, "bold")).place(x=40, y=98)
        Entry(self.top,textvariable=self.codigo,font=("Times New Roman", 13, "bold italic"),width="10").place(x=20,y=120)
        Label(self.top, text="Apellidos y Nombre", fg="black", font=("Times New Roman", 13, "bold")).place(x=400, y=98)
        Entry(self.top, textvariable=self.apelNom, font=("Times New Roman", 20, "bold italic"),width="40").place(x=250, y=120)
        Label(self.top, text="Fecha Alta", fg="black", font=("Times New Roman", 13, "bold")).place(x=30, y=158)
        Entry(self.top, textvariable=self.fechaAlta, font=("Times New Roman", 13, "bold italic"), width="10").place(x=20,y=180)
        Label(self.top, text="Categoria", fg="black", font=("Times New Roman", 13, "bold")).place(x=180, y=158)
        Entry(self.top, textvariable=self.categoria, font=("Times New Roman", 13, "bold italic"), width="10").place(x=170, y=180)
        Label(self.top, text="Descripcion categoria", fg="black", font=("Times New Roman", 13, "bold")).place(x=400, y=160)
        Entry(self.top, textvariable=self.descripcionCategoria, font=("Times New Roman", 15, "bold italic"), width="35").place(x=320,y=180)
        Label(self.top, text="Retribucion", fg="black", font=("Times New Roman", 13, "bold")).place(x=40,y=220)
        Entry(self.top, textvariable=self.retribucion, font=("Times New Roman", 15, "bold italic"),width="13").place(x=30, y=240)
        Label(self.top, text="Complemento", fg="black", font=("Times New Roman", 13, "bold")).place(x=220, y=220)
        Entry(self.top, textvariable=self.complemento, font=("Times New Roman", 15, "bold italic"), width="13").place(x=210, y=240)
        Label(self.top, text="IRPF", fg="black", font=("Times New Roman", 13, "bold")).place(x=410, y=220)
        Entry(self.top, textvariable=self.irpf, font=("Times New Roman", 15, "bold italic"), width="13").place(x=380, y=240)
        Label(self.top, text="Fecha Baja", fg="black", font=("Times New Roman", 13, "bold")).place(x=610, y=220)
        Entry(self.top, textvariable=self.fechaBaja, font=("Times New Roman", 15, "bold italic"), width="13").place(x=580,y=240)
        Button(self.top, text="Alta Empleado", fg="white", background="green", font=("Times New Roman", 20, "bold"), command=self.NuevoEmpleado).place(x=150, y=400)
        Button(self.top, text="Baja Empleado", fg="white", background="red", font=("Times New Roman", 20, "bold"),command=self.BorrarEmpleado).place(x=500, y=400)
        #Button(self.top, text="Buscar Empleado", fg="white", background="orange", font=("Times New Roman", 20, "bold"),command=self.BuscarEmpleado).place(x=320, y=500)
    def NuevoEmpleado(self):
        conexion = sqlite3.connect("gestorNominas.db")
        cursor = conexion.cursor()

        try:
            cursor.execute("INSERT INTO empleados (cod,apelnom,fealta,febaja,nCate,desCat,retribucion,complemento,irpf) VALUES (null, '{}','{}','0000-00-00',{},'{}',{},{},{})".format(self.apelNom.get(), self.fechaAlta.get(), self.categoria.get(), self.descripcionCategoria.get(), float(self.retribucion.get()), float(self.complemento.get()), float(self.irpf.get())))
            conexion.commit()
        except sqlite3.IntegrityError:
            showerror("El empleado no ha sido guardado")
        except ValueError:
            showerror("Error","Caracteres incorrectos")
        else:
            showinfo("Aviaso","Empleado registrado")
        conexion.close()
    def BorrarEmpleado(self):
        conexion = sqlite3.connect("gestorNominas.db")
        cursor = conexion.cursor()
        try:
            busqueda = cursor.execute("SELECT * FROM empleados WHERE cod = {}".format(self.codigo.get()))

            for i in busqueda:
                    #showinfo("Aviso", "Quiere borrar los datos de {}".format(i[1]))
                    respuesta = askquestion("Aviso","¿QUIERE DAR DE BAJA AL EMPLEADO {} CON Nºempleado: {}".format(i[1],self.codigo.get()))

                    baja = i[3]

            if respuesta and baja == '0000-00-00':
                try:
                    #print("UPDATE empleados set febaja = {} WHERE cod = {}".format(datetime.date.today(),self.codigo.get()))
                    cursor.execute("UPDATE empleados set febaja = '{}' WHERE cod = {}".format(datetime.date.today(),self.codigo.get()))
                    conexion.commit()

                except:
                        showerror("Error","Fallo en la conexion")
                else:
                    showinfo("Aviso","Empleado dado de baja con fecha {}".format(datetime.date.today()))
            else:
                    showerror("Aviso","DADO DE BAJA CON ANTERIORIDAD")
        except:
            showerror("Error","El empleado Nº {} no existe en la bbdd".format(self.codigo.get()))

            conexion.close()
#clase para la actualización de datos de los empleados
class Gestor():
    def __init__(self):
        self.codigo = StringVar()
        self.apelNom = StringVar()
        self.fechaAlta = StringVar()
        self.categoria = StringVar()
        self.descripcionCategoria = StringVar()
        self.retribucion = StringVar()
        self.complemento = StringVar()
        self.irpf = StringVar()
        self.top = Toplevel()
        self.top.transient()
        self.top.grab_set()
        self.top.geometry("850x450")
        self.top.resizable(False, False)
        self.top.title("GESTOR")
        Label(self.top, text="GESTOR", fg="white", background="orange",font=("Times New Roman", 40, "bold")).place(x=300, y=5)
        Label(self.top, text="Codigo", fg="black", font=("Times New Roman", 13, "bold")).place(x=40, y=98)
        Entry(self.top, textvariable=self.codigo, font=("Times New Roman", 13, "bold italic"), width="10",background="#33E9FF").place(x=20,y=120)
        Label(self.top, text="Apellidos y Nombre", fg="black", font=("Times New Roman", 13, "bold")).place(x=400, y=98)
        Entry(self.top, textvariable=self.apelNom, font=("Times New Roman", 20, "bold italic"), width="40").place(x=250,y=120)
        Label(self.top, text="Fecha Alta", fg="black", font=("Times New Roman", 13, "bold")).place(x=30, y=158)
        Entry(self.top, textvariable=self.fechaAlta, font=("Times New Roman", 13, "bold italic"), width="10").place(x=20, y=180)
        Label(self.top, text="Categoria", fg="black", font=("Times New Roman", 13, "bold")).place(x=180, y=158)
        Entry(self.top, textvariable=self.categoria, font=("Times New Roman", 13, "bold italic"), width="10").place(x=170, y=180)
        Label(self.top, text="Descripcion categoria", fg="black", font=("Times New Roman", 13, "bold")).place(x=400,y=160)
        Entry(self.top, textvariable=self.descripcionCategoria, font=("Times New Roman", 15, "bold italic"),width="35").place(x=320, y=180)
        Label(self.top, text="Retribucion", fg="black", font=("Times New Roman", 13, "bold")).place(x=140, y=220)
        Entry(self.top, textvariable=self.retribucion, font=("Times New Roman", 15, "bold italic"), width="13").place(x=130, y=240)
        Label(self.top, text="Complemento", fg="black", font=("Times New Roman", 13, "bold")).place(x=320, y=220)
        Entry(self.top, textvariable=self.complemento, font=("Times New Roman", 15, "bold italic"), width="13").place(x=310, y=240)
        Label(self.top, text="IRPF", fg="black", font=("Times New Roman", 13, "bold")).place(x=510, y=220)
        Entry(self.top, textvariable=self.irpf, font=("Times New Roman", 15, "bold italic"), width="13").place(x=480,y=240)
        Button(self.top, text="Actualizar Cambios", fg="white", background="orange", font=("Times New Roman", 20, "bold"),command=self.Actualizar).place(x=280, y=300)

    def Actualizar(self):
        conexion = sqlite3.connect("gestorNominas.db")
        cursor = conexion.cursor()
        try:
            datos = conexion.execute("SELECT*FROM empleados WHERE cod = {}".format(self.codigo.get()))
            for i in datos:
                feBaja = i[3]
            if feBaja == '0000-00-00':

                cursor.execute("UPDATE empleados set apelnom = '{}', fealta = '{}', nCate = {}, desCat = '{}', retribucion = {}, complemento = {}, irpf = {} WHERE cod = {}".format(self.apelNom.get(),self.fechaAlta.get(),self.categoria.get(),self.descripcionCategoria.get(),self.retribucion.get(),self.complemento.get(),self.irpf.get(),self.codigo.get()))
                conexion.commit()
                showinfo("Aviso", "Empleado Actualizado")

            else:
                showerror("Error","Empleado está dado de baja")
        except sqlite3.OperationalError: #Controla que los caracteres introducidos sean correctos
            showerror("Error", "Caracteres incorrectos")
        except UnboundLocalError: #Controla por si el empleado buscado no exite
            showerror("Error", "No existe el empleado Nº:{}".format(self.codigo.get()))


        conexion.close()


#clase para el cálculo de nóminas y generación de la misma
class Recibos():
    def __init__(self):
        self.codigo = StringVar()
        self.apelNom = StringVar()
        self.fechaAlta = StringVar()
        self.categoria = StringVar()
        self.descripcionCategoria = StringVar()
        self.retribucion = StringVar()
        self.complemento = StringVar()
        self.irpf = StringVar()
        self.top = Toplevel()
        self.top.transient()
        self.top.grab_set()
        self.top.geometry("850x450")
        self.top.resizable(False, False)
        self.top.title("RECIBOS")
        Label(self.top, text="RECIBOS", fg="white", background="orange", font=("Times New Roman", 40, "bold")).place(x=300, y=5)
        Label(self.top, text="Codigo empleado a calcular", fg="black", font=("Times New Roman", 13, "bold")).place(x=200, y=120)
        Label(self.top, text="Apellidos y Nombre", fg="black", font=("Times New Roman", 13, "bold")).place(x=470, y=150)
        Label(self.top, text="Fecha Alta", fg="black", font=("Times New Roman", 13, "bold")).place(x=60, y=150)
        Label(self.top, text="Fecha Baja", fg="black", font=("Times New Roman", 13, "bold")).place(x=180, y=150)
        Label(self.top, text="Cod Categ.", fg="black", font=("Times New Roman", 13, "bold")).place(x=60, y=210)
        Label(self.top, text="Categoria", fg="black", font=("Times New Roman", 13, "bold")).place(x=180, y=210)
        Label(self.top, text="Retribucion", fg="black", font=("Times New Roman", 13, "bold")).place(x=60, y=290)
        Label(self.top, text="Complemento", fg="black", font=("Times New Roman", 13, "bold")).place(x=190, y=290)
        Label(self.top, text="IRPF", fg="black", font=("Times New Roman", 13, "bold")).place(x=340, y=290)
        Label(self.top, text="RET. IRPF", fg="black", font=("Times New Roman", 13, "bold")).place(x=430, y=290)
        Label(self.top, text="RET. SS", fg="black", font=("Times New Roman", 13, "bold")).place(x=560, y=290)
        Label(self.top, text="NETO", fg="black", font=("Times New Roman", 13, "bold")).place(x=710, y=290)
        Entry(self.top, textvariable=self.codigo, font=("Times New Roman", 13, "bold italic"), width="10",background="#33E9FF").place(x=90, y=120)
        Button(self.top, text="Calcular", fg="white", background="orange",font=("Times New Roman", 20, "bold"), command=self.calculo).place(x=200, y=380)
        Button(self.top, text="Imprimir", fg="white", background="orange", font=("Times New Roman", 20, "bold"),command=self.archivo).place(x=500, y=380)

    def calculo(self):
        conexion = sqlite3.connect("gestorNominas.db")
        cursor = conexion.cursor()
        busqueda = cursor.execute("SELECT*FROM empleados WHERE cod = {}".format(self.codigo.get()))
        try:
            for i in busqueda:
                self.nombre = i[1]
                self.fechaA = i[2]
                self.fechaB = i[3]
                self.codCat = i[4]
                self.cate = i[5]
                self.sueldo = i[6]
                self.comple = i[7]
                self.irp = i[8]
            if self.fechaB == '0000-00-00':
                self.retIrp = round((self.sueldo+self.comple)*(self.irp/100),2)
                self.retSS = round(self.sueldo*0.064,2)
                self.neto = round((self.sueldo+self.comple)-(self.retIrp+self.retSS),2)
                Label(self.top, text=self.nombre, fg="black", font=("Times New Roman", 18, "bold"),background="#33E9FF").place(x=440, y=180)
                Label(self.top, text=self.fechaA, fg="black", font=("Times New Roman", 16, "bold"), background="#33E9FF").place( x=50, y=180)
                Label(self.top, text=self.fechaB, fg="black", font=("Times New Roman", 16, "bold"), background="#33E9FF").place(x=170,y=180)
                Label(self.top, text=self.codCat, fg="black", font=("Times New Roman", 16, "bold"), background="#33E9FF").place(x=90, y=240)
                Label(self.top, text=self.cate, fg="black", font=("Times New Roman", 16, "bold"), background="#33E9FF").place(x=170,y=240)
                Label(self.top, text="{} €".format(self.sueldo), fg="black", font=("Times New Roman", 16, "bold"), background="#33E9FF").place(x=55,y=320)
                Label(self.top, text="{} €".format(self.comple), fg="black", font=("Times New Roman", 16, "bold"),background="#33E9FF").place(x=195, y=320)
                Label(self.top, text="{} %".format(self.irp), fg="black", font=("Times New Roman", 16, "bold"),background="#33E9FF").place(x=325, y=320)
                Label(self.top, text="{} €".format(self.retIrp), fg="black", font=("Times New Roman", 16, "bold"),background="yellow").place(x=420, y=320)
                Label(self.top, text="{} €".format(self.retSS), fg="black", font=("Times New Roman", 16, "bold"),background="yellow").place(x=540, y=320)
                Label(self.top, text="{} €".format(self.neto), fg="black", font=("Times New Roman", 16, "bold"),background="yellow").place(x=680, y=320)
            else:
                showinfo("Aviso","El empleado con Nº:{}. Está dado de baja".format(self.codigo.get()))
        except:
            showerror("Error","No existe el empleado con Nº:{}".format(self.codigo.get()))
        conexion.close()
    def archivo(self): #genera el archivo
        b = datetime.date.today() #capta el mes en que se genera la nómina

        try:
            fichero = open("Nomina empleado {}.txt".format(self.nombre),'w')
            apellidos = self.nombre.split(",")
            texto = "Mes: {}\nCodigo Empleado: {}\n\tApellidos: {}\n\tNombre: {}\n\tNº Cat: {} -- {} --\n\tRetribucion: {} €\n\tComplemento: {} €\n\tIRPF: {} %\n\tRET.IRPF: {}€\n\tRET.SS: {} €\n\tTOTAL A PERCIBIR ------ {} €-------  \n\n".format(b.strftime("%B"),self.codigo.get(),apellidos[0],apellidos[1],self.codCat,self.cate,self.sueldo,self.comple,self.irp,self.retIrp,self.retSS,self.neto)
            fichero.write(texto)
            fichero.close()
            showinfo("Fichero","Nómina Registrada")
        except:
            showerror("Error","Fallo al crear nómina")


#función para crear la bbdd si no existe
def CreaBaseDatos():
    conexion = sqlite3.connect("gestorNominas.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("CREATE TABLE empleados (cod INTEGER PRIMARY KEY AUTOINCREMENT,apelnom VARCHAR(100) NOT NULL,fealta DATE,febaja DATE,nCate INT,desCat VARCHAR(100),retribucion FLOAT,complemento FLOAT, irpf FLOAT )")
    except sqlite3.OperationalError:
        print()
    else:
        showinfo("Aviso","La base de datos se creo correctamente")
    conexion.close()

root = Tk()
CreaBaseDatos()
a = Menu(root)




