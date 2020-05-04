-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-05-2020 a las 10:25:41
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_ferrosale`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_anuncios_venta`
--

CREATE TABLE `tabla_anuncios_venta` (
  `id` int(11) NOT NULL,
  `fecha` varchar(50) NOT NULL,
  `id_escala` int(11) NOT NULL,
  `id_tipo` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `descripcion` varchar(3000) NOT NULL,
  `precio` float(9,2) NOT NULL,
  `nomyapell` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `emailOK` varchar(2) NOT NULL DEFAULT 'NO',
  `codigo` varchar(255) NOT NULL,
  `foto` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_anuncios_venta`
--

INSERT INTO `tabla_anuncios_venta` (`id`, `fecha`, `id_escala`, `id_tipo`, `titulo`, `descripcion`, `precio`, `nomyapell`, `email`, `emailOK`, `codigo`, `foto`) VALUES
(42, '28 abril 2020 - 23:39', 1, 1, 'VENDO Máquina de mantenimiento de vía', 'Color amarillo, 115 mm de largo\r\nDigital aunque también funciona en analógico.', 54.90, 'Perico de los Palotes', 'tatianaviejo@gmail.com', 'SI', 'pIjHNM7gbNxhWQdMVzJGseZNHOCvuKQrmH7mSquCEBiAPVE1KRwK4JZDjOH0', '42.png'),
(43, '29 abril 2020 - 15:09', 1, 1, 'VENDO Locomotora de vapor GR 851', 'Color negro con anagramas.\r\nAnalógica.', 165.00, 'Alfredo Velasco', 'tatianaviejo@gmail.com', 'SI', 'ph5naD3HohYmP5l9Dguw4nrt3I5b2CSVlAuwXxotVWfGdcpVyZ8MePKli4ZX', '43.png'),
(44, '29 abril 2020 - 17:55', 2, 3, 'VENDO Vagón cisterna \"VTG\"', 'Longitud 55 mm', 19.90, 'Tatiana Viejo', 'tatianaviejo@gmail.com', 'SI', 'WC4gFrp7PLFZF0iLNLsICi7PlKbf6JWXDem3bOBSuPty69LNuvaCbDjz2I19', '44.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_escalas`
--

CREATE TABLE `tabla_escalas` (
  `id` int(11) NOT NULL,
  `escala` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_escalas`
--

INSERT INTO `tabla_escalas` (`id`, `escala`) VALUES
(1, 'H0'),
(2, 'N'),
(3, 'Z');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_mensajes`
--

CREATE TABLE `tabla_mensajes` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `mensaje` varchar(2000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_mensajes`
--

INSERT INTO `tabla_mensajes` (`id`, `nombre`, `mensaje`) VALUES
(1, 'Tatiana', 'Hola Alfredo'),
(2, 'Tatiana', '¿qué tal?'),
(3, 'Tatiana', 'Estoy probando el chat y parece que funciona.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_tipos`
--

CREATE TABLE `tabla_tipos` (
  `id` int(11) NOT NULL,
  `tipo` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_tipos`
--

INSERT INTO `tabla_tipos` (`id`, `tipo`) VALUES
(1, 'Máquinas'),
(2, 'Automotores'),
(3, 'Vagones'),
(4, 'Coches'),
(5, 'Sets'),
(6, 'Vías'),
(7, 'Accesorios');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tabla_anuncios_venta`
--
ALTER TABLE `tabla_anuncios_venta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_escalas` (`id_escala`),
  ADD KEY `fk_tipos` (`id_tipo`);

--
-- Indices de la tabla `tabla_escalas`
--
ALTER TABLE `tabla_escalas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tabla_mensajes`
--
ALTER TABLE `tabla_mensajes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tabla_tipos`
--
ALTER TABLE `tabla_tipos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tabla_anuncios_venta`
--
ALTER TABLE `tabla_anuncios_venta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT de la tabla `tabla_escalas`
--
ALTER TABLE `tabla_escalas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `tabla_mensajes`
--
ALTER TABLE `tabla_mensajes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `tabla_tipos`
--
ALTER TABLE `tabla_tipos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tabla_anuncios_venta`
--
ALTER TABLE `tabla_anuncios_venta`
  ADD CONSTRAINT `fk_escalas` FOREIGN KEY (`id_escala`) REFERENCES `tabla_escalas` (`id`),
  ADD CONSTRAINT `fk_tipos` FOREIGN KEY (`id_tipo`) REFERENCES `tabla_tipos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
