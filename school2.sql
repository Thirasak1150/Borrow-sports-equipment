-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 10, 2024 at 10:20 AM
-- Server version: 8.0.17
-- PHP Version: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `school2`
--

-- --------------------------------------------------------

--
-- Table structure for table `borrow`
--

CREATE TABLE `borrow` (
  `id_student` varchar(100) NOT NULL,
  `id_sport_equiment` varchar(100) NOT NULL,
  `start_borrow_date` varchar(100) NOT NULL,
  `start_return_date` varchar(100) NOT NULL,
  `status_` varchar(50) NOT NULL,
  `end_return_date` varchar(100) NOT NULL,
  `id_bor_row` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `borrow`
--

INSERT INTO `borrow` (`id_student`, `id_sport_equiment`, `start_borrow_date`, `start_return_date`, `status_`, `end_return_date`, `id_bor_row`) VALUES
('66345', '001', '2024-03-20 19:50:58', '2024-03-27 19:50:58', 'คืนเเล้ว', '2024-03-20 19:51:45', 4),
('61222', '005', '2024-03-20 19:52:26', '2024-03-27 19:52:26', 'คืนเเล้ว', '2024-03-21 15:29:36', 5),
('66345', '002', '2024-03-21 15:02:51', '2024-03-28 15:02:51', 'คืนเเล้ว', '2024-03-21 15:03:47', 6),
('66345', '001', '2024-03-21 15:04:43', '2024-03-28 15:04:43', 'คืนเเล้ว', '2024-03-21 15:26:04', 7),
('61222', '004', '2024-03-21 15:26:23', '2024-03-28 15:26:23', 'ยังไม่คืน', '', 8),
('61222', '005', '2024-03-21 15:29:19', '2024-03-28 15:29:19', 'คืนเเล้ว', '2024-03-21 15:29:36', 9);

-- --------------------------------------------------------

--
-- Table structure for table `sports_equipment`
--

CREATE TABLE `sports_equipment` (
  `sport_id` varchar(50) NOT NULL,
  `sport_name` varchar(100) NOT NULL,
  `count_equipment` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sports_equipment`
--

INSERT INTO `sports_equipment` (`sport_id`, `sport_name`, `count_equipment`) VALUES
('001', 'วอลเลย์บอล', 5),
('002', 'ฟุตบอล', 10),
('003', 'บาสเก็ตบอล', 10),
('004', 'ปิงปอง', 9),
('005', 'ตะกร้อ', 11);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` varchar(100) NOT NULL,
  `s_name` varchar(100) NOT NULL,
  `s_lastname` varchar(100) NOT NULL,
  `s_grade` varchar(100) NOT NULL,
  `s_tel` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `s_name`, `s_lastname`, `s_grade`, `s_tel`) VALUES
('61222', 'ณัฐณิชา ', 'ทับเที่ยง', 'ม.6', '092-399-2699'),
('62749', 'วรรณวิษา', 'เพชรสังกฤษ', 'ม.5', '061-456-4958'),
('63678', 'ปรัชยาพร', 'ลัทธิวรรณ', 'ม.4', '093-550-5965'),
('64524', 'นงนภัส', 'วรรณาหาร', 'ม.3', '098-889-3459'),
('64577', 'ณัฐวรา', 'แสงฉาย', 'ม.3', '092-389-4832'),
('65423', 'หริฎฐ์', 'เบี้ยไธสง', 'ม.2', '092-339-4495'),
('65455', 'มุทิตา', 'เรืองศรี', 'ม.2', '088-383-8944'),
('66329', 'จิราภา', 'ยอดศิริ', 'ม.1', '087-394-5586'),
('66345', 'นิลาวัลย์', 'หมินหมัน', 'ม.1', '098-358-8573'),
('66348', 'กนกวรรณ ', 'เหนือเกาะหวาย', 'ม.1', '093-598-5804');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `borrow`
--
ALTER TABLE `borrow`
  ADD PRIMARY KEY (`id_bor_row`);

--
-- Indexes for table `sports_equipment`
--
ALTER TABLE `sports_equipment`
  ADD PRIMARY KEY (`sport_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `borrow`
--
ALTER TABLE `borrow`
  MODIFY `id_bor_row` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
