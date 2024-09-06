from tkinter import *

#DEFINICION DE LA VENTANA
ventana = Tk()
ventana.title("Base de datos SalchiBurguer || Creador: Jose Mafla")
ventana.geometry("500x450")
ventana.resizable(0,0)
ventana.config(bd=15)

# DEFINICION DE VARIABLES 
valor_nombre_registro = StringVar()
valor_apellidos_registro = StringVar()
valor_correo_registro = StringVar()
valor_contraseña_registro = StringVar()
valor_codigo_registro = StringVar()

# DEFINICION DE METODOS 

def registro():
    frame_registro.config(
        bd=4,
        relief="solid"
    )
    frame_registro.grid(row=1)
    titulo_registro = Label(frame_registro, text="Vamos a registrarte")
    titulo_registro.config(bg="orange",
                           fg="white",
                           font=("Arial", 15),
                           padx=100
                           )
    titulo_registro.grid(row=1,column=0, columnspan=5)
    Label(frame_registro, text="").grid(row=2)
    Label(frame_registro, text="Nombre: ").grid(row=3, column=0, sticky=NW)
    nombre_entry = Entry(frame_registro, textvariable=valor_nombre_registro).grid(row=3, column=1, sticky=NW)

    Label(frame_registro, text="").grid(row=4)
    Label(frame_registro, text="Apellidos: ").grid(row=5, column=0, sticky=NW)
    apellidos_entry = Entry(frame_registro).grid(row=5, column=1, sticky=NW)

    Label(frame_registro, text="").grid(row=6)
    Label(frame_registro, text="Correo: ").grid(row=7, column=0, sticky=NW)
    correo_entry = Entry(frame_registro).grid(row=7, column=1, sticky=NW)

    Label(frame_registro, text="").grid(row=8)
    Label(frame_registro, text="Contraseña: ").grid(row=9, column=0, sticky=NW)
    contraseña_entry = Entry(frame_registro).grid(row=9, column=1, sticky=NW)

    Label(frame_registro, text="").grid(row=10)
    Label(frame_registro, text="Codigo: ").grid(row=11, column=0, sticky=NW)
    codigo_entry = Entry(frame_registro).grid(row=11, column=1, sticky=NW)

    Label(frame_registro, text="").grid(row=12)
    boton_registro = Button(frame_registro, text="Registrarse")
    boton_registro.config(bg="green",
                          fg="white")
    boton_registro.grid(row=13, column=1, sticky=NW)


    frame_main.grid_remove()

#DEFINICIONES DEL FRAME MAIN
frame_main = Frame(ventana, width=200,height=250)
frame_main.config(bd=3,
                  relief="solid",
                  padx=100,
                  pady=50
                  )
frame_main.grid(row=1,sticky=S)

titulo_main = Label(frame_main, text="Bienvenido")
titulo_main.config(
    bg="green",
    fg="white",
    font=("Arial", 15),
    padx=50
)
titulo_main.grid(row=0, column=0, columnspan=5,sticky=SW)
Label(frame_main, text="").grid(row=2, column=0)
Button(frame_main, text="Registrarse", command=registro).grid(row=3, column=0, sticky=NW)
Label(frame_main, text="O").grid(row=3, column=1, sticky=NW)
Button(frame_main, text="Loguearse").grid(row=3, column=2, sticky=NW)

frame_registro = Frame(ventana, width=250)







ventana.mainloop()