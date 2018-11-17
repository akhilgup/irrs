-- MySQL dump 10.13  Distrib 5.7.22, for osx10.9 (x86_64)
--
-- Host: localhost    Database: hack
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `image_input`
--

DROP TABLE IF EXISTS `image_input`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `image_input` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image_name` varchar(255) NOT NULL,
  `image_path` text NOT NULL,
  `time_stamp` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `image_name` (`image_name`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `image_input`
--

LOCK TABLES `image_input` WRITE;
/*!40000 ALTER TABLE `image_input` DISABLE KEYS */;
INSERT INTO `image_input` VALUES (1,'IMG_20181101_084041.jpg','/Users/akhilgupta/Documents/GitHub/nitiayog_5/images/IMG_20181101_084041.jpg','17-11-2018 16:17:18'),(2,'IMG_20181101_084040.jpg','/Users/akhilgupta/Documents/GitHub/nitiayog_5/images/IMG_20181101_084040.jpg','17-11-2018 16:17:18'),(3,'download.jpg','/Users/akhilgupta/Documents/GitHub/nitiayog_5/images/download.jpg','17-11-2018 16:17:18'),(4,'199.jpg','/Users/akhilgupta/Documents/GitHub/nitiayog_5/images/199.jpg','17-11-2018 16:17:18'),(5,'101.jpg','/Users/akhilgupta/Documents/GitHub/nitiayog_5/images/101.jpg','17-11-2018 16:17:18'),(6,'102.jpg','/Users/akhilgupta/Documents/GitHub/nitiayog_5/images/102.jpg','17-11-2018 16:17:18'),(7,'IMG_20181101_084027.jpg','/Users/akhilgupta/Documents/GitHub/nitiayog_5/images/IMG_20181101_084027.jpg','17-11-2018 16:17:18'),(8,'106.jpg','/Users/akhilgupta/Documents/GitHub/nitiayog_5/images/106.jpg','17-11-2018 16:17:18'),(9,'104.jpg','/Users/akhilgupta/Documents/GitHub/nitiayog_5/images/104.jpg','17-11-2018 16:17:18'),(10,'105.jpg','/Users/akhilgupta/Documents/GitHub/nitiayog_5/images/105.jpg','17-11-2018 16:17:18'),(11,'IMG_20181101_084202.jpg','/Users/akhilgupta/Documents/GitHub/nitiayog_5/images/IMG_20181101_084202.jpg','17-11-2018 16:17:18'),(12,'IMG_20181101_082005 (1).jpg','/Users/akhilgupta/Documents/GitHub/nitiayog_5/images/IMG_20181101_082005 (1).jpg','17-11-2018 16:17:18'),(13,'test 1.jpg','/Users/akhilgupta/Documents/GitHub/nitiayog_5/images/test 1.jpg','17-11-2018 16:17:18'),(14,'th.jpg','/Users/akhilgupta/Documents/GitHub/nitiayog_5/images/th.jpg','17-11-2018 16:17:18'),(15,'IMG_20181101_082005.jpg','/Users/akhilgupta/Documents/GitHub/nitiayog_5/images/IMG_20181101_082005.jpg','17-11-2018 16:17:18');
/*!40000 ALTER TABLE `image_input` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `output_info`
--

DROP TABLE IF EXISTS `output_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `output_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `input_id` int(11) NOT NULL,
  `image_name` varchar(255) NOT NULL,
  `image_path` text NOT NULL,
  `vehicle` varchar(255) NOT NULL,
  `potholes` varchar(255) NOT NULL,
  `freeways` varchar(255) NOT NULL,
  `traffic` varchar(255) NOT NULL,
  `pedestrian_lanes` varchar(255) NOT NULL,
  `time_stamp` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `image_name` (`image_name`),
  KEY `input_id` (`input_id`),
  CONSTRAINT `output_info_ibfk_1` FOREIGN KEY (`input_id`) REFERENCES `image_input` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `output_info`
--

LOCK TABLES `output_info` WRITE;
/*!40000 ALTER TABLE `output_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `output_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-17 17:32:38
