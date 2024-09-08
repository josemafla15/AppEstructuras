from tkinter import *
from Usuarios import usuario as User
from datetime import datetime
from Productos import Producto as Product

#DEFINICION DE LA VENTANA
ventana = Tk()
ventana.title("Base de datos SalchiBurguer || Creador: Jose Mafla")
ventana.geometry("500x450")
ventana.resizable(0,0)
ventana.config(bd=15)

# DEFINICION DE VARIABLES 

# VARIABLES REGISTRO
valor_nombre_registro = StringVar()
valor_apellidos_registro = StringVar()
valor_correo_registro = StringVar()
valor_contraseña_registro = StringVar()


# VARIABLES LOGIN
valor_correo_login = StringVar()
valor_contraseña_login = StringVar()

# VARIABLES ACCIONES

# VARIABLES AÑADIR 
datos_usuario = []

opcion = IntVar()



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
    apellidos_entry = Entry(frame_registro, textvariable=valor_apellidos_registro).grid(row=5, column=1, sticky=NW)

    Label(frame_registro, text="").grid(row=6)
    Label(frame_registro, text="Correo: ").grid(row=7, column=0, sticky=NW)
    correo_entry = Entry(frame_registro, textvariable=valor_correo_registro).grid(row=7, column=1, sticky=NW)

    Label(frame_registro, text="").grid(row=8)
    Label(frame_registro, text="Contraseña: ").grid(row=9, column=0, sticky=NW)
    contraseña_entry = Entry(frame_registro, textvariable=valor_contraseña_registro).grid(row=9, column=1, sticky=NW)


    Label(frame_registro, text="").grid(row=10)
    boton_registro = Button(frame_registro, text="Registrarse", command=registro)
    boton_registro.config(bg="green",
                          fg="white")
    boton_registro.grid(row=11, column=1, sticky=NW)

    Label(frame_registro, text="").grid(row=12)


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
    correo_entry = Entry(frame_login, textvariable=valor_correo_login).grid(row=3, column=1, sticky=NW)

    Label(frame_login, text="").grid(row=4)
    Label(frame_login, text="Contraseña: ").grid(row=5, column=0, sticky=NW)
    contraseña_entry = Entry(frame_login, textvariable=valor_contraseña_login).grid(row=5, column=1, sticky=NW)

    Label(frame_login, text="").grid(row=6)
    boton_iniciar_sesion = Button(frame_login, text="Iniciar sesión", command=login)
    boton_iniciar_sesion.config(bg="green",
                                fg="white"
                                )
    boton_iniciar_sesion.grid(row=7, column=1, sticky=NW)

    frame_main.grid_remove()

def registro():
    usuario = User.Usuario(valor_nombre_registro.get(), valor_apellidos_registro.get(), valor_correo_registro.get(), valor_contraseña_registro.get())
    registro = usuario.registrarse() 

    
    #print(registro)
    if registro[0] >= 1 :
        
        respuesta = Label(frame_registro, text= f"Felicitaciones {registro[1].nombre}, creaste tu cuenta")
        respuesta.config(
            bg="orange",
            fg="white",
            bd=3,
            relief="solid",
            font=("Arial", 10)
        )
        respuesta.grid(row=13, column=1)
        Label(frame_registro, text="").grid(row=14)

        
        
    else:    
        respuesta = Label(frame_registro, text= f"Lo sentimos, ocurrió un error")
        respuesta.config(
            bg="red",
            fg="white",
            bd=3,
            relief="solid",
            font=("Arial", 10)
        )
        respuesta.grid(row=13, column=1)
        Label(frame_registro, text="").grid(row=14)


