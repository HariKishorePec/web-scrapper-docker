-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 14, 2023 at 06:04 AM
-- Server version: 8.0.18
-- PHP Version: 7.3.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bse`
--

-- create database if not exist
CREATE DATABASE IF NOT EXISTS `bse` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

use bse;
-- --------------------------------------------------------

--
-- Table structure for table `bulk_deals`
--



CREATE TABLE `bulk_deals` (
  `id` int(11) NOT NULL,
  `security_code` int(11) DEFAULT NULL,
  `security_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `client_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `deal_type` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `deal_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bulk_deals`
--
ALTER TABLE `bulk_deals`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
