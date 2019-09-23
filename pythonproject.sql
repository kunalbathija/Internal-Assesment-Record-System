-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 25, 2019 at 03:56 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pythonproject`
--

-- --------------------------------------------------------

--
-- Table structure for table `aoa`
--

CREATE TABLE `aoa` (
  `roll_no` int(11) NOT NULL DEFAULT '0',
  `name` varchar(50) NOT NULL,
  `ut1` int(11) DEFAULT NULL,
  `ut2` int(11) DEFAULT NULL,
  `ut_avg` int(11) DEFAULT NULL,
  `email_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `aoa`
--

INSERT INTO `aoa` (`roll_no`, `name`, `ut1`, `ut2`, `ut_avg`, `email_id`) VALUES
(1, 'Anish Adnani', NULL, NULL, 0, '2017.anish.adnani@ves.ac.in'),
(2, 'Aadarsh Ahuja', NULL, NULL, NULL, '2017.aadarsh.ahuja@ves.ac.in'),
(3, 'Samay Ahuja', NULL, NULL, NULL, '2017.samay.ahuja@ves.ac.in'),
(4, 'Anjali Amin', NULL, NULL, NULL, '2017.anjali.amin@ves.ac.in'),
(5, 'Purva Badgujar', NULL, NULL, NULL, '2017.purva.badgujar@ves.ac.in'),
(6, 'Atharva Bapat', NULL, NULL, NULL, '2017.atharva.bapat@ves.ac.in'),
(7, 'Kunal Bathija', NULL, NULL, NULL, '2017.kunal.bathija@ves.ac.in'),
(8, 'Nihal Bhandary', NULL, NULL, NULL, '2017.nihal.bhandary@ves.ac.in'),
(9, 'Kalpesh Bhole', NULL, NULL, NULL, '2017.kalpesh.bhole@ves.ac.in'),
(10, 'Tina Chandwani', NULL, NULL, NULL, '2017.tina.chandwani@ves.ac.in');

-- --------------------------------------------------------

--
-- Table structure for table `cg`
--

