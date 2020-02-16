-- MySQL dump 10.16  Distrib 10.1.38-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: youngtrip
-- ------------------------------------------------------
-- Server version	5.7.28

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
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$150000$qAy45m0AlicN$ngNWNOSlEV3x8ygck86/49m/Uasw2ExaASZHEcJ0cN0=','2020-02-11 03:14:40.378024',1,'admin','','798945742@qq.com',1,1,'2020-01-25 00:29:07.188504','');
INSERT INTO `auth_user` VALUES (2,'pbkdf2_sha256$150000$bBGsdrAgYHhg$HyxpESsU+WlB/Z/8hlzEGLaxFmHEF9kctiW39wNbPyc=',NULL,0,'zhangsan','','test1@qq.com',0,1,'2020-01-25 07:28:41.041561','');
INSERT INTO `auth_user` VALUES (3,'pbkdf2_sha256$150000$e4fZEAX9KPxE$y6RJNOMST26IBrX/e5yRkZd5TYy3noyrJtXhSpBoJBI=',NULL,0,'lisi','','test2@qq.com',0,1,'2020-01-25 08:20:00.807614','');
INSERT INTO `auth_user` VALUES (4,'pbkdf2_sha256$150000$mGZ5rvTPpoLn$2y+p+L0v7/1kTB1fskhuHYMM++/pv7qw3QR3bcuFGlQ=',NULL,0,'anni','','test3@qq.com',0,1,'2020-01-25 14:08:49.861077','');
INSERT INTO `auth_user` VALUES (6,'pbkdf2_sha256$150000$Ws1CWHEpauts$8dLYyKwgtrwY7OC+I3XC3e7JMjKJRC/YpJSMBCkhvf4=',NULL,0,'beta','','test5@qq.com',0,1,'2020-01-26 08:52:59.461214','');
INSERT INTO `auth_user` VALUES (7,'pbkdf2_sha256$150000$FVVbBawalqgs$v9sKES954AE3q8CI8QULR1ailwVmjS0tZ2CD+HmUNH0=',NULL,0,'hellokity','','lizhenqiang@cqnu.edu.cn',0,1,'2020-01-28 09:07:47.743493','');

/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `account_userprofile`
--

DROP TABLE IF EXISTS `account_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `avatar` varchar(100) DEFAULT NULL,
  `sex` varchar(10) NOT NULL,
  `sign` varchar(100) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_userprofile_user_id_5afa3c7a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_userprofile`
--

LOCK TABLES `account_userprofile` WRITE;
/*!40000 ALTER TABLE `account_userprofile` DISABLE KEYS */;
INSERT INTO `account_userprofile` VALUES (1,'https://api.adorable.io/avatars/200/admin.png','female','努力加油!https',1);
INSERT INTO `account_userprofile` VALUES (2,'https://api.adorable.io/avatars/200/test1.png','0','',2);
INSERT INTO `account_userprofile` VALUES (3,'https://api.adorable.io/avatars/200/test2.png','0','',3);
INSERT INTO `account_userprofile` VALUES (4,'https://api.adorable.io/avatars/200/test3.png','0','',4);
INSERT INTO `account_userprofile` VALUES (5,'https://api.adorable.io/avatars/200/test5.png','0','',6);
/*!40000 ALTER TABLE `account_userprofile` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `card_card`
--

DROP TABLE IF EXISTS `card_card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `card_card` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(80) DEFAULT NULL,
  `pic` varchar(100) DEFAULT NULL,
  `content` varchar(400) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `createtime` datetime(6) NOT NULL,
  `updatetime` datetime(6) NOT NULL,
  `userprofile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `card_card_userprofile_id_b55e4769_fk_account_userprofile_id` (`userprofile_id`),
  CONSTRAINT `card_card_userprofile_id_b55e4769_fk_account_userprofile_id` FOREIGN KEY (`userprofile_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `card_card`
--

LOCK TABLES `card_card` WRITE;
/*!40000 ALTER TABLE `card_card` DISABLE KEYS */;
INSERT INTO `card_card` VALUES (1,'新墨西哥州Albuquerque# 浪漫的热气球节和似雪的白色沙滩','card/image/homecard1.jpg','暑假从国内回来，我们就准备着自驾前往新墨西哥州参加全世界最大的热气球节。先来说说我们这三天的行程安排，由于我和谢博士都喜欢自由散漫的旅行方式，我们这次的行程也没有安排得太紧。主要活动是【Albuquerque热气球节-白色沙漠-Santa Fe（新墨西哥州的州府）】','2020-02-06','墨西哥','2020-02-06 04:14:41.318958','2020-02-06 10:36:55.896874',1);
INSERT INTO `card_card` VALUES (2,'非洲海岛流浪记🇲🇺毛里求斯','card/image/homecard2.jpg','酒店有随处可见的美丽风景，也有随处可见的超舒服的沙发让人relax，看到很多情侣就躺在沙发上看看风景看看书喝喝饮料发发呆，让人不禁感叹这才是享受生活呐！','2020-02-06','非洲','2020-02-06 04:16:05.875953','2020-02-06 04:16:05.875987',2);
INSERT INTO `card_card` VALUES (3,'滇川藏区，从泸沽湖畔到稻城亚丁','card/image/homecard3.jpg','秋天是祖国各地最美的时候，10月中旬的高原地区，天高气爽，碧空如洗，层林尽染，金黄遍地。我们从成都出发自驾，沿着“天路”雅西高速过西昌进云南，穿过如仙女般的泸沽湖，取道丽江，过虎跳峡和小中甸到香格里拉，看过普达措的蜀都湖又转过松赞林寺的转经筒，一路北上去德钦的飞来寺欣赏梅里雪山的日照金山，然后回到四川，来到天堂般的稻城亚丁。后面他们还要接着沿G317去色达、黑水和毕棚沟，我因为没假就从亚丁机场返程。','2020-02-06','中国,迪庆藏族自治州','2020-02-06 04:17:09.674081','2020-02-06 04:17:09.674146',3);
INSERT INTO `card_card` VALUES (4,'大寫的墨西哥🇲🇽&哈瓦那','card/image/homecard4.jpg','半夜的航班讓我很困','2020-02-06','古巴,哈瓦那','2020-02-06 04:17:36.002299','2020-02-06 04:17:36.002331',4);
INSERT INTO `card_card` VALUES (5,'【马尔代夫】掉进果冻色的梦','card/image/homecard5.jpg','辛苦忙碌了一年，到2019年末终于下定决心出门好好放松一下，果断请了一直不敢请的5天年假。休假最主要的目的之一也是陪老妈好好放松下，于是把选择权给了她，而老妈怀揣着年轻时的满腔向往选择了马代。就这样开始了做攻略预订出行的一系列工作。马尔代夫是著名的“一岛一酒店”，出行前最重要的就是选择要去的岛，之后除了想要换岛体验的情况之外，就可以上岛开始无需辗转的度假时光了。','2020-02-06','马尔代夫','2020-02-06 04:17:53.503130','2020-02-06 04:17:53.503156',2);
INSERT INTO `card_card` VALUES (6,'天上人间','card/image/homecard5.jpg','乐趣无穷 哥哥哥','2020-02-06','杭州','2020-02-06 04:18:31.608326','2020-02-10 02:54:04.447020',1);

