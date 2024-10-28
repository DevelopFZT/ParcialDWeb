-- Crear base de datos
CREATE DATABASE parcial_rfnd;

-- Usar la base de datos
USE parcial_rfnd;

-- Crear tabla login
CREATE TABLE login (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL,
    contrasenia VARCHAR(255) NOT NULL,
    rol VARCHAR(50) NOT NULL
);

-- Insertar datos en la tabla login
INSERT INTO login (usuario, contrasenia, rol) VALUES ('admin', 'admin123', 'administrador');
INSERT INTO login (usuario, contrasenia, rol) VALUES ('usuario1', 'password1', 'usuario');
INSERT INTO login (usuario, contrasenia, rol) VALUES ('usuario2', 'password2', 'usuario');

-- Crear tabla asunto
CREATE TABLE asunto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descripcion TEXT
);

-- Insertar datos en la tabla asunto
INSERT INTO asunto (titulo, descripcion) VALUES ('Asunto 1', 'Descripción del asunto 1');
INSERT INTO asunto (titulo, descripcion) VALUES ('Asunto 2', 'Descripción del asunto 2');
INSERT INTO asunto (titulo, descripcion) VALUES ('Asunto 3', 'Descripción del asunto 3');

-- Crear tabla nivel_educativo
CREATE TABLE nivel_educativo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nivel VARCHAR(100) NOT NULL
);

-- Insertar datos en la tabla nivel_educativo
INSERT INTO nivel_educativo (nivel) VALUES ('Primaria');
INSERT INTO nivel_educativo (nivel) VALUES ('Secundaria');
INSERT INTO nivel_educativo (nivel) VALUES ('Preparatoria');
INSERT INTO nivel_educativo (nivel) VALUES ('Universidad');

-- Crear tabla alumnos
CREATE TABLE alumnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido_paterno VARCHAR(100) NOT NULL,
    apellido_materno VARCHAR(100) NOT NULL,
    telefono VARCHAR(15),
    correo VARCHAR(100)
);

-- Insertar datos en la tabla alumnos
INSERT INTO alumnos (nombre, apellido_paterno, apellido_materno, telefono, correo) 
VALUES ('Juan', 'Pérez', 'García', '555-1234', 'juan.perez@example.com');
INSERT INTO alumnos (nombre, apellido_paterno, apellido_materno, telefono, correo) 
VALUES ('María', 'González', 'López', '555-5678', 'maria.gonzalez@example.com');
INSERT INTO alumnos (nombre, apellido_paterno, apellido_materno, telefono, correo) 
VALUES ('Carlos', 'López', 'Martínez', '555-8765', 'carlos.lopez@example.com');

-- Crear tabla municipios
CREATE TABLE municipios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_municipio VARCHAR(100) NOT NULL,
    nombre_oficina VARCHAR(100) NOT NULL,
    estado VARCHAR(100) NOT NULL
);

-- Insertar datos en la tabla municipios
INSERT INTO municipios (nombre_municipio, nombre_oficina, estado) 
VALUES ('Municipio 1', 'Oficina Central', 'Estado 1');
INSERT INTO municipios (nombre_municipio, nombre_oficina, estado) 
VALUES ('Municipio 2', 'Oficina Regional', 'Estado 2');
INSERT INTO municipios (nombre_municipio, nombre_oficina, estado) 
VALUES ('Municipio 3', 'Oficina Local', 'Estado 3');

-- Crear tabla turnos
CREATE TABLE turnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha_solicitud DATE NOT NULL,
    curp VARCHAR(18) NOT NULL,
    nombre_completo VARCHAR(255) NOT NULL,
    estado VARCHAR(100) NOT NULL,
    municipio_id INT NOT NULL,
    alumno_id INT NOT NULL,
    nivel_educativo_id INT NOT NULL,
    asunto_id INT NOT NULL,
    estatus_tramite VARCHAR(50) NOT NULL,
    FOREIGN KEY (municipio_id) REFERENCES municipios(id),
    FOREIGN KEY (alumno_id) REFERENCES alumnos(id),
    FOREIGN KEY (nivel_educativo_id) REFERENCES nivel_educativo(id),
    FOREIGN KEY (asunto_id) REFERENCES asunto(id)
);

-- Insertar datos de ejemplo en la tabla turnos
INSERT INTO turnos (fecha_solicitud, curp, nombre_completo, estado, municipio_id, alumno_id, nivel_educativo_id, asunto_id, estatus_tramite) 
VALUES ('2025-02-12', 'CURP1234567890', 'Juan Pérez García', 'Estado 1', 1, 1, 1, 1, 'Pendiente');
INSERT INTO turnos (fecha_solicitud, curp, nombre_completo, estado, municipio_id, alumno_id, nivel_educativo_id, asunto_id, estatus_tramite) 
VALUES ('2025-02-13', 'CURP0987654321', 'María González López', 'Estado 2', 2, 2, 2, 2, 'Resuelto');
INSERT INTO turnos (fecha_solicitud, curp, nombre_completo, estado, municipio_id, alumno_id, nivel_educativo_id, asunto_id, estatus_tramite) 
VALUES ('2025-02-14', 'CURP1122334455', 'Carlos López Martínez', 'Estado 3', 3, 3, 3, 3, 'Pendiente');

git status
git add .
git commit -m "Creacion de proyecto con arquitectura adecuada y creacion de la base de datos"
git push origin main