CREATE TABLE `cg` (
  `roll_no` int(11) NOT NULL DEFAULT '0',
  `name` varchar(50) NOT NULL,
  `ut1` int(11) DEFAULT NULL,
  `ut2` int(11) DEFAULT NULL,
  `ut_avg` int(11) DEFAULT NULL,
  `email_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cg`
--

INSERT INTO `cg` (`roll_no`, `name`, `ut1`, `ut2`, `ut_avg`, `email_id`) VALUES
(1, 'Anish Adnani', NULL, NULL, 0, '2017.anish.adnani@ves.ac.in'),
(2, 'Aadarsh Ahuja', NULL, NULL, NULL, '2017.aadarsh.ahuja@ves.ac.in'),
(3, 'Samay Ahuja', NULL, NULL, NULL, '2017.samay.ahuja@ves.ac.in'),
(4, 'Anjali Amin', NULL, NULL, NULL, '2017.anjali.amin@ves.ac.in'),
(5, 'Purva Badgujar', NULL, NULL, NULL, '2017.purva.badgujar@ves.ac.in'),
(6, 'Atharva Bapat', NULL, NULL, NULL, '2017.atharva.bapat@ves.ac.in'),
(7, 'Kunal Bathija', NULL, NULL, NULL, '2017.kunal.bathija@ves.ac.in'),
(8, 'Nihal Bhandary', NULL, NULL, NULL, '2017.nihal.bhandary@ves.ac.in'),
(9, 'Kalpesh Bhole', NULL, NULL, NULL, '2017.kalpesh.bhole@ves.ac.in'),
(10, 'Tina Chandwani', NULL, NULL, NULL, '2017.tina.chandwani@ves.ac.in');

-- --------------------------------------------------------

--
-- Table structure for table `coa`
--

CREATE TABLE `coa` (
  `roll_no` int(11) NOT NULL DEFAULT '0',
  `name` varchar(50) NOT NULL,
  `ut1` int(11) DEFAULT NULL,
  `ut2` int(11) DEFAULT NULL,
  `ut_avg` int(11) DEFAULT NULL,
  `email_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `coa`
--

INSERT INTO `coa` (`roll_no`, `name`, `ut1`, `ut2`, `ut_avg`, `email_id`) VALUES
(1, 'Anish Adnani', NULL, NULL, 0, '2017.anish.adnani@ves.ac.in'),
(2, 'Aadarsh Ahuja', NULL, NULL, NULL, '2017.aadarsh.ahuja@ves.ac.in'),
(3, 'Samay Ahuja', NULL, NULL, NULL, '2017.samay.ahuja@ves.ac.in'),
(4, 'Anjali Amin', NULL, NULL, NULL, '2017.anjali.amin@ves.ac.in'),
(5, 'Purva Badgujar', NULL, NULL, NULL, '2017.purva.badgujar@ves.ac.in'),
(6, 'Atharva Bapat', NULL, NULL, NULL, '2017.atharva.bapat@ves.ac.in'),
(7, 'Kunal Bathija', NULL, NULL, NULL, '2017.kunal.bathija@ves.ac.in'),
(8, 'Nihal Bhandary', NULL, NULL, NULL, '2017.nihal.bhandary@ves.ac.in'),
(9, 'Kalpesh Bhole', NULL, NULL, NULL, '2017.kalpesh.bhole@ves.ac.in'),
(10, 'Tina Chandwani', NULL, NULL, NULL, '2017.tina.chandwani@ves.ac.in');

-- --------------------------------------------------------

--
-- Table structure for table `maths`
--

CREATE TABLE `maths` (
  `roll_no` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `ut1` int(11) DEFAULT NULL,
  `ut2` int(11) DEFAULT NULL,
  `ut_avg` int(11) DEFAULT NULL,
  `email_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `maths`
--

INSERT INTO `maths` (`roll_no`, `name`, `ut1`, `ut2`, `ut_avg`, `email_id`) VALUES
(1, 'Anish Adnani', NULL, NULL, 0, '2017.anish.adnani@ves.ac.in'),
(2, 'Aadarsh Ahuja', NULL, NULL, NULL, '2017.aadarsh.ahuja@ves.ac.in'),
(3, 'Samay Ahuja', NULL, NULL, NULL, '2017.samay.ahuja@ves.ac.in'),
(4, 'Anjali Amin', NULL, NULL, NULL, '2017.anjali.amin@ves.ac.in'),
(5, 'Purva Badgujar', NULL, NULL, NULL, '2017.purva.badgujar@ves.ac.in'),
(6, 'Atharva Bapat', NULL, NULL, NULL, '2017.atharva.bapat@ves.ac.in'),
(7, 'Kunal Bathija', NULL, NULL, NULL, '2017.kunal.bathija@ves.ac.in'),
(8, 'Nihal Bhandary', NULL, NULL, NULL, '2017.nihal.bhandary@ves.ac.in'),
(9, 'Kalpesh Bhole', NULL, NULL, NULL, '2017.kalpesh.bhole@ves.ac.in'),
(10, 'Tina Chandwani', NULL, NULL, NULL, '2017.tina.chandwani@ves.ac.in');

-- --------------------------------------------------------

--
-- Table structure for table `os`
--

CREATE TABLE `os` (
  `roll_no` int(11) NOT NULL DEFAULT '0',
  `name` varchar(50) NOT NULL,
  `ut1` int(11) DEFAULT NULL,
  `ut2` int(11) DEFAULT NULL,
  `ut_avg` int(11) DEFAULT NULL,
  `email_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `os`
--

INSERT INTO `os` (`roll_no`, `name`, `ut1`, `ut2`, `ut_avg`, `email_id`) VALUES
(1, 'Anish Adnani', NULL, NULL, 0, '2017.anish.adnani@ves.ac.in'),
(2, 'Aadarsh Ahuja', NULL, NULL, NULL, '2017.aadarsh.ahuja@ves.ac.in'),
(3, 'Samay Ahuja', NULL, NULL, NULL, '2017.samay.ahuja@ves.ac.in'),
(4, 'Anjali Amin', NULL, NULL, NULL, '2017.anjali.amin@ves.ac.in'),
(5, 'Purva Badgujar', NULL, NULL, NULL, '2017.purva.badgujar@ves.ac.in'),
(6, 'Atharva Bapat', NULL, NULL, NULL, '2017.atharva.bapat@ves.ac.in'),
(7, 'Kunal Bathija', NULL, NULL, NULL, '2017.kunal.bathija@ves.ac.in'),
(8, 'Nihal Bhandary', NULL, NULL, NULL, '2017.nihal.bhandary@ves.ac.in'),
(9, 'Kalpesh Bhole', NULL, NULL, NULL, '2017.kalpesh.bhole@ves.ac.in'),
(10, 'Tina Chandwani', NULL, NULL, NULL, '2017.tina.chandwani@ves.ac.in');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `maths`
--
ALTER TABLE `maths`
  ADD PRIMARY KEY (`roll_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `maths`
--
ALTER TABLE `maths`
  MODIFY `roll_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
