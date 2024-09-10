from tkinter import *
from Usuarios import usuario as User
from datetime import datetime
from Productos import Producto as Product
from tkinter import messagebox as MessageBox 

#DEFINICION DE LA VENTANA
ventana = Tk()
ventana.title("Base de datos SalchiBurguer || Creador: Jose Mafla")
ventana.geometry("500x450")
#ventana.resizable()
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

# VARIABLES ANADIR 
datos_usuario = []

valor_tipo_anadir = IntVar()

valor_cantidad_anadir = IntVar()

# VARIABLES ELIMINAR TODo

valor_id_eliminar = IntVar()



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
        accionesFrame()
        frame_login.grid_remove()


        

def accionesFrame():

    frame_acciones.config(
        bd=4,
        relief="solid"
        )
    frame_acciones.grid(row=0)

    
    respuesta = Label(frame_acciones, text=f"Bienvenido {datos_usuario[1]} ¡¡Ingresaste a tu cuenta!!")
                                            
    respuesta.config(bg="blue",
                         fg="white",
                         padx=25,
                         pady=15,
                         font=("Arial",10)
                         )
    respuesta.grid(row=0,column=0, columnspan=5)

    Label(frame_acciones, text="").grid(row=1)
    pregunta = Label(frame_acciones, text=f"¿Que acción deseas realizar?")
    pregunta.grid(row=2, column=0, sticky=NW)                                        

    
    
    Label(frame_acciones, text="").grid(row=3)
    

    Label(frame_acciones, text="Añadir inventario").grid(row=4, column=0, sticky=NW)
    boton_añadir = Button(frame_acciones, text="Añadir", command=anadirFrame)
    boton_añadir.config(bd=3, 
                        relief="solid",
                        bg="green",
                        fg="white")
    boton_añadir.grid(row=4, column=1, sticky=NW)

    Label(frame_acciones, text="").grid(row=5)

    Label(frame_acciones, text="Ver el inventario").grid(row=6, column=0, sticky=NW)
    boton_ver = Button(frame_acciones, text="Ver", command=verFrame)
    boton_ver.config(bd=3, 
                        relief="solid",
                        bg="green",
                        fg="white")
    boton_ver.grid(row=6, column=1, sticky=NW)

    Label(frame_acciones, text="").grid(row=7)

    Label(frame_acciones, text="Sacar elemento del inventario").grid(row=8, column=0, sticky=NW)
    boton_sacar = Button(frame_acciones, text="Sacar", command=sacarFrame)
    boton_sacar.config(bd=3, 
                        relief="solid",
                        bg="green",
                        fg="white")
    boton_sacar.grid(row=8, column=1, sticky=NW)

    Label(frame_acciones, text="").grid(row=9)

    Label(frame_acciones, text="Eliminar ultimo elemento del inventario").grid(row=10, column=0, sticky=NW)
    boton_eliminar = Button(frame_acciones, text="Eliminar", command=eliminarFrame)
    boton_eliminar.config(bd=3, 
                        relief="solid",
                        bg="green",
                        fg="white")
    boton_eliminar.grid(row=10, column=1, sticky=NW)

    Label(frame_acciones, text="").grid(row=11)
    Label(frame_acciones, text="Eliminar cualquier elemento del inventario").grid(row=12, column=0, sticky=NW)
    boton_eliminar_cualquiera = Button(frame_acciones, text="Eliminar", command=eliminarTodoFrame)
    boton_eliminar_cualquiera.config(bd=3, 
                        relief="solid",
                        bg="green",
                        fg="white")
    boton_eliminar_cualquiera.grid(row=12, column=1, sticky=NW)




