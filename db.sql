/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 10.3.16-MariaDB : Database - databasefpprogjar
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`databasefpprogjar` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `databasefpprogjar`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add chat',1,'add_chat'),
(2,'Can change chat',1,'change_chat'),
(3,'Can delete chat',1,'delete_chat'),
(4,'Can view chat',1,'view_chat'),
(5,'Can add message',2,'add_message'),
(6,'Can change message',2,'change_message'),
(7,'Can delete message',2,'delete_message'),
(8,'Can view message',2,'view_message'),
(9,'Can add chat_ acc',3,'add_chat_acc'),
(10,'Can change chat_ acc',3,'change_chat_acc'),
(11,'Can delete chat_ acc',3,'delete_chat_acc'),
(12,'Can view chat_ acc',3,'view_chat_acc'),
(13,'Can add log entry',4,'add_logentry'),
(14,'Can change log entry',4,'change_logentry'),
(15,'Can delete log entry',4,'delete_logentry'),
(16,'Can view log entry',4,'view_logentry'),
(17,'Can add permission',5,'add_permission'),
(18,'Can change permission',5,'change_permission'),
(19,'Can delete permission',5,'delete_permission'),
(20,'Can view permission',5,'view_permission'),
(21,'Can add group',6,'add_group'),
(22,'Can change group',6,'change_group'),
(23,'Can delete group',6,'delete_group'),
(24,'Can view group',6,'view_group'),
(25,'Can add user',7,'add_user'),
(26,'Can change user',7,'change_user'),
(27,'Can delete user',7,'delete_user'),
(28,'Can view user',7,'view_user'),
(29,'Can add content type',8,'add_contenttype'),
(30,'Can change content type',8,'change_contenttype'),
(31,'Can delete content type',8,'delete_contenttype'),
(32,'Can view content type',8,'view_contenttype'),
(33,'Can add session',9,'add_session'),
(34,'Can change session',9,'change_session'),
(35,'Can delete session',9,'delete_session'),
(36,'Can view session',9,'view_session'),
(37,'Can add room',1,'add_room'),
(38,'Can change room',1,'change_room'),
(39,'Can delete room',1,'delete_room'),
(40,'Can view room',1,'view_room'),
(41,'Can add room_ acc',3,'add_room_acc'),
(42,'Can change room_ acc',3,'change_room_acc'),
(43,'Can delete room_ acc',3,'delete_room_acc'),
(44,'Can view room_ acc',3,'view_room_acc');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$180000$T9kSVKAAeUFS$CaKE4LVtMnjWbCcFLSDx6MIVEVz2EQ1HrBz8p+OmuRk=','2020-05-24 03:07:07.255858',0,'mhdfadlyhasanss','','','',0,1,'2020-05-19 10:04:40.178643'),
(2,'pbkdf2_sha256$180000$C1nAQEYGzCcT$yJvlpCZpWQmQ4In8Itb8YrYD/VzWqsigtz0mAWzk1HA=','2020-05-19 13:09:39.281752',0,'pogger','','','',0,0,'2020-05-19 13:09:38.992090'),
(4,'pbkdf2_sha256$180000$oh3utA0iz6nU$ffdJMRWwKyQSdcURBKeX2WnRd4KVteKBdQJCQXwqB+o=','2020-05-20 05:38:24.291007',0,'hzzzeys','','','burh@gmail.com',0,1,'2020-05-20 05:38:05.200168'),
(7,'pbkdf2_sha256$180000$LSVMhNvJR7no$HdjetyPVefJ8IofbSXT4XHPmLZSpF2iTBJcXdcf1W1w=','2020-05-24 03:11:05.800467',0,'mhdfadlyhasan','','','mhdfadlyhasan16a11@gmail.coms',0,1,'2020-05-24 03:10:28.249554'),
(8,'sdasdf',NULL,0,'','','','',0,0,'0000-00-00 00:00:00.000000'),
(9,'',NULL,0,'asdf','','','',0,0,'0000-00-00 00:00:00.000000'),
(10,'pbkdf2_sha256$180000$g1DOkb8brxCb$65Oye8C5Fhzjz4LIj+B1u8j09b/FnMbL3sHXcBTg8JQ=',NULL,0,'fadlytesting','','','mhdfadlyhasan16a1@gmail.comssasdf',0,1,'2020-06-01 06:20:25.740491'),
(17,'',NULL,0,'asdfasd','','','asdfasdfasdfasdfasdfasd',0,0,'0000-00-00 00:00:00.000000'),
(18,'pbkdf2_sha256$180000$FLCXVnNSMnmx$YmW5f/fnFxuxqQzDlTUoSTYaevxnAf1spVNJzUYymLw=',NULL,0,'051117400078','','','mhdfadlyhasan16a1@gmail.comssssdfdf',0,0,'2020-06-01 07:36:51.017404'),
(19,'pbkdf2_sha256$180000$iu0oPDwbJ6N3$syQDpiCzN4LrdtW/45nEPi3kZIHNSd1GP/FraZrcnlc=',NULL,0,'mhdfadlyhasana','','','mhdfadlyhasan16a1@gmail.comsssdfsdf',0,0,'2020-06-01 08:15:18.629470'),
(20,'pbkdf2_sha256$180000$XohSfpaeBSuO$kf2r/MiXOsBc3wIg0athSgzPE1kE52VBpDLvQpVmIn8=',NULL,0,'progjarteam3','','','mhdfadlyhasan16a1sdfsdf@gmail.com',0,1,'2020-06-02 02:17:23.231824'),
(21,'pbkdf2_sha256$180000$Wn9Y0SNrzxkN$UG1h1/Q4yALhGQMYaNBEFKjfwurWAjQwpyzWorRUARc=',NULL,0,'team3','','','mhdfadlyhasan16a1@gmail.com',0,1,'2020-06-02 05:45:04.360078');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `chat_message` */

