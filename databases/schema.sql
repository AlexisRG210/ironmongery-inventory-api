-- 1. Crear la base de datos con nombre concreto
CREATE DATABASE IF NOT EXISTS ferreteria_db;
USE ferreteria_db;

-- 2. Crear la tabla de productos
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio_costo DECIMAL(10, 2) NOT NULL,
    precio_venta DECIMAL(10, 2) NOT NULL,
    cantidad_actual INT NOT NULL,
    stock_minimo_alerta INT NOT NULL
);

-- 3. Insertar productos de ferretería para pruebas
INSERT INTO productos (nombre, precio_costo, precio_venta, cantidad_actual, stock_minimo_alerta) VALUES
('Martillo de Uña 16oz', 85.00, 130.00, 12, 5),   -- Stock OK
('Cinta Aislar Negra 20m', 12.50, 25.00, 3, 10),   -- ⚠️ STOCK BAJO (Alerta)
('Pinzas de Presión 10"', 140.00, 210.00, 8, 4),   -- Stock OK
('Flexómetro 5 metros', 45.00, 75.00, 2, 5),      -- ⚠️ STOCK BAJO (Alerta)
('Desarmador de Cruz PH2', 30.00, 55.00, 15, 6);   -- Stock OK