def anadirFrame():

    def volver():
        accionesFrame()
        frame_anadir.grid_remove()

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

    Label(frame_anadir, text="Tipo de producto: ").grid(row=1, column=0, sticky=NW)
    Label(frame_anadir, text="Tipo 1 = 1kg papas ").grid(row=2, column=0, sticky=NW)
    Label(frame_anadir, text="Tipo 2 = 1lt aceite ").grid(row=3, column=0, sticky=NW)
    Label(frame_anadir, text="Tipo 3 = 1 paquete salchichas").grid(row=4, column=0, sticky=NW)
    
    Label(frame_anadir, text="Selecciona el tipo").grid(row=5, column=0, sticky=NW)

    entry_tipo = Entry(frame_anadir, textvariable=valor_tipo_anadir).grid(row=5, column=1, sticky=NW)
    llamada()

    Label(frame_anadir, text="").grid(row=6)
    Label(frame_anadir, text="Cantidad: ").grid(row=7, column=0, sticky=NW)
    entry_cantidad = Entry(frame_anadir, textvariable=valor_cantidad_anadir).grid(row=7, column=1, sticky=NW)

    Label(frame_anadir, text="").grid(row=8)
    boton_anadir = Button(frame_anadir, text="Añadir producto al inventario", command=accionAnadir)
    boton_anadir.config(bg="green",
                    fg="white")
    boton_anadir.grid(row=9, column=1, sticky=NW)

    boton_volver = Button(frame_anadir, text="Volver", command=volver)
    boton_volver.config(bg="green", fg="white")
    boton_volver.grid(row=9, column=2, sticky=NW)

    


def accionAnadir():
    producto = Product.Producto(datos_usuario[0], valor_tipo_anadir.get(), valor_cantidad_anadir.get())
    anadido = producto.anadir()

    if anadido[0] >= 1:
       Label(frame_acciones, text="").grid(row=12)
       Label(frame_acciones, text="").grid(row=13)
       respuesta = Label(frame_acciones, text="Producto creado exitosamente        ")
       respuesta.config(bg="dark orange",
                        fg="white",
                        padx=40)
       respuesta.grid(row=14, column=0, sticky=NW)
       accionesFrame() 
       frame_anadir.grid_remove()
       

    elif anadido[1].id_tipo >3 or anadido[1].id_tipo == 0:
        Label(frame_anadir, text="").grid(row=10)
        Label(frame_anadir, text="Tipo de producto incorrecto").grid(row=11, column=1, sticky=NW)
        Label(frame_anadir, text="Solo puedes ingresar 1, 2 o 3").grid(row=12, column=1, sticky=NW)
    else: 
        Label(frame_anadir, text="").grid(row=10)
        Label(frame_anadir, text="Error al crear el producto").grid(row=11, column=1, sticky=NW)

def verFrame():
    
    def volver():
        accionesFrame()
        frame_ver.grid_remove()
        #frame_ver
    frame_acciones.grid_remove()
    frame_ver.config(bd=4, relief="solid")
    frame_ver.grid(row=0)

    titulo = Label(frame_ver, text="Este es tu inventario")
    titulo.config(bg="lime green",
                    fg="white",
                    font=("Arial", 10),
                    padx=80,
                    pady=15
                    )
    titulo.grid(row=0, column=0, columnspan=5)

    
    producto = Product.Producto("","","")
    ver = producto.ver()

    boton_volver = Button(frame_ver, text="Volver", command=volver)
    boton_volver.config(bg="green", fg="white")
    boton_volver.grid(row=1, column=0, sticky=NW)

    frame_mostrar.config(bd=4, relief="solid")
    frame_mostrar.grid(row=2)

    # boton_volver = Button(frame_mostrar, text="Volver", command=volver)
    # boton_volver.config(bg="green", fg="white")
    # boton_volver.grid(row=1, column=0, sticky=NW)


    for producto in ver:
        Label(frame_mostrar,text=f"Id producto:  {producto[0]}").grid()
        Label(frame_mostrar,text=f"Id usuario creador: {producto[1]}").grid()
        Label(frame_mostrar,text=f"Id tipo de producto:  {producto[2]}").grid()
        Label(frame_mostrar,text=f"Cantidad: {producto[3]}").grid()
        Label(frame_mostrar,text=f"Fecha creación: {producto[4]}").grid()
        Label(frame_mostrar,text=f"--------").grid()
    
        