DROP TABLE IF EXISTS `chat_message`;

CREATE TABLE `chat_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `msg` varchar(50) NOT NULL,
  `getTime` datetime(6) NOT NULL,
  `AccSent_id` int(11) NOT NULL,
  `room_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chat_message_AccSent_id_2f32fb04_fk_auth_user_id` (`AccSent_id`),
  KEY `chat_message_room_id_5e7d8d78_fk_chat_room_id` (`room_id`),
  CONSTRAINT `chat_message_AccSent_id_2f32fb04_fk_auth_user_id` FOREIGN KEY (`AccSent_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `chat_message_room_id_5e7d8d78_fk_chat_room_id` FOREIGN KEY (`room_id`) REFERENCES `chat_room` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=255 DEFAULT CHARSET=latin1;

/*Data for the table `chat_message` */

insert  into `chat_message`(`id`,`msg`,`getTime`,`AccSent_id`,`room_id`) values 
(99,'fad','2020-05-31 10:41:44.306103',4,7),
(100,'jir bro','2020-05-31 10:41:55.070597',1,7),
(101,'<','2020-05-31 11:45:53.256669',4,7),
(102,'ko','2020-05-31 11:46:03.513962',4,7),
(103,'fad','2020-05-31 11:56:34.434903',1,7),
(104,'Pog','2020-05-31 12:43:31.065742',1,7),
(105,'fadly','2020-05-31 13:19:01.555617',1,7),
(106,'a','2020-05-31 13:39:29.702968',4,7),
(107,'d','2020-05-31 13:39:32.489512',4,7),
(108,'adsf','2020-05-31 13:39:33.471884',4,7),
(109,'asd','2020-05-31 13:39:33.821946',4,7),
(110,'dsf','2020-05-31 13:39:34.027398',4,7),
(111,'asfd','2020-05-31 13:39:34.254789',4,7),
(112,'afds','2020-05-31 13:39:34.367488',4,7),
(113,'af','2020-05-31 13:39:34.591885',4,7),
(114,'fad','2020-05-31 14:01:00.859460',4,7),
(115,'fad','2020-05-31 14:05:32.750248',4,7),
(116,'test','2020-05-31 14:05:49.501422',4,7),
(117,'jir bro','2020-05-31 14:05:51.000179',4,7),
(118,'waduh','2020-05-31 14:05:53.055812',1,7),
(119,'waduu moment','2020-05-31 14:05:59.253857',1,7),
(120,'test','2020-05-31 14:06:35.505980',1,7),
(121,'asdfasd','2020-05-31 14:06:38.107020',1,7),
(122,'asdfadsf','2020-05-31 14:06:41.104000',1,7),
(123,'hah','2020-05-31 15:12:50.426984',1,7),
(124,'fad','2020-05-31 15:14:27.255557',1,7),
(125,'fad','2020-05-31 15:16:59.524604',1,7),
(126,'ok','2020-05-31 15:29:09.800517',1,7),
(127,'fad','2020-05-31 15:47:48.307820',2,1),
(128,'fad','2020-05-31 15:48:22.292435',1,1),
(129,'apa slur','2020-05-31 15:48:29.329340',2,1),
(130,'tod','2020-05-31 15:48:35.081160',1,1),
(131,'yo fad','2020-05-31 15:55:38.138545',1,1),
(132,'apa slur','2020-05-31 15:55:41.507534',4,1),
(133,'lsh','2020-05-31 15:55:56.329109',1,1),
(134,'aoa','2020-05-31 15:56:00.935146',4,1),
(135,'gaoaoa gan','2020-05-31 15:56:04.813880',1,1),
(136,'jir bro','2020-05-31 15:56:08.801202',4,1),
(137,'a','2020-05-31 16:12:30.333436',4,1),
(138,'yikes','2020-05-31 16:12:32.956603',1,1),
(139,'adsf','2020-05-31 16:14:22.299054',4,1),
(140,'hah','2020-05-31 16:16:36.169672',4,1),
(141,'wkwkw','2020-05-31 16:16:42.916062',1,1),
(142,'ok','2020-05-31 16:17:08.998583',1,1),
(143,'ok','2020-05-31 16:17:11.895384',4,1),
(144,'dan','2020-05-31 16:17:12.668792',4,1),
(145,'gimana kabar fad?','2020-05-31 16:17:16.085151',4,1),
(146,'wah sehat bro','2020-05-31 16:17:19.416860',1,1),
(147,'ngapai bro?','2020-05-31 16:23:08.689745',8,1),
(148,'test','2020-05-31 17:46:05.621411',1,1),
(149,'fad','2020-06-01 05:23:57.151754',1,14),
(150,'ok','2020-06-01 05:24:00.625565',1,14),
(151,'yo fad','2020-06-01 05:26:31.973200',1,14),
(152,'fad','2020-06-01 05:28:40.791188',1,13),
(153,'bro','2020-06-01 06:40:57.228551',1,13),
(154,'test bro','2020-06-01 06:42:33.863878',1,14),
(155,'as','2020-06-01 06:44:28.218848',9,14),
(156,'asdf','2020-06-01 06:44:45.717894',1,14),
(157,'jir','2020-06-01 06:45:48.555800',9,14),
(158,'asd','2020-06-01 06:47:57.658122',1,14),
(159,'a','2020-06-01 06:48:23.304697',1,14),
(160,'maksud','2020-06-01 06:48:26.843402',9,14),
(161,'jir','2020-06-01 06:49:22.639497',9,13),
(162,'ah','2020-06-01 06:49:28.341803',1,13),
(163,'ke double ya','2020-06-01 06:49:32.299512',1,13),
(164,'kedouble ya?','2020-06-01 06:49:36.289217',9,13),
(165,'fad','2020-06-01 06:57:00.195255',9,13),
(166,'ya?','2020-06-01 06:57:33.724139',9,14),
(167,'ada','2020-06-01 06:58:03.693213',1,13),
(168,'ad','2020-06-01 06:58:20.579263',9,14),
(169,'ad','2020-06-01 06:59:30.593588',9,14),
(170,'a','2020-06-01 07:00:18.118251',9,14),
(171,'aasdf','2020-06-01 07:02:16.848677',9,14),
(172,'fad','2020-06-01 07:02:55.916185',9,14),
(173,'asd','2020-06-01 07:03:29.479280',1,14),
(174,'asdf','2020-06-01 07:06:41.954811',1,14),
(175,'asdf','2020-06-01 07:07:31.941507',1,14),
(176,'fad','2020-06-01 07:15:17.054849',9,14),
(177,'fads','2020-06-01 07:16:43.551395',1,14),
(178,'ada apa lur?','2020-06-01 07:16:56.358547',9,14),
(179,'gapapa slur','2020-06-01 07:17:00.455893',1,14),
(180,'lancar tapi kan?','2020-06-01 07:17:30.768372',1,14),
(181,'lancar jaya lur','2020-06-01 07:18:08.987171',1,14),
(182,'harusnya ga dapat','2020-06-01 07:18:17.567367',1,14),
(183,'dapat kah?','2020-06-01 07:18:29.513083',1,13),
(184,'pekopekopeko','2020-06-01 14:02:54.000000',10,16),
(185,'asdf','2020-06-01 17:06:25.888206',10,19),
(186,'yo fad','2020-06-01 17:09:15.259135',10,20),
(187,'selamat pagi fad','2020-06-02 09:34:07.940834',20,19),
(188,'halo','2020-06-02 09:46:46.362761',10,19),
(189,'fad','2020-06-02 11:29:43.709133',10,32),
(190,'fad','2020-06-02 11:38:31.428365',10,33),
(191,'ok','2020-06-02 11:38:48.132217',20,33),
(192,'fad','2020-06-02 11:43:05.950666',10,34),
(193,'ok','2020-06-02 11:43:40.499206',10,34),
(194,'he?','2020-06-02 11:44:07.272787',10,34),
(195,'ada apa','2020-06-02 11:44:18.243481',10,34),
(196,'asdf','2020-06-02 11:44:24.103418',20,34),
(197,'fad','2020-06-02 11:52:47.746157',10,34),
(198,'apa brom','2020-06-02 11:53:08.121552',10,34),
(199,'fad','2020-06-02 11:55:16.768031',10,34),
(200,'fad','2020-06-02 11:55:23.625448',10,34),
(201,'fad','2020-06-02 11:56:45.231937',10,34),
(202,'test','2020-06-02 12:01:02.791277',10,34),
(203,'ok','2020-06-02 12:01:08.615959',20,34),
(204,'a','2020-06-02 12:01:23.054259',10,34),
(205,'ok','2020-06-02 12:01:40.234710',20,34),
(206,'fad','2020-06-02 12:07:12.090092',10,34),
(207,'ok','2020-06-02 12:07:15.654709',20,34),
(208,'yo fad','2020-06-02 12:10:06.642314',20,34),
(209,'ok','2020-06-02 12:10:09.036983',10,34),
(210,'a','2020-06-02 12:10:30.306677',10,34),
(211,'fad','2020-06-02 12:12:19.410678',20,34),
(212,'ok','2020-06-02 12:12:21.770137',10,34),
(213,'fadly','2020-06-02 12:14:10.844291',20,34),
(214,'fad','2020-06-02 12:15:24.617338',20,34),
(215,'ok','2020-06-02 12:15:29.016524',10,34),
(216,'a','2020-06-02 12:15:44.643765',10,34),
(217,'fad','2020-06-02 12:21:38.535185',20,33),
(218,'ok','2020-06-02 12:21:49.625514',20,34),
(219,'yo','2020-06-02 12:22:31.138853',10,35),
(220,'mantap','2020-06-02 12:22:33.885605',20,35),
(221,'fad','2020-06-02 12:24:34.888910',10,35),
(222,'uo dly','2020-06-02 12:25:01.690992',10,34),
(223,'ada apa?','2020-06-02 12:25:04.888286',20,34),
(224,'fad','2020-06-02 12:34:26.083517',10,34),
(225,'apa bro','2020-06-02 12:34:28.452283',20,34),
(226,'as','2020-06-02 12:34:34.353268',20,34),
(227,'hah?','2020-06-02 12:34:40.752789',10,34),
(228,'adsf','2020-06-02 12:35:19.124453',20,34),
(229,'yo','2020-06-02 12:36:21.868006',10,33),
(230,'yo','2020-06-02 12:36:24.069463',20,33),
(231,'asd','2020-06-02 12:36:37.578612',10,33),
(232,'fad','2020-06-02 12:38:59.029407',20,36),
(233,'fadly','2020-06-02 12:42:03.222491',10,37),
(234,'waduh','2020-06-02 12:42:39.270848',10,38),
(235,'teset','2020-06-02 12:47:52.735361',20,39),
(236,'fad','2020-06-02 12:47:59.872667',21,39),
(237,'test','2020-06-02 12:48:40.048191',20,40),
(238,'fad','2020-06-02 12:48:42.505990',21,40),
(239,'fad','2020-06-02 12:56:40.398697',21,40),
(240,'ok','2020-06-02 12:56:42.321558',10,40),
(241,'asdf','2020-06-02 12:56:48.401333',10,40),
(242,'ok','2020-06-02 13:12:19.855601',10,40),
(243,'yo','2020-06-02 13:12:41.270638',21,41),
(244,'asdf','2020-06-02 14:47:34.376134',10,42),
(245,'fad','2020-06-02 14:49:31.935434',21,42),
(246,'fad','2020-06-02 14:49:37.063146',10,42),
(247,'ada apa?','2020-06-02 14:49:47.382770',21,42),
(248,'fad','2020-06-02 14:50:13.020176',10,43),
(249,'ada apa?','2020-06-02 14:50:18.234456',21,43),
(250,'gapapa','2020-06-02 14:50:25.605145',10,43),
(251,'adsf','2020-06-02 14:58:30.113276',21,43),
(252,'pog','2020-06-02 15:01:02.689466',10,43),
(253,'loh','2020-06-02 15:01:08.681799',21,43),
(254,'berhasil?','2020-06-02 15:01:12.339025',10,43);