/*!40000 ALTER TABLE `card_card` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment_comment`
--

DROP TABLE IF EXISTS `comment_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(100) DEFAULT NULL,
  `date` datetime(6) NOT NULL,
  `card_id` int(11) NOT NULL,
  `userprofile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `comment_comment_card_id_160fbb7c_fk_card_card_id` (`card_id`),
  KEY `comment_comment_userprofile_id_001b24b0_fk_account_u` (`userprofile_id`),
  CONSTRAINT `comment_comment_card_id_160fbb7c_fk_card_card_id` FOREIGN KEY (`card_id`) REFERENCES `card_card` (`id`),
  CONSTRAINT `comment_comment_userprofile_id_001b24b0_fk_account_u` FOREIGN KEY (`userprofile_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment_comment`
--

LOCK TABLES `comment_comment` WRITE;
/*!40000 ALTER TABLE `comment_comment` DISABLE KEYS */;
INSERT INTO `comment_comment` VALUES (2,'我要评论了哦啊','2020-02-08 08:01:56.909904',1,2);
INSERT INTO `comment_comment` VALUES (3,'评论','2020-02-08 08:02:47.365471',1,3);
INSERT INTO `comment_comment` VALUES (5,'在此评测在此','2020-02-08 12:46:23.432476',1,1);
INSERT INTO `comment_comment` VALUES (10,'测试','2020-02-08 13:36:00.856587',1,1);
INSERT INTO `comment_comment` VALUES (11,'评论一下','2020-02-09 11:57:23.095278',2,1);
INSERT INTO `comment_comment` VALUES (12,'评论一下把','2020-02-10 04:32:46.022857',6,1);
INSERT INTO `comment_comment` VALUES (13,'你需要评论吗？？','2020-02-10 03:50:41.109018',4,1);


/*!40000 ALTER TABLE `comment_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `like_like`
--

DROP TABLE IF EXISTS `like_like`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `like_like` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `card_id` int(11) NOT NULL,
  `userprofile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `like_like_card_id_userprofile_id_ae138772_uniq` (`card_id`,`userprofile_id`),
  KEY `like_like_userprofile_id_557f576d_fk_account_userprofile_id` (`userprofile_id`),
  CONSTRAINT `like_like_card_id_251c22d1_fk_card_card_id` FOREIGN KEY (`card_id`) REFERENCES `card_card` (`id`),
  CONSTRAINT `like_like_userprofile_id_557f576d_fk_account_userprofile_id` FOREIGN KEY (`userprofile_id`) REFERENCES `account_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `like_like`
--

LOCK TABLES `like_like` WRITE;
/*!40000 ALTER TABLE `like_like` DISABLE KEYS */;
INSERT INTO `like_like` VALUES (45,1,2);
INSERT INTO `like_like` VALUES (46,1,3);
INSERT INTO `like_like` VALUES (70,2,1);
INSERT INTO `like_like` VALUES (77,3,1);
INSERT INTO `like_like` VALUES (89,6,2);
INSERT INTO `like_like` VALUES (94,6,1);
INSERT INTO `like_like` VALUES (95,1,1);
/*!40000 ALTER TABLE `like_like` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-16 22:35:44