def login():
    usuario = User.Usuario("", "", valor_correo_login.get(), valor_contraseña_login.get())
    login = usuario.loguearse()

    # frame_login.grid_remove()
    if not login :
        
        Label(frame_login, text="Lo sentimos, credenciales incorrectas").grid(row=15,column=1)
    else: 
        datos_usuario.append(login[0])
        datos_usuario.append(login[1])
        datos_usuario.append(login[2])
        datos_usuario.append(login[3])
        datos_usuario.append(login[4])
        datos_usuario.append(login[5])

        print(datos_usuario)
        accionesFrame(login)
        frame_login.grid_remove()
        

def accionesFrame(usuario):

    frame_acciones.config(
        bd=4,
        relief="solid"
    )
    frame_acciones.grid(row=0)

    
    respuesta = Label(frame_acciones, text=f"Bienvenido {usuario[1]} ¡¡Ingresaste a tu cuenta!!")
                                            
    respuesta.config(bg="blue",
                         fg="white",
                         padx=25,
                         pady=15,
                         font=("Arial",10)
                         )
    respuesta.grid(row=0,column=0, columnspan=5)

    Label(frame_acciones, text="").grid(row=1)
    pregunta = Label(frame_acciones, text=f"¿Que acción deseas realizar?")
                                            
    
    pregunta.grid(row=2,column=0)
    


    Label(frame_acciones, text="").grid(row=3)
    

    Label(frame_acciones, text="Añadir inventario").grid(row=4, column=0, sticky=NW)
    boton_añadir = Button(frame_acciones, text="Añadir", command=accionAnadir)
    boton_añadir.config(bd=3, 
                        relief="solid",
                        bg="green",
                        fg="white")
    boton_añadir.grid(row=4, column=1, sticky=NW)

    Label(frame_acciones, text="").grid(row=5)

    Label(frame_acciones, text="Ver el inventario").grid(row=6, column=0, sticky=NW)
    boton_ver = Button(frame_acciones, text="Ver")
    boton_ver.config(bd=3, 
                        relief="solid",
                        bg="green",
                        fg="white")
    boton_ver.grid(row=6, column=1, sticky=NW)

    Label(frame_acciones, text="").grid(row=7)

    Label(frame_acciones, text="Eliminar inventario").grid(row=8, column=0, sticky=NW)
    boton_añadir = Button(frame_acciones, text="Eliminar")
    boton_añadir.config(bd=3, 
                        relief="solid",
                        bg="green",
                        fg="white")
    boton_añadir.grid(row=8, column=1, sticky=NW)

    Label(frame_acciones, text="").grid(row=9)

def accionAnadir():

    frame_acciones.grid_remove()
    frame_anadir.config(bd=4, relief="solid")
    frame_anadir.grid(row=1)

    titulo = Label(frame_anadir, text="Añadamos ese producto al inventario")
    titulo.config(bg="pink",
                  fg="white",
                  font=("Arial", 10),
                  padx=80,
                  pady=15

                  )
    titulo.grid(row=0, column=0, columnspan=5)

    Label(frame_anadir, text="Tipo de producto: ").grid(row=1, column=0)
    Label(frame_anadir, text="Producto tipo 1 = 1kg papas ").grid(row=2, column=0, sticky=NW)
    Label(frame_anadir, text="Producto tipo 2 = 1lt aceite ").grid(row=3, column=0, sticky=NW)
    Label(frame_anadir, text="Producto tipo 3 = 1 paquete salchichas x 12 ").grid(row=4, column=0, sticky=NW)
    
    Label(frame_anadir, text="Selecciona una opción").grid(row=5, column=0, sticky=NW)

    
    OptionMenu(frame_anadir, opcion ,"Tipo 1", "Tipo 2", "Tipo 3").grid(row=5, column=1, sticky=NW)
    llamada()

def llamada():
    producto = Product.Producto("", "", "")
    llamar = producto.traerTipos()


    print(llamar)
    # for elemento in llamar:
    #     print(elemento[0])

    #Label(frame_anadir, text="").grid(row=3)
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

# FRAME ACCIONES
frame_acciones = Frame(ventana, width=250)

# FRAME CREAR 
frame_anadir = Frame(ventana, width=250)







ventana.mainloop()