/*Table structure for table `chat_room` */

DROP TABLE IF EXISTS `chat_room`;

CREATE TABLE `chat_room` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `RoomName` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=latin1;

/*Data for the table `chat_room` */

insert  into `chat_room`(`id`,`RoomName`) values 
(1,'GijinkaTc'),
(2,'1'),
(3,'1'),
(4,'1'),
(5,'4'),
(6,'yikes'),
(7,'69'),
(9,'faad'),
(10,'fusasdfasdaadsa'),
(11,'fasss'),
(12,'asdfsad'),
(13,'asdfasdf'),
(14,'asgdasdgfasdgf'),
(15,'asdf'),
(16,'loh'),
(17,'GTA V SKUD'),
(18,'mhdfadlyhasanss'),
(19,'hzzzeys'),
(20,'asdf'),
(21,'fadlytesting - progjarteam3'),
(22,'progjarteam3 - mhdfadlyhasanss'),
(23,'okakoro zombie'),
(24,'fadlytesting - mhdfadlyhasanss'),
(25,'okakoro zombie part 2'),
(26,'wadu'),
(27,'fadlytesting - mhdfadlyhasanss'),
(28,'fadlytesting - hzzzeys'),
(29,'testing baru'),
(30,'progjarteam3 - fadlytesting'),
(31,'fadlytesting - fadlytesting'),
(32,'fadlytesting - progjarteam3'),
(33,'group anti crash'),
(34,'gropu charsh'),
(35,'team3progjar'),
(36,'tim fadly'),
(37,'fadlytesting - progjarteam3'),
(38,'teambaru'),
(39,'progjarteam3 - team3'),
(40,'Team 3 Progjar'),
(41,'fadlytesting - team3'),
(42,'testingfadly'),
(43,'team3 - fadlytesting'),
(44,'final project');