def sacarFrame():

    def sacarNo():
        accionesFrame()
        frame_sacar.grid_remove()

    frame_acciones.grid_remove()

    frame_sacar.config(bd=4, relief="solid")
    frame_sacar.grid(row=0)

    titulo = Label(frame_sacar, text="Saquemos un producto del inventario")
    titulo.config(
        bg="dark orange",
        fg="white",
        font=("Arial", 10),
        padx=10,
        pady=15
    )
    titulo.grid(row=0, column=0, columnspan=5, sticky=NW)

    Label(frame_sacar, text="").grid(row=1)

    Label(frame_sacar, text="¿Que hace esta acción?").grid(row=2, column=0, sticky=NW)
    boton_info = Button(frame_sacar,text="Mostrar info", command=mostrarInfoSacar).grid(row=3, column=0,sticky=NW)

    Label(frame_sacar, text="").grid(row=4)
    Label(frame_sacar, text="¿Desea llevar a cabo la acción?").grid(row=5, column=0, sticky=NW)
    
    Label(frame_sacar, text="").grid(row=6)
    boton_si = Button(frame_sacar, text="Si", command=accionSacar)
    boton_si.config(bg="green",
                    fg="white")
    boton_si.grid(row=5, column=1, sticky=NW)

    
    boton_no = Button(frame_sacar, text="No", command=sacarNo)
    boton_no.config(bg="green",
                   fg="white")
    boton_no.grid(row=5, column=2, sticky=NW)
    
def accionSacar():

    producto = Product.Producto("","","")
    sacado = producto.sacar()

    if sacado[0] >=1:
        Label(frame_acciones, text="").grid(row=11)
        Label(frame_acciones, text="").grid(row=12)
        respuesta = Label(frame_acciones, text="Producto eliminado correctamente")
        respuesta.config(bg="sky blue", fg="white", padx=40)
        respuesta.grid(row=14, column=0, sticky=NW)
        accionesFrame()
        frame_sacar.grid_remove()
    
    else:
        Label(frame_sacar, text="").grid(row=6)
        Label(frame_sacar, text="No se pudo eliminar el producto").grid(row=7, column=0, sticky=NW)

def eliminarFrame():


    def eliminarNo():
        frame_eliminar.grid_remove()
        accionesFrame()

    frame_eliminar.config(bd=4, relief="solid")
    frame_eliminar.grid(row=1)

    frame_acciones.grid_remove()
    titulo = Label(frame_eliminar, text="Eliminemos un producto del inventario")
    titulo.config(bg="lawn green",
        fg="black",
        font=("Arial", 10),
        padx=10,
        pady=15)
    titulo.grid(row=0, column=0, columnspan=5, sticky=NW)


    Label(frame_eliminar, text="").grid(row=2)
    Label(frame_eliminar, text="¿Que hace esta acción?").grid(row=3, column=0, sticky=NW)
    boton_info = Button(frame_eliminar,text="Mostrar info", command=mostrarInfoEliminar).grid(row=4, column=0,sticky=NW) 

    Label(frame_eliminar, text="").grid(row=5, column=0, sticky=NW)
    Label(frame_eliminar, text="¿Desea llevar a cabo la acción?").grid(row=6, column=0, sticky=NW)
    boton_si = Button(frame_eliminar, text="Si", command=accionEliminar)
    boton_si.config(bg="green", fg="white")
    boton_si.grid(row=6, column=1, sticky=NW)
    
    boton_no = Button(frame_eliminar, text="No", command=eliminarNo)
    boton_no.config(bg="green", fg="white")
    boton_no.grid(row=6, column=2, sticky=NW)
    
def accionEliminar():

    producto = Product.Producto("","","")
    eliminado = producto.eliminar()

    if eliminado[0] >= 1:
        Label(frame_acciones, text="").grid(row=11)
        Label(frame_acciones, text="").grid(row=12)
        respuesta = Label(frame_acciones, text="Producto eliminado correctamente")
        respuesta.config(bg="spring green", fg="white", padx=40)
        respuesta.grid(row=14, column=0, sticky=NW)
        accionesFrame()
        frame_eliminar.grid_remove()
    
    else: 
        Label(frame_eliminar, text="").grid(row=7)
        Label(frame_eliminar, text="Ya no hay elementos en el inventario").grid(row=8, column=0, sticky=NW)

