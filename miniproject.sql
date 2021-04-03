-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 25, 2021 at 11:52 AM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `miniproject`
--

-- --------------------------------------------------------

--
-- Table structure for table `mentions`
--

DROP TABLE IF EXISTS `mentions`;
CREATE TABLE IF NOT EXISTS `mentions` (
  `mid` bigint(20) NOT NULL,
  `text` varchar(250) DEFAULT NULL,
  `sender` varchar(250) DEFAULT NULL,
  `polarity` float DEFAULT NULL,
  `subjectivity` float DEFAULT NULL,
  PRIMARY KEY (`mid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mentions`
--

INSERT INTO `mentions` (`mid`, `text`, `sender`, `polarity`, `subjectivity`) VALUES
(1367413251193991172, 'Hi  ', 'Pg35740700', 0, 0),
(1367363274547687428, ' MiniPro44233766 I feel lucky today ', 'Hrishi72239127', 0.333333, 0.833333),
(1367338952223461377, 'Hii  ', 'Hrishi72239127', 0, 0),
(1367162255867961344, 'Today is a great day!  ', 'AspeaksR', 1, 0.75),
(1366629317183119364, ' Hello', 'AspeaksR', 0, 0),
(1372982763687571457, ' am very happy with the carwash service, my window looks pristine. Thank you!', 'AspeaksR', 1, 1),
(1373136942573883393, 'The services you offered were best I have ever experienced. Thank you !  ', 'Hrishi72239127', 1, 0.6),
(1373130461648543744, 'did not really like the iphone 12  ', 'Pg35740700', 0.2, 0.2),
(1374614601245941761, ' hi, i hated the your services and will never use your products again. i find you obnoxious and you… https://t.co/em2mfush1l', 'AspeaksR', -0.9, 0.7);

-- --------------------------------------------------------

--
-- Table structure for table `responses`
--

DROP TABLE IF EXISTS `responses`;
CREATE TABLE IF NOT EXISTS `responses` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `mid` bigint(20) DEFAULT NULL,
  `text` varchar(250) DEFAULT NULL,
  `is_liked` int(11) DEFAULT NULL,
  `is_rt` int(11) DEFAULT NULL,
  PRIMARY KEY (`RID`),
  KEY `mid` (`mid`)
) ENGINE=MyISAM AUTO_INCREMENT=120 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `responses`
--

INSERT INTO `responses` (`RID`, `mid`, `text`, `is_liked`, `is_rt`) VALUES
(109, 1367413251193991172, 'Hello. We are here to help.', 0, 0),
(115, 1367363274547687428, '', 1, 0),
(111, 1367338952223461377, 'Hello. We are here to help.', 0, 0),
(112, 1367162255867961344, 'As a company, we feel a lot better when our customers wake up in a positive way. Your services mean a lot to us. Much appreciated.', 0, 1),
(113, 1366629317183119364, 'Hello. We are here to help.', 0, 0),
(114, 1372982763687571457, 'As a company, we feel a lot better when our customers wake up in a positive way. Your services mean a lot to us. Much appreciated.', 0, 1),
(116, 1373136942573883393, 'As a company, we feel a lot better when our customers wake up in a positive way. Your services mean a lot to us. Much appreciated.', 0, 1),
(118, 1373130461648543744, 'Hello. We are here to help.', 0, 0),
(119, 1374614601245941761, 'Dear sir/madam, we regret this. We will get in touch to help you feel better right away, please be patient with us', 0, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