/*Table structure for table `chat_room_acc` */

DROP TABLE IF EXISTS `chat_room_acc`;

CREATE TABLE `chat_room_acc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `AccID_id` int(11) NOT NULL,
  `RoomID_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chat_room_acc_AccID_id_38a98a37_fk_auth_user_id` (`AccID_id`),
  KEY `chat_room_acc_RoomID_id_be59b66f_fk_chat_room_id` (`RoomID_id`),
  CONSTRAINT `chat_room_acc_AccID_id_38a98a37_fk_auth_user_id` FOREIGN KEY (`AccID_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `chat_room_acc_RoomID_id_be59b66f_fk_chat_room_id` FOREIGN KEY (`RoomID_id`) REFERENCES `chat_room` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=latin1;

/*Data for the table `chat_room_acc` */

insert  into `chat_room_acc`(`id`,`AccID_id`,`RoomID_id`) values 
(1,1,1),
(2,4,1),
(6,4,1),
(8,7,1),
(9,7,1),
(10,2,5),
(11,4,5),
(13,2,6),
(14,1,7),
(15,2,7),
(16,1,7),
(17,1,1),
(18,1,9),
(19,1,10),
(20,1,11),
(21,4,1),
(22,1,12),
(23,1,13),
(24,1,14),
(25,8,15),
(27,8,1),
(28,9,14),
(29,9,13),
(30,10,14),
(31,10,16),
(32,1,16),
(33,10,17),
(34,1,17),
(36,10,18),
(37,1,18),
(38,10,19),
(39,4,19),
(40,10,20),
(41,9,20),
(42,20,19),
(47,10,23),
(48,10,24),
(49,1,24),
(50,10,25),
(51,10,26),
(52,10,27),
(53,1,27),
(54,10,28),
(55,4,28),
(56,20,17),
(59,20,29),
(60,10,29),
(63,10,31),
(64,10,31),
(65,10,32),
(66,20,32),
(67,20,33),
(68,10,33),
(69,20,34),
(70,10,34),
(71,20,35),
(72,10,35),
(73,10,36),
(74,20,36),
(75,10,37),
(76,20,37),
(77,20,38),
(78,10,38),
(79,20,39),
(80,21,39),
(81,21,40),
(82,20,40),
(83,10,40),
(84,10,41),
(85,21,41),
(86,10,42),
(87,21,42),
(88,21,43),
(89,10,43),
(90,10,44),
(91,21,44),
(92,20,44);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(4,'admin','logentry'),
(6,'auth','group'),
(5,'auth','permission'),
(7,'auth','user'),
(2,'chat','message'),
(1,'chat','room'),
(3,'chat','room_acc'),
(8,'contenttypes','contenttype'),
(9,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2020-05-19 10:02:18.298354'),
(2,'auth','0001_initial','2020-05-19 10:02:20.218369'),
(3,'admin','0001_initial','2020-05-19 10:02:27.369480'),
(4,'admin','0002_logentry_remove_auto_add','2020-05-19 10:02:29.619204'),
(5,'admin','0003_logentry_add_action_flag_choices','2020-05-19 10:02:29.647797'),
(6,'contenttypes','0002_remove_content_type_name','2020-05-19 10:02:31.148351'),
(7,'auth','0002_alter_permission_name_max_length','2020-05-19 10:02:31.217826'),
(8,'auth','0003_alter_user_email_max_length','2020-05-19 10:02:31.275937'),
(9,'auth','0004_alter_user_username_opts','2020-05-19 10:02:31.306227'),
(10,'auth','0005_alter_user_last_login_null','2020-05-19 10:02:32.238761'),
(11,'auth','0006_require_contenttypes_0002','2020-05-19 10:02:32.308933'),
(12,'auth','0007_alter_validators_add_error_messages','2020-05-19 10:02:32.340574'),
(13,'auth','0008_alter_user_username_max_length','2020-05-19 10:02:32.410569'),
(14,'auth','0009_alter_user_last_name_max_length','2020-05-19 10:02:32.487436'),
(15,'auth','0010_alter_group_name_max_length','2020-05-19 10:02:32.958600'),
(16,'auth','0011_update_proxy_permissions','2020-05-19 10:02:33.123699'),
(17,'chat','0001_initial','2020-05-19 10:02:34.186896'),
(18,'chat','0002_account_acc_password','2020-05-19 10:02:37.849018'),
(19,'chat','0003_auto_20200519_1649','2020-05-19 10:02:40.159133'),
(20,'chat','0004_delete_account','2020-05-19 10:02:40.826742'),
(21,'sessions','0001_initial','2020-05-19 10:02:41.327541'),
(22,'chat','0005_auto_20200530_1141','2020-05-30 04:41:33.645667');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('v9esiwgvmuhbetn7hkt47k5fwqixfv3y','NWFjZThiZDdhMTdjZDc5YjI2ZDViMzYwNDhkNjQwZjBlMDFhYmQxYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlMzJjYmI4ZWQ5ZjFmMTU3Njc1MTk4OTIzMjc5N2I1YWFlZWY5MTRlIn0=','2020-06-04 20:31:30.088794');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
