from estudiante import  Estudiantes
from tkinter import * #Tk,Label,Entry,Button
from tkinter import messagebox


class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestion de estudiantes")
        self.ventana.geometry("600x600")
        self.ventana.resizable(1,1)

        self.main()
#....Vistas Views del sistema
   
    def borrarPantalla (self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

        print("\033c")

    def menuAcciones(self):
        self.borrarPantalla()
        tipo="Coche"
        Label(self.ventana, text=f":::Menu de {tipo}:::")
        Button(self.ventana, text="1.-Agregar",command=self.insertar_estudiantes_view).pack(pady=10)
        Button(self.ventana, text="2.-Borrar",command=self.borrar_estudiantes_view).pack(pady=10)
        Button(self.ventana, text="3.-Modificar",command=self.actualizar_estudiantes_view).pack(pady=10)
        Button(self.ventana, text="4.-Mostrar",command=self.mostrar_estudiantes_view).pack(pady=10)
        Button(self.ventana, text="5.-Regresar",command=self.main).pack(pady=10)
   
    def insertar_estudiantes_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingresar los datos del Estudiante...").pack(pady=10)
        Label(self.ventana, text="Nombre: ").pack(pady=5)
        self.nombre=Entry(self.ventana)
        self.nombre.focus()
        self.nombre.pack(pady=5)

        Label(self.ventana, text="Nota: ").pack(pady=5)
        self.nota=Entry(self.ventana)
        self.nota.pack(pady=5)
        self.nota.pack(pady=5)

        Button(self.ventana, text="::Regresar::",command=self.menuAcciones).pack(pady=5)

        Button(self.ventana, text="::Agregar::",command=self.insertar_coche_controller).pack(pady=5)

    def borrar_estudiantes_view(self):

        self.borrarPantalla()

        Label(self.ventana, text=".....ELIMINAR ESTUDIANTES.....").pack(pady=10)
        Label(self.ventana, text="Id de el estudiante a eliminar: ").pack(pady=5)
        self.Id=Entry(self.ventana)
        self.Id.focus()
        self.Id.pack(pady=5)
        

        Button(self.ventana, text="::Regresar::",command=self.menuAcciones).pack(pady=5)
        
        Button(self.ventana, text="::Borrar::",command=self.borrar_coche_controller).pack(pady=5)

    def actualizar_estudiantes_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="Id de el estudiante a actualizar: ").pack(pady=5)
        self.Id=Entry(self.ventana)
        self.Id.focus()
        self.Id.pack(pady=5)

        Label(self.ventana, text="...Ingresar los datos del estudiante a actualizar...").pack(pady=10)
        self.nombre=Entry(self.ventana)
        Label(self.ventana, text="Nombre: ").pack(pady=5)
        self.nombre.focus()
        self.nombre.pack(pady=5)
        
        Label(self.ventana, text="Nota: ").pack(pady=5)
        self.nota=Entry(self.ventana)
        self.nota.pack(pady=5)

        Button(self.ventana, text="::Regresar::",command=self.menuAcciones).pack(pady=5)
        
        Button(self.ventana, text="::Actualizar::",command=self.actualizar_coche_controller).pack(pady=5)

    def mostrar_estudiantes_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="....::LISTADO DE ESTUDIANTES::....").pack(pady=10)

        estudiante1 = Estudiantes('',0)
        registros = estudiante1.consultar()
        del estudiante1

        if registros and len(registros) > 0:
            # Encabezado
            encabezado = f"{'ID':<5} | {'Nombre':<10} | {'Nota':<10}"
            Label(self.ventana, text=encabezado, font=("Courier", 9, "bold")).pack(pady=5)

            # Filas
            for fila in registros:
                info = f"{fila[0]:<6} | {fila[1]:<10}"
                Label(self.ventana, text=info, font=("Courier", 9)).pack(pady=2)
        else:
            Label(self.ventana, text="No se encontró información en la base de datos.").pack(pady=20)

        Button(self.ventana, text="::Regresar::",command=self.menuAcciones).pack(pady=5)

    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text=";;; MENU PRINCIPAL ;;;",).pack(pady=20)
        Button(self.ventana, text="1.- Estudiantes",command=self.menuAcciones).pack(pady=10)
        Button(self.ventana, text="2.- Salir",command=self.ventana.quit).pack(pady=10)

 #....Controlador o controller del sistema...  

    def respuesta_sql(self,respuesta):
            if respuesta:
                # input("\t\t:::accion exitosa:::")
                messagebox.showinfo(title=":: Exitoso ::", message="...Accion Realizada Con Exito...")
            else:
                # input("\t\t:::!camarada al chile no jalo!:::") 
                messagebox.showerror(title=":: Verifique por favor ::", message="...Error con la Accion...") 

    def insertar_coche_controller(self):
        # cochesitos={}
        # cochesitos['marca']=self.marca.get()
        
        datosEstudiantes =(self.nombre.get(),self.nota.get())
        estudiante1 = Estudiantes(*datosEstudiantes)
        respuesta = estudiante1.insertar()
        self.respuesta_sql(respuesta)
        del estudiante1

    def borrar_coche_controller(self):
            # cochesitos={}
            # cochesitos['marca']=self.marca.get()
            
        id_estudiante = self.Id.get()
        
        estudiante1 = Estudiantes('',0)
        respuesta = estudiante1.eliminar(id_estudiante)
        self.respuesta_sql(respuesta)
        del estudiante1

    def actualizar_coche_controller(self):

        id_estudiante = self.Id.get()
        datosEstudiantes =(self.nombre.get(),self.nota.get())
        estudiante1 = Estudiantes(*datosEstudiantes)
        respuesta = estudiante1.actualizar(id_estudiante)
        self.respuesta_sql(respuesta)
        del estudiante1

    def mostrar_coche_controller(self):

        estudiante1 = Estudiantes('',0)
        registros = estudiante1.consultar()
        if len(registros) > 0:
            numEstudiantes = 1
            print(f"\n\testudiante # {numEstudiantes}\n\tID:\ttnombre\ttnombre:\n")
            for fila in registros:
                print(f"\t{fila[0]} \t {fila[1]}\t {fila[2]}\t {fila[3]}") 
        else:
            print("no se encontro informacion en la base de datos")
            self.esperaTecla()
            del estudiante1

if __name__ == "__main__":
    ventana=Tk()
    app = App(ventana)
    ventana.mainloop()
