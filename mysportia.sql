-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-10-2023 a las 02:01:56
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mysportia`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `cedula` int(10) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `email` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`cedula`, `nombre`, `apellido`, `telefono`, `direccion`, `email`) VALUES
(125469883, 'Juan', 'Millan', '3116063021', 'mz 17 cas 7', 'xorozk@gmail.com'),
(234567899, 'SGSDFGSD', 'SDGSDGSD', '3216549878', 'DGDGSD', 'casha@gmail.com'),
(1025689235, 'Heider', 'Orozco', '3116063021', 'mz 17 cas 3', 'xorozk@gmail.com'),
(1065569616, 'Heider', 'Orozco', '3116063021', 'mz 17 cas 3', 'xorozk@gmail.com'),
(1065569618, 'Heider', 'Orozco', '3116063021', 'mz 17 cas 3', 'xorozk@gmail.com'),
(1065620834, 'Carlos', 'Solorzano', '3043712935', 'Calle falsa', 'cabascarlosandres@gmail.com'),
(1234567899, 'SGSDFGSD', 'SDGSDGSD', '3216549878', 'DGDGSD', 'casha@gmail.com'),
(1256938741, 'LUis', 'Orozco', '3116063021', 'mz 17 cas 3', 'xorozk@gmail.com'),
(2147483647, 'Heider', 'Orozco', '3116063021', 'mz 17 cas 3', 'xorozk@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalleventas`
--

CREATE TABLE `detalleventas` (
  `id_pedido` int(3) UNSIGNED NOT NULL,
  `id_producto` int(10) NOT NULL,
  `cantidad` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detalleventas`
--

INSERT INTO `detalleventas` (`id_pedido`, `id_producto`, `cantidad`) VALUES
(53706, 1, 5),
(788856, 2, 3),
(616193, 3, 1),
(551897, 5, 5),
(378249, 2, 1),
(516796, 2, 1),
(716726, 7, 1),
(114226, 2, 1),
(122345, 3, 1),
(199684, 3, 1),
(51358, 2, 1),
(228124, 2, 1),
(635696, 2, 1),
(263794, 2, 1),
(837924, 2, 2),
(556575, 2, 1),
(520631, 2, 1),
(316114, 2, 1),
(391605, 2, 1),
(412062, 2, 1),
(599419, 2, 1),
(195865, 2, 1),
(452715, 2, 1),
(737035, 3, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id_producto` int(10) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(150) DEFAULT 'Este articulo no contiene descripción',
  `marca` varchar(100) NOT NULL,
  `precio` decimal(30,2) NOT NULL,
  `stock` int(99) NOT NULL,
  `imagen` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id_producto`, `nombre`, `descripcion`, `marca`, `precio`, `stock`, `imagen`) VALUES
(1, 'Balon de futbol', 'Balon hecho con materiales organicos. Agradable al tacto', 'Adidas', 100000.00, 20, 'balón.png'),
(2, 'Camiseta de Colombia', 'Camiseta talla M de la selección de futbol de Colombia', 'Adidas', 50000.00, 10, 'camCol.png'),
(3, 'Guayos', 'Gayos de talla 42 para jugar futbol', 'Nike', 120000.00, 12, 'guayos.png'),
(4, 'Pelota de Tennis', 'Pelota con un diseño ergonómico para jugar Tennis', 'Wilson', 25000.00, 70, 'pelota.png'),
(5, 'Raqueta de Tennis profesional', 'Raqueta hecha de materiales resistentes', 'Adidas', 125000.00, 45, 'raqueta.png'),
(6, 'Chamarra deportiva', 'Chamarra deportiva', 'Wilson', 650000.00, 1, 'chamarra.png'),
(7, 'Atletico Madrid Mangas Largas', 'Chándal para hombre hecho de tejido de punto de alta calidad que te mantendrá abrigado y cómodo', 'zhaojiexiaodian', 750000.00, 0, 'manga.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `id_pedido` int(3) UNSIGNED NOT NULL,
  `fecha` date NOT NULL DEFAULT current_timestamp(),
  `cedula` int(10) NOT NULL,
  `total` decimal(30,2) NOT NULL,
  `estado` varchar(50) NOT NULL DEFAULT 'por pagar'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`id_pedido`, `fecha`, `cedula`, `total`, `estado`) VALUES
(51358, '2023-10-20', 1065569616, 50000.00, 'pagado'),
(53706, '2023-10-20', 1234567899, 500000.00, 'pagado'),
(114226, '2023-10-20', 1025689235, 50000.00, 'pagado'),
(122345, '2023-10-20', 1065569616, 120000.00, 'pagado'),
(195865, '2023-10-20', 1065569616, 50000.00, 'pagado'),
(199684, '2023-10-20', 1065569616, 120000.00, 'pagado'),
(228124, '2023-10-20', 1065569616, 50000.00, 'pagado'),
(263794, '2023-10-20', 1065569616, 50000.00, 'pagado'),
(316114, '2023-10-20', 1065569616, 50000.00, 'pagado'),
(378249, '2023-10-20', 1025689235, 50000.00, 'pagado'),
(391605, '2023-10-20', 1065569618, 50000.00, 'pagado'),
(412062, '2023-10-20', 1065569616, 50000.00, 'pagado'),
(452715, '2023-10-20', 1256938741, 50000.00, 'pagado'),
(516796, '2023-10-20', 1025689235, 50000.00, 'pagado'),
(520631, '2023-10-20', 1065569616, 50000.00, 'pagado'),
(551897, '2023-10-20', 1065620834, 625000.00, 'pagado'),
(556575, '2023-10-20', 1065569616, 50000.00, 'pagado'),
(599419, '2023-10-20', 1065569616, 50000.00, 'pagado'),
(616193, '2023-10-20', 1234567899, 120000.00, 'pagado'),
(635696, '2023-10-20', 1065569616, 50000.00, 'pagado'),
(716726, '2023-10-20', 2147483647, 750000.00, 'pagado'),
(737035, '2023-10-20', 1065569616, 120000.00, 'pagado'),
(788856, '2023-10-20', 234567899, 150000.00, 'pagado'),
(837924, '2023-10-20', 125469883, 100000.00, 'pagado');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`cedula`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id_producto`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`id_pedido`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
