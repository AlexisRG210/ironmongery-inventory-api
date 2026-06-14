CREATE DATABASE IF NOT EXISTS ferreteria_db;
USE ferreteria_db;

CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio_costo DECIMAL(10,2) NOT NULL,
    precio_venta DECIMAL(10,2) NOT NULL,
    cantidad_actual INT NOT NULL,
    stock_minimo_alerta INT NOT NULL
);

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    rol VARCHAR(20) NOT NULL DEFAULT 'empleado'
);

INSERT INTO usuarios (username, password_hash)
VALUES ('empleado1', 'empleado123');

INSERT INTO productos
(nombre, precio_costo, precio_venta, cantidad_actual, stock_minimo_alerta)
VALUES
('Martillo de Uña 16oz', 85.00, 130.00, 12, 5),
('Cinta Aislar Negra 20m', 12.50, 25.00, 3, 10),
('Pinzas de Presión 10"', 140.00, 210.00, 8, 4),
('Flexómetro 5 metros', 45.00, 75.00, 2, 5),
('Desarmador de Cruz PH2', 30.00, 55.00, 15, 6);