CREATE DATABASE IF NOT EXISTS inventario_2 ;
use inventario_2;

CREATE TABLE usuarios(
    id int(255) auto_increment not null,
    nombre varchar(255),
    apellido varchar(255),
    correo varchar (255) not null,
    password varchar(255) not null,
    fechaCreacion DATE not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_correo UNIQUE(correo)

 ) ENGINE = InnoDb;


 CREATE TABLE tipoProductos (
    id int(255) auto_increment not null,
    nombre varchar(255) not null,
    CONSTRAINT pk_tipoProductos PRIMARY KEY(id)

 ) ENGINE = InnoDb;

 CREATE TABLE productos(
    id int(255) auto_increment not null,
    id_usuario int(255),
    id_tipo int(255),
    cantidad int(255) not null,
    fechaIngreso DATE not null,

    
    CONSTRAINT pk_productos PRIMARY KEY(id),
    CONSTRAINT fk_productos_usuario FOREIGN KEY(id_usuario) REFERENCES usuarios(id),
    CONSTRAINT fk_productos_tipo FOREIGN KEY(id_tipo) REFERENCES tipoProductos(id) 

 ) ENGINE = InnoDb;

   INSERT INTO tipoProductos VALUES (null, "1kg papas");
   INSERT INTO tipoProductos VALUES (null, "1lt aceite");
   INSERT INTO tipoProductos VALUES (null, "1 paquete salchichas x 12");

