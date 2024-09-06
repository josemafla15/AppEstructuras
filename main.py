from tkinter import *
from Usuarios import usuario as User

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

def registroFrame():
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
    boton_registro = Button(frame_registro, text="Registrarse", command=registro)
    boton_registro.config(bg="green",
                          fg="white")
    boton_registro.grid(row=13, column=1, sticky=NW)


    frame_main.grid_remove()

def loginFrame():
    frame_login.config(
        bd=4,
        relief="solid"
    )
    frame_login.grid(row=1)
    titulo_login = Label(frame_login, text="Vamos a iniciar sesión")
    titulo_login.config(bg="orange",
                           fg="white",
                           font=("Arial", 15),
                           padx=100
                           )
    titulo_login.grid(row=1,column=0, columnspan=5)

    Label(frame_login, text="").grid(row=2)
    Label(frame_login, text="Correo: ").grid(row=3, column=0, sticky=NW)
    correo_entry = Entry(frame_login).grid(row=3, column=1, sticky=NW)

    Label(frame_login, text="").grid(row=4)
    Label(frame_login, text="Contraseña: ").grid(row=5, column=0, sticky=NW)
    contraseña_entry = Entry(frame_login).grid(row=5, column=1, sticky=NW)

    Label(frame_login, text="").grid(row=6)
    boton_iniciar_sesion = Button(frame_login, text="Iniciar sesión")
    boton_iniciar_sesion.config(bg="green",
                                fg="white"
                                )
    boton_iniciar_sesion.grid(row=7, column=1, sticky=NW)

    frame_main.grid_remove()

def registro():
    usuario = User.Usuario(valor_nombre_registro, valor_apellidos_registro, valor_correo_registro, valor_contraseña_registro)
    registro = usuario.registrarse() 

    if registro[0] >= 1:
        print("Registro exitoso")
    else: print("Lo sentimos, contraseña invalida")

# DEFINICION DE FRAMES

# FRAME MAIN
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
Button(frame_main, text="Registrarse", command=registroFrame).grid(row=3, column=0, sticky=NW)
Label(frame_main, text="O").grid(row=3, column=1, sticky=NW)
Button(frame_main, text="Iniciar sesión", command=loginFrame).grid(row=3, column=2, sticky=NW)

# FRAMES REGISTRO
frame_registro = Frame(ventana, width=250)

# FRAMES LOGIN
frame_login = Frame(ventana, width=250)







ventana.mainloop()