def eliminarTodoFrame():

    def volver():
        accionesFrame()
        frame_eliminar_todo.grid_remove()
    
    frame_acciones.grid_remove()
    frame_eliminar_todo.config(bd=4, relief="solid")
    frame_eliminar_todo.grid(row=1)

    titulo = Label(frame_eliminar_todo, text="Eliminemos cualquier elemento")
    titulo.config(bg="violet red",
                  fg="white",
                  font=("Arial", 10),
                  padx=10,
                  pady=15)
    titulo.grid(row=0, column=0, columnspan=5, sticky=NW)

    Label(frame_eliminar_todo, text="").grid(row=1)
    Label(frame_eliminar_todo, text="¿Que hace esta acción?").grid(row=2, column=0, sticky=NW)
    boton_info = Button(frame_eliminar_todo, text="Mostrar info", command=mostrarInfoEliminarTodo).grid(row=3, column=0, sticky=NW)

    Label(frame_eliminar_todo, text="").grid(row=4)
    Label(frame_eliminar_todo, text="Ingrese el id del elemento").grid(row=5, column=0, sticky=NW)
    Label(frame_eliminar_todo, text="que desea eliminar del inventario: ").grid(row=6, column=0, sticky=NW)
    
    entry_id = Entry(frame_eliminar_todo, textvariable=valor_id_eliminar).grid(row=7, column=0, sticky=NW)

    Label(frame_eliminar_todo, text="").grid(row=8)
    #Label(frame_eliminar_todo, text="Eliminar elemento: ").grid(row=9, column=0, sticky=NW)
    boton_si = Button(frame_eliminar_todo, text="Eliminar elemento", command=accionEliminarTodo)
    boton_si.config(bg="green", fg="white")
    boton_si.grid(row=9, column=0, sticky=NW)

    Label(frame_eliminar_todo, text="").grid(row=10) 
    boton_volver = Button(frame_eliminar_todo, text="Volver", command=volver)
    boton_volver.config(bg="green", fg="white")
    boton_volver.grid(row=11, column=0, sticky=NW)

def accionEliminarTodo():
    producto = Product.Producto("","","")
    eliminado = producto.eliminarTodo(valor_id_eliminar.get())

    if eliminado[0] >= 1:
        Label(frame_acciones, text="").grid(row=11)
        Label(frame_acciones, text="").grid(row=12)
        respuesta = Label(frame_acciones, text="Producto eliminado correctamente")
        respuesta.config(bg="coral", fg="white", padx=40)
        respuesta.grid(row=14, column=0, sticky=NW)
        accionesFrame()
        frame_eliminar_todo.grid_remove()
    else:
        Label(frame_eliminar_todo, text="").grid(row=12)
        Label(frame_eliminar_todo, text="El producto con el id que ingresó no existe").grid(row=13, column=0, sticky=NW)

    

def mostrarInfoSacar():
    MessageBox.showinfo("¡¡Atencioón!!", "Esta acción saca el producto más viejo en el inventario para usarlo en la cocina (FIFO)")

def mostrarInfoEliminar():
    MessageBox.showinfo("¡¡Atención!!", "Esta acción elimina el ultimo producto agregado al inventario(LIFO)")

def mostrarInfoEliminarTodo():
    MessageBox.showinfo("¡¡Atención!!", "Esta acción elimina cualquier producto agregado al inventario(Listas)")


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

# FRAME ANADIR 
frame_anadir = Frame(ventana, width=250)

#FRAME VER 
frame_ver = Frame(ventana, width=250)

frame_mostrar= Frame(frame_ver, width=250)

# FRAME SACAR
frame_sacar = Frame(ventana, width=250)

# FRAME ELIMINAR 
frame_eliminar = Frame(ventana, width=250)

# FRAME ELIMINAR TODo
frame_eliminar_todo = Frame(ventana, width=250)






ventana.mainloop()