CREATE DATABASE  IF NOT EXISTS `proapp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `proapp`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: proapp
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bid`
--

DROP TABLE IF EXISTS `bid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bid` (
  `Task_ID` int NOT NULL,
  `Tradesperson_ID` int NOT NULL,
  `Bid_Amount` decimal(10,2) NOT NULL,
  `Bid_Status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Task_ID`,`Tradesperson_ID`),
  KEY `Tradesperson_ID` (`Tradesperson_ID`),
  CONSTRAINT `bid_ibfk_1` FOREIGN KEY (`Task_ID`) REFERENCES `task` (`Task_ID`),
  CONSTRAINT `bid_ibfk_2` FOREIGN KEY (`Tradesperson_ID`) REFERENCES `tradesperson` (`Tradesperson_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bid`
--

LOCK TABLES `bid` WRITE;
/*!40000 ALTER TABLE `bid` DISABLE KEYS */;
INSERT INTO `bid` VALUES (1,1,1000000.00,'Accepted'),(2,2,1500000.00,'Accepted'),(3,3,2000000.00,'Accepted'),(4,4,1800000.00,'Pending'),(4,6,1750000.00,'Pending'),(5,5,2500000.00,'Pending'),(5,7,2200000.00,'Pending'),(6,1,800000.00,'Accepted'),(7,2,3000000.00,'Accepted'),(8,3,5000000.00,'Accepted'),(9,4,1200000.00,'Accepted'),(10,5,4000000.00,'Pending'),(10,8,3800000.00,'Pending'),(10,9,4200000.00,'Pending');
/*!40000 ALTER TABLE `bid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `certification`
--

DROP TABLE IF EXISTS `certification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `certification` (
  `Certification_ID` int NOT NULL AUTO_INCREMENT,
  `Certification_Name` varchar(100) NOT NULL,
  `Course_ID` int DEFAULT NULL,
  `Tradesperson_ID` int DEFAULT NULL,
  `Date_Obtained` date DEFAULT NULL,
  PRIMARY KEY (`Certification_ID`),
  KEY `Course_ID` (`Course_ID`),
  KEY `Tradesperson_ID` (`Tradesperson_ID`),
  CONSTRAINT `certification_ibfk_1` FOREIGN KEY (`Course_ID`) REFERENCES `course` (`Course_ID`),
  CONSTRAINT `certification_ibfk_2` FOREIGN KEY (`Tradesperson_ID`) REFERENCES `tradesperson` (`Tradesperson_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `certification`
--

LOCK TABLES `certification` WRITE;
/*!40000 ALTER TABLE `certification` DISABLE KEYS */;
INSERT INTO `certification` VALUES (1,'Certified Plumber',1,1,'2022-02-15'),(2,'Master Electrician',2,2,'2022-11-20'),(3,'Expert Carpenter',3,3,'2023-07-10'),(4,'HVAC Specialist',4,4,'2022-05-05'),(5,'Professional Builder',5,5,'2023-06-12'),(6,'Advanced Plumber',1,1,'2022-08-18'),(7,'Electrical Systems Expert',2,2,'2023-01-22');
/*!40000 ALTER TABLE `certification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `Course_ID` int NOT NULL AUTO_INCREMENT,
  `Course_Name` varchar(100) NOT NULL,
  `Field` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Course_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES (1,'Basic Plumbing','Plumbing'),(2,'Advanced Electrical','Electrical'),(3,'Carpentry Fundamentals','Carpentry'),(4,'HVAC Essentials','HVAC'),(5,'Construction Techniques','Construction');
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `Customer_ID` int NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(50) NOT NULL,
  `LastName` varchar(50) NOT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `Suburb` varchar(50) DEFAULT NULL,
  `State` varchar(20) DEFAULT NULL,
  `Registration_Date` date DEFAULT NULL,
  `Last_Activity_Date` date DEFAULT NULL,
  PRIMARY KEY (`Customer_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Rudi','Hermawan','Jl. Cikini No. 159','Menteng','DKI Jakarta','2023-01-05','2024-03-10'),(2,'Maya','Putri','Jl. Kebon Sirih No. 267','Gambir','DKI Jakarta','2023-02-10','2024-03-12'),(3,'Wayan','Sudiarta','Jl. Raya Kuta No. 378','Kuta','Bali','2023-03-15','2024-03-14'),(4,'Putri','Indah','Jl. Pahlawan No. 489','Medan Maimun','Sumatera Utara','2023-04-20','2024-03-16'),(5,'Joko','Susilo','Jl. Slamet Riyadi No. 591','Serengan','Jawa Tengah','2023-05-25','2024-03-18');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `material`
--

DROP TABLE IF EXISTS `material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `material` (
  `Material_ID` int NOT NULL AUTO_INCREMENT,
  `Material_Name` varchar(100) NOT NULL,
  `Unit_Price` decimal(10,2) NOT NULL,
  `Supplier_ID` int DEFAULT NULL,
  PRIMARY KEY (`Material_ID`),
  KEY `Supplier_ID` (`Supplier_ID`),
  CONSTRAINT `material_ibfk_1` FOREIGN KEY (`Supplier_ID`) REFERENCES `supplier` (`Supplier_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material`
--

LOCK TABLES `material` WRITE;
/*!40000 ALTER TABLE `material` DISABLE KEYS */;
INSERT INTO `material` VALUES (1,'Copper Pipe',105000.00,1),(2,'Electrical Wire',7500.00,2),(3,'Teak Board',250000.00,3),(4,'AC Refrigerant',450000.00,4),(5,'Cement Mix',150000.00,5),(6,'PVC Pipe',87500.00,1),(7,'Circuit Breaker',300000.00,2),(8,'Pine Board',185000.00,3),(9,'AC Filter',120000.00,4),(10,'Brick',8500.00,5);
/*!40000 ALTER TABLE `material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `material_transaction`
--

DROP TABLE IF EXISTS `material_transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `material_transaction` (
  `Order_ID` int NOT NULL,
  `Tradesperson_ID` int NOT NULL,
  `Transaction_Date` date NOT NULL,
  `Payment_Status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Order_ID`,`Tradesperson_ID`,`Transaction_Date`),
  KEY `Tradesperson_ID` (`Tradesperson_ID`),
  CONSTRAINT `material_transaction_ibfk_1` FOREIGN KEY (`Order_ID`) REFERENCES `order` (`Order_ID`),
  CONSTRAINT `material_transaction_ibfk_2` FOREIGN KEY (`Tradesperson_ID`) REFERENCES `tradesperson` (`Tradesperson_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material_transaction`
--

LOCK TABLES `material_transaction` WRITE;
/*!40000 ALTER TABLE `material_transaction` DISABLE KEYS */;
INSERT INTO `material_transaction` VALUES (1,1,'2024-01-15','Completed'),(2,2,'2024-02-20','Completed'),(3,3,'2024-03-22','Pending'),(4,4,'2024-03-27','Pending'),(5,5,'2024-04-01','Pending'),(6,6,'2024-02-10','Completed'),(7,7,'2024-02-25','Completed'),(8,8,'2024-03-18','Pending');
/*!40000 ALTER TABLE `material_transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `Order_ID` int NOT NULL AUTO_INCREMENT,
  `Tradesperson_ID` int DEFAULT NULL,
  `Supplier_ID` int DEFAULT NULL,
  `Order_Date` date DEFAULT NULL,
  `Total_Value` decimal(10,2) NOT NULL,
  `Order_Status` enum('Placed','Processing','Shipped','Delivered') NOT NULL,
  PRIMARY KEY (`Order_ID`),
  KEY `Tradesperson_ID` (`Tradesperson_ID`),
  KEY `Supplier_ID` (`Supplier_ID`),
  CONSTRAINT `order_ibfk_1` FOREIGN KEY (`Tradesperson_ID`) REFERENCES `tradesperson` (`Tradesperson_ID`),
  CONSTRAINT `order_ibfk_2` FOREIGN KEY (`Supplier_ID`) REFERENCES `supplier` (`Supplier_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (1,1,1,'2024-01-10',1050000.00,'Delivered'),(2,2,2,'2024-02-15',2250000.00,'Shipped'),(3,3,3,'2024-03-20',5000000.00,'Processing'),(4,4,4,'2024-03-25',1800000.00,'Placed'),(5,5,5,'2024-03-30',1500000.00,'Placed'),(6,6,1,'2024-02-05',1925000.00,'Delivered'),(7,7,2,'2024-02-20',3000000.00,'Shipped'),(8,8,3,'2024-03-15',3700000.00,'Processing');
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_material`
--

DROP TABLE IF EXISTS `order_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_material` (
  `Order_ID` int NOT NULL,
  `Material_ID` int NOT NULL,
  `Quantity` int NOT NULL,
  PRIMARY KEY (`Order_ID`,`Material_ID`),
  KEY `Material_ID` (`Material_ID`),
  CONSTRAINT `order_material_ibfk_1` FOREIGN KEY (`Order_ID`) REFERENCES `order` (`Order_ID`),
  CONSTRAINT `order_material_ibfk_2` FOREIGN KEY (`Material_ID`) REFERENCES `material` (`Material_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_material`
--

LOCK TABLES `order_material` WRITE;
/*!40000 ALTER TABLE `order_material` DISABLE KEYS */;
INSERT INTO `order_material` VALUES (1,1,10),(2,2,300),(3,3,20),(4,4,4),(5,5,10),(6,1,10),(6,6,10),(7,7,10),(8,8,20);
/*!40000 ALTER TABLE `order_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `Supplier_ID` int NOT NULL AUTO_INCREMENT,
  `SupplierName` varchar(100) NOT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `Suburb` varchar(50) DEFAULT NULL,
  `State` varchar(20) DEFAULT NULL,
  `Registration_Date` date DEFAULT NULL,
  `Last_Activity_Date` date DEFAULT NULL,
  PRIMARY KEY (`Supplier_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (1,'PipaJaya Supplies','Jl. Hayam Wuruk No. 789','Taman Sari','DKI Jakarta','2023-01-01','2024-03-15'),(2,'ElektroMegah Parts','Jl. Ir. H. Juanda No. 456','Bandung Wetan','Jawa Barat','2023-02-01','2024-03-20'),(3,'KayuMakmur Materials','Jl. Panglima Sudirman No. 123','Genteng','Jawa Timur','2023-03-01','2024-03-18'),(4,'DinginSejuk AC','Jl. Urip Sumoharjo No. 321','Makassar','Sulawesi Selatan','2023-04-01','2024-03-22'),(5,'BatuPerkasa Masonry','Jl. Gajah Mada No. 654','Denpasar Utara','Bali','2023-05-01','2024-03-17');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task`
--

DROP TABLE IF EXISTS `task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task` (
  `Task_ID` int NOT NULL AUTO_INCREMENT,
  `Customer_ID` int DEFAULT NULL,
  `Task_Name` varchar(100) NOT NULL,
  `Task_Status` enum('Posted','Bidding','Assigned','In Progress','Completed') NOT NULL,
  `Posting_Date` date DEFAULT NULL,
  `Expiry_Date` date DEFAULT NULL,
  `Tradesperson_ID` int DEFAULT NULL,
  PRIMARY KEY (`Task_ID`),
  KEY `Customer_ID` (`Customer_ID`),
  KEY `Tradesperson_ID` (`Tradesperson_ID`),
  CONSTRAINT `task_ibfk_1` FOREIGN KEY (`Customer_ID`) REFERENCES `customer` (`Customer_ID`),
  CONSTRAINT `task_ibfk_2` FOREIGN KEY (`Tradesperson_ID`) REFERENCES `tradesperson` (`Tradesperson_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task`
--

LOCK TABLES `task` WRITE;
/*!40000 ALTER TABLE `task` DISABLE KEYS */;
INSERT INTO `task` VALUES (1,1,'Fix leaky faucet','Completed','2024-01-05','2024-01-20',1),(2,2,'Install new light fixture','In Progress','2024-02-10','2024-02-25',2),(3,3,'Build custom shelves','Assigned','2024-03-15','2024-03-30',3),(4,4,'Repair AC unit','Posted','2024-03-20','2024-04-05',NULL),(5,5,'Repoint brick wall','Bidding','2024-03-25','2024-04-10',NULL),(6,1,'Unclog drain','Completed','2024-02-01','2024-02-15',1),(7,2,'Rewire basement','Completed','2024-01-15','2024-01-30',2),(8,3,'Install kitchen cabinets','In Progress','2024-03-01','2024-03-16',3),(9,4,'Service furnace','Assigned','2024-02-20','2024-03-07',4),(10,5,'Build retaining wall','Posted','2024-03-10','2024-03-25',NULL);
/*!40000 ALTER TABLE `task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task_transaction`
--

DROP TABLE IF EXISTS `task_transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task_transaction` (
  `Task_ID` int NOT NULL,
  `Customer_ID` int NOT NULL,
  `Transaction_Date` date NOT NULL,
  `Payment_Status` enum('Pending','Completed','Refunded') NOT NULL,
  `Rating` int DEFAULT NULL,
  PRIMARY KEY (`Task_ID`,`Customer_ID`,`Transaction_Date`),
  KEY `Customer_ID` (`Customer_ID`),
  CONSTRAINT `task_transaction_ibfk_1` FOREIGN KEY (`Task_ID`) REFERENCES `task` (`Task_ID`),
  CONSTRAINT `task_transaction_ibfk_2` FOREIGN KEY (`Customer_ID`) REFERENCES `customer` (`Customer_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_transaction`
--

LOCK TABLES `task_transaction` WRITE;
/*!40000 ALTER TABLE `task_transaction` DISABLE KEYS */;
INSERT INTO `task_transaction` VALUES (1,1,'2024-01-18','Completed',5),(2,2,'2024-02-23','Pending',NULL),(3,3,'2024-03-28','Pending',NULL),(6,1,'2024-02-12','Completed',4),(7,2,'2024-01-28','Completed',5),(8,3,'2024-03-10','Pending',NULL),(9,4,'2024-03-05','Pending',NULL);
/*!40000 ALTER TABLE `task_transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tradesperson`
--

DROP TABLE IF EXISTS `tradesperson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tradesperson` (
  `Tradesperson_ID` int NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(50) NOT NULL,
  `LastName` varchar(50) NOT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `Suburb` varchar(50) DEFAULT NULL,
  `State` varchar(20) DEFAULT NULL,
  `Registration_Date` date DEFAULT NULL,
  `Last_Activity_Date` date DEFAULT NULL,
  PRIMARY KEY (`Tradesperson_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tradesperson`
--

LOCK TABLES `tradesperson` WRITE;
/*!40000 ALTER TABLE `tradesperson` DISABLE KEYS */;
INSERT INTO `tradesperson` VALUES (1,'Budi','Santoso','Jl. Sudirman No. 123','Menteng','DKI Jakarta','2022-01-23','2022-03-15'),(2,'Siti','Rahayu','Jl. Thamrin No. 456','Kebayoran Baru','DKI Jakarta','2022-10-01','2023-07-20'),(3,'Agus','Wijaya','Jl. Gajah Mada No. 789','Sawahan','Jawa Timur','2023-06-01','2024-07-18'),(4,'Dewi','Lestari','Jl. Diponegoro No. 321','Tegalsari','Jawa Timur','2022-04-01','2024-08-22'),(5,'Eko','Prasetyo','Jl. Pemuda No. 654','Semarang Tengah','Jawa Tengah','2023-05-01','2024-03-17'),(6,'Sri','Wahyuni','Jl. Asia Afrika No. 987','Sumur Bandung','Jawa Barat','2022-12-01','2024-09-21'),(7,'Hendra','Gunawan','Jl. Veteran No. 147','Mamajang','Sulawesi Selatan','2023-07-01','2024-09-19'),(8,'Rina','Sari','Jl. Gatot Subroto No. 258','Denpasar Barat','Bali','2023-08-01','2024-06-16'),(9,'Andi','Kusuma','Jl. Ahmad Yani No. 369','Ilir Timur I','Sumatera Selatan','2022-09-01','2024-05-23'),(10,'Yuni','Hartono','Jl. Malioboro No. 753','Gedongtengen','DI Yogyakarta','2024-03-01','2024-03-14');
/*!40000 ALTER TABLE `tradesperson` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-04 16:48